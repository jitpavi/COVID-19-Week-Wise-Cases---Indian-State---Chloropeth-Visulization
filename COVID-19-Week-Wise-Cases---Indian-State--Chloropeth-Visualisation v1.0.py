"""
Code Name: COVID-19-Week-Wise-Cases---Indian-State--Chloropeth-Visualisation
Code Author: Jitin Pavithran
Code Version: 1.0
Code Description: This project will produce the Chloropeth map to visualize the number of cases in each state of India starting from Week 10 of the year 2020.
"""

# Import all the important libraries required for this code

import pandas as pd
import requests
import plotly.express as px
from dateutil.parser import parse

# Access the API which maintains the live data of the Covid-19 cases in each State of India
time_series_df = pd.read_csv("https://api.covid19india.org/csv/latest/state_wise_daily.csv")
time_series_df_con = time_series_df[time_series_df['Status']=="Confirmed"]

# Retrieve the code names of each state mentioned in the columns
col_list = time_series_df_con.columns.values.tolist()

# Create a master list which will contain the list of tuples
master_list = []

for index,row in time_series_df_con.iterrows():
    for c in col_list[3:]:
        if row[c] != 0:
            row_list = []
            row_list.append(row['Date'])
            row_list.append(c)
            row_list.append(row[c])
            master_list.append(tuple(row_list)) # Each tuple host the reported date,State code name and No.of Cases reported on that date

# Build a new Dataframe holding the tuples created in above step
master_df = pd.DataFrame(master_list,columns=['Detected_Date','State_Code','Cases_Reported'])

# Parse the dates and convert the datatype into DateTime
master_df['Detected_Date'] = master_df['Detected_Date'].apply(lambda x: parse(x,fuzzy=True))

# Convert the datetime format in the form of Year-Week
master_df['Detected_Date'] = master_df['Detected_Date'].dt.strftime('%Y-%U')

#State_Code_list = sorted(col_list[3:])

# Create a Dataframe which will hold the columns of Code names and State names
ISO_Code = pd.read_csv(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Covid_statewise_chloropeth\iso_code_state_india-1583j.csv",)

# Clean the data of State name column
ISO_Code['Subdivision name'] = ISO_Code['Subdivision name'].str.replace('\[.*\]',"")
ISO_Code['Code'] = ISO_Code['Code'].str.replace('IN-',"")
ISO_Code.sort_values(by='Code',inplace=True,ignore_index=True)

# State_Name = sorted(ISO_Code['Subdivision name'][:36].unique())

# Create a dictionary containing the mappings of Code names with State names
State_Code_Name_dict = {}

for i,r in ISO_Code.iterrows():
    State_Code_Name_dict[r['Code']] = r['Subdivision name'] # Update the dictionary with the mappings for each Code using the for loop

# Add a new column in the Master Dataframe containing the State Names
master_df['State_Name'] = master_df['State_Code'].apply(lambda x:State_Code_Name_dict[x])

# Save the Master Dataframe into a CSV file
master_df.to_csv(r"C:\Users\jpavithr\OneDrive - Capgemini\Desktop\Automation Drive - Python training\Pandas\real python\Covid_statewise_chloropeth\state_wise_masterdata.csv")

# Access the JSON object holding the GEOCodes for each State of India
repo_url = 'https://raw.githubusercontent.com/Subhash9325/GeoJson-Data-of-Indian-States/master/Indian_States'
indian_state_geo = requests.get(repo_url).json()

# Creat Cholopeth figure object and providing all the required inputs taken from the Master Dataframe
fig = px.choropleth(master_df,
                    geojson= indian_state_geo,
                    locations="State_Name",
                    color="Cases_Reported",
                    featureidkey='properties.NAME_1',
                    animation_frame="Detected_Date",
                    hover_name="State_Name",
                    title = "Week-Wise COVID cases in Indian States",
                    scope="asia",
                   color_continuous_scale=px.colors.sequential.PuRd)

# Tune how the geocode should display the final output map
fig.update_geos(showcountries=False, showcoastlines=True, showland=True, fitbounds="locations",visible=False)

# Include the Week wise date slider in the bottom of the map
fig["layout"].pop("updatemenus")

# Display the figure
fig.show()
