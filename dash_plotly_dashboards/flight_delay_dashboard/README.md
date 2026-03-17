## Flight Delay Dashboard

![Flight Delay Desktop Dashboard](https://github.com/Cameron-Nann-Python/ibm-data-science-projects/blob/main/dash_plotly_dashboards/flight_delay_dashboard/screenshots/flight_delay_desktop.png)

## Overview
This interactive dashboard observes flight delay statistics for U.S. flights. Five graphs will be implemented for:
- average carrier delay time
- average weather delay time
- average national delay time
- average security delay time
- average late aircraft delay time
All five graph outputs respond to a year dropdown input for the dates when the flight data was collected.

## Features

### App Layout
The app will utilize dash bootstrap components to structure the layout for mobile and desktop users:
- First Row: dashboard title
- Second Row: year dropdown
- Third Row:
  - Left Column: average carrier delay and average national delay graphs
  - Right Column: average weather delay and average security delay graphs
- Fourth Row: average late aircraft delay graphs

### compute_info() function
This function slices the data frame and computes averages for each flight delay statistic. New data frames are returned for visualization.

### Callback function
The callback decorator takes the five graphs as outputs and year dropdown as the input. The callback function `get_graph()` takes the data frames from the `compute_info()` function and passes them to plotly express graph functions.

## Mobile Layout
The following is an example of the mobile implementation:
![Flight Delay Mobile](https://github.com/Cameron-Nann-Python/ibm-data-science-projects/blob/main/dash_plotly_dashboards/flight_delay_dashboard/screenshots/flight_delay_mobile.png)

## Required Technologies
- Python 3.13
  
## Import Required Libraries
- Install required libraries with the following command:
```
pip install -r requirements.txt
```

## Run the App
Open the dashboard on a local server with the following command:
```
python app.py
```

## Files Included
- `flight_delay.py`: Python file containing Dash app and IBM dataset.
- `requirements.txt`: Required Python librariers.
- `flight_delay_desktop.png`: Dash app on desktop.
- `flight_delay_mobile.png`: Dash app for mobile users.
