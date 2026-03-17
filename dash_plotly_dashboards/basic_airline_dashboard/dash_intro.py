# Import Libraries
import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html

# Import Data
# Read the airline data into pandas dataframe
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})


# Randomly sample 500 data points with random_state=42
data = airline_data.sample(n=500, random_state=42)

# Pie Chart Creation
fig = px.pie(
    data,
    values='Flights',
    names='DistanceGroup',
    title='Distance Group Proportion by Flights'
)
fig.show()


# ## Create a dash application
# 
# Components to implement:
# - title of application
# - description of application
# - chart conveying proportion
# 
# Map to Dash HTML tags
# - title added using html.H1() tag
# - description added using html.P() tag
# - chart added using dcc.Graph() tag

# Instantiate a dash app
app = dash.Dash(__name__)

# Layout information

# Title information
title = 'Airline Dashboard'
title_style = {
    'textAlign': 'center',
    'color': '#503D36',
    'font-size': 40
}

# Description information
description = 'Proportion of distance group (250 mile distance interval group) by flights.'
description_style = {
    'textAlign': 'center',
    'color': '#F57241'
}

# Create the layout
app.layout = html.Div(
    children=[
        html.H1(title, style=title_style),
        html.P(description, style=description_style),
        dcc.Graph(figure=fig)
        ])

# Run the app
if __name__ == '__main__':
    app.run()
