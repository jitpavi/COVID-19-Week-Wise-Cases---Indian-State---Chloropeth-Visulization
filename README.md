# Project Name - COVID-19-Week-Wise-Cases---Indian-State--Chloropeth-Visualisation

#### -- Project Status: [Active]
In process of adding the data reported from the district level of each respective States of India.

## Project Intro/Objective:
This project will produce the chloropeth map to visualize the number of cases reported in each state of India starting from Week 10 of the year 2020. In the map there will be Week-wise Slider through which you can visualise the weekly status of each respective States and how much badly are they affected by the Covid-19 crisis.

### Methods Used:
* Data Exploration
* Data Wrangling
* Data Visualization

### Technologies Used:
* Python
* Pandas
* Pycharm
* Plotly Express
* Chloropeth visualisation

## Project Description:

### Prerequisites
  ### -> Dataset:
  * API for accessing data from the Central website hosting all the data related to Covid-19 cases in each state of India (https://api.covid19india.org/csv/latest/state_wise_daily.csv)
  
  ### -> Python Libraries:
  * Pandas
  * Plotly Express
  * Requests
  * Dateutil
  
### Workflow:
1. Using the API call create a new dataframe and filter with those cases which are being Confirmed.
2. Inorder to acheive the output we need three columns namely Date detected, State Name and Cases Confirmed.
3. Information received through API has columns State codes mentioned in the form of columns which needs to be converted into rows for each respective dates.
4. Create a new List of Tuples which out of the original Dataframe which will contains the values above 3 columns.
5. Using the Tuples we create a master Dataframe which will be used to build the output.
6. Parse the Date columns into Datetime object and convert the format into "Year-Week" type.
7. Create a new  ISO Code Dataframe holding the columns of State code and State name.
8. Perform Data Wrangling on the ISO code dataframe and sorted the column name "Code"
9. Iterate through the rows of ISO Code dataframe and create a Dictionary object to hold the mappings of Code names with State Names.
10.Access the open source geocode Json object and save it in a JSON object variable.
11.Create a fig object which will have all the required data to be displayed in the output.
12.Update the geocode property of the Figure object to make the output data more presentabe.
13. Display the data and move the week slider in the bottom to observer the cases in each states.

## Expected Output:
As you can observe here, for every week starting from week 10 each state of India diplays the number of cases reported.
For better understanding you can hover your mouse pointer over each state and see the figures.

 ![Chloropeth Map - COVID-19 Cases in India](https://github.com/jitpavi/COVID-19-Week-Wise-Cases---Indian-State--Chloropeth-Visualisation/blob/master/Chloropeth%20Map%20-%20COVID-19%20Cases%20in%20India.JPG)

## Featured Notebooks/Analysis/Deliverables
* [COVID-19-Week-Wise-Cases---Indian-State--Chloropeth-Visualisationv1.0.py](https://github.com/jitpavi/COVID-19-Week-Wise-Cases---Indian-State--Chloropeth-Visualisation/blob/master/COVID-19-Week-Wise-Cases---Indian-State--Chloropeth-Visualisation%20v1.0.py)

## Versioning
Code version - v1.0

## Author:

* **Jitin Pavithran** - [jitpavi](https://github.com/jitpavi)

## Acknowledgments:

* https://api.covid19india.org/csv/latest/state_wise_daily.csv
*	https://raw.githubusercontent.com/Subhash9325/GeoJson-Data-of-Indian-States/master/Indian_States


## References:

* https://towardsdatascience.com/interactive-covid-19-visualizations-using-plotly-with-4-lines-of-code-fa33b334ab84
