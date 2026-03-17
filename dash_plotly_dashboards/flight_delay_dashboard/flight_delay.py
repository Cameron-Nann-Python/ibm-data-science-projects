import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Import Data from IBM
airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Instantiate dash app
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[{'name':'viewport', 'content': 'width=device-width, initial-scale=1.0'}]
    )

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            # Title
            html.H1('Flight Delay Time Statistics',
                    style={'textAlign' : 'center',
                            'color': '#0000FF'}),
        ], width=12)
    ]),
    dbc.Row([
        dbc.Col([
            # Year Toggle
            "Input Year: ",
            dcc.Dropdown(
                id='input-year',
                value=2010,
                options=[{'label':x, 'value':x} for x in sorted(airline_data['Year'].unique())]),
        ], xs=12, sm=12, md=12, lg=11, xl=11),
    ]),
    dbc.Row([
        dbc.Col([
            # Carrier Graph
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='carrier-plot', figure={})
                ])
            ], class_name='mb-4'),

            # National airline graph
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='nas-plot', figure={})
                ])
            ], class_name='mb-4')
        ], xs=12, sm=6, md=6, lg=5, xl=5),

        dbc.Col([
            # Weather Graph
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='weather-plot', figure={})
                ])
            ], class_name='mb-4'),

            # Security graph
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='security-plot', figure={})
                ])
            ], class_name='mb-4')
        ], xs=12, sm=6, md=6, lg={'size':5, 'offset':1}, xl={'size':5, 'offset':1})
    ]),

    dbc.Row([
        dbc.Col([
            # Late carrier graph
            dbc.Card([
                dbc.CardBody([
                    dcc.Graph(id='late-plot', figure={})
                ])
            ], class_name='mb-4')
        ], xs=12, sm=10, md=10, lg=8, xl=8)
    ])
], fluid=True)

def compute_info(airline_data, entered_year):
    """ 
    Returns averages for flight delay data for graphical computation.
        Parameters:
            airline_data (pd.DataFrame): input airline data
            entered_year (int): input year for computation
        Returns:
            computed average dataframes for carrier, 
            weather, national, security, and late instances.
    """
    # Select data
    df =  airline_data[airline_data['Year']==int(entered_year)]

    # Compute delay averages
    avg_car = df.groupby(['Month','Reporting_Airline'])['CarrierDelay'].mean().reset_index()
    avg_weather = df.groupby(['Month','Reporting_Airline'])['WeatherDelay'].mean().reset_index()
    avg_NAS = df.groupby(['Month','Reporting_Airline'])['NASDelay'].mean().reset_index()
    avg_sec = df.groupby(['Month','Reporting_Airline'])['SecurityDelay'].mean().reset_index()
    avg_late = df.groupby(['Month','Reporting_Airline'])['LateAircraftDelay'].mean().reset_index()

    # Return dataframes
    return avg_car, avg_weather, avg_NAS, avg_sec, avg_late

# Add callback for interactivity
@app.callback(
    [
     Output(component_id='carrier-plot', component_property='figure'),
     Output(component_id='weather-plot', component_property='figure'),
     Output(component_id='nas-plot', component_property='figure'),
     Output(component_id='security-plot', component_property='figure'),
     Output(component_id='late-plot', component_property='figure')
     ], 
    Input(component_id='input-year', component_property='value')
)

# Add callback graph to change
def get_graph(entered_year):

    # Get average dataframes for graphs
    avg_car, avg_weather, avg_NAS, avg_sec, avg_late = compute_info(airline_data, entered_year)

    # Line plot for carrier delay
    carrier_fig = px.line(avg_car, x='Month', y='CarrierDelay', color='Reporting_Airline', 
                          title='Average Carrier Delay Time (Minutes) by Airline')

    # Line plot for weather delay
    weather_fig = px.line(avg_weather, x='Month', y='WeatherDelay', color='Reporting_Airline',
                          title='Average Weather Delay Time (Minutes) by Airline')

    # Line plot for nas delay
    nas_fig = px.line(avg_NAS, x='Month', y='NASDelay', color='Reporting_Airline',
                      title='Average National Delay (Minutes) by Airline')

    # Line plot for security delay
    sec_fig = px.line(avg_sec, x='Month', y='SecurityDelay', color='Reporting_Airline',
                      title='Average Security Delay (Minutes) by Airline')

    # Line plot for late aircraft delay
    late_fig = px.line(avg_late, x='Month', y='LateAircraftDelay', color='Reporting_Airline',
                       title='Average Late Aircraft Delay (Minutes) by Airline')

    return[carrier_fig, weather_fig, nas_fig, sec_fig, late_fig]

# Run app
if __name__ == '__main__':
    app.run()