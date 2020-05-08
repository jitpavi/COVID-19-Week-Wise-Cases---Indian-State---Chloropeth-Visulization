# Project Name - COVID-19-Week-Wise-Cases---Indian-State--Chloropeth-Visualisation

#### -- Project Status: [Active]
In process of adding the data reported from the district level of each respective States of India.

## Project Intro/Objective:
This project will produce the chloropeth map to visualize the number of cases reported in each state of India starting from Week 10 of the year 2020.

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
1. Using request module download the data using the API call from the website hosting the required data.
2. Convert the response data into JSON obejct.
3. Create a Dataframe using Pandas from the JSON object.
4. Replace the index column with the Date column name "date".
5. Create a fig object where we are going to plot the chart and pass it as an input to the animator function.
6. Define a Buildchart function which will be called for every frame in plotting the chart by the FuncAnimation.
7. Create an Animator object with inputs as fig,buildchart function and interval of 30ms.
8. Save the animator object in the form of GIF format file.

## Expected Output:
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
