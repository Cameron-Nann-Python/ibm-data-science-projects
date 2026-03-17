import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output


airline_data =  pd.read_csv('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv', 
                            encoding = "ISO-8859-1",
                            dtype={'Div1Airport': str, 'Div1TailNum': str, 
                                   'Div2Airport': str, 'Div2TailNum': str})

# Define layout
app = dash.Dash(__name__)

# Add title and title style
title = "Airline Performance Dashboard"
title_style = {
    "textAlign" : "center",
    "color" : "#503D36",
    "font-size" : "40"
}
# Add dropdown features for year range
dropdown_style = {
    'height' : '5opx',
    'font-size' : '35'
}
year_div_style = {
    'font-size': '40'
}

# App setup
app.layout = html.Div(children=[
    # Title
    html.H1(title, style=title_style),
    # Year dropdown
    html.Div(
        [
            "Input Year: ", 
            dcc.Input(id='input-year', value='2010', type='number', style=dropdown_style), 
        ], 
        style=year_div_style
    ),
    html.Br(),
    html.Br(),
    # Add a graph component
    html.Div(dcc.Graph(id='line-plot')),
])

# Add callback decorator
@app.callback(
        Output(component_id='line-plot', component_property='figure'), 
        Input(component_id='input-year', component_property='value')
)

# Add computation to callback function
def get_graph(entered_year):

    # Selected data based on entered year
    df = airline_data[airline_data['Year'] == int(entered_year)]

    # Group data by Month and compute average arrival delay time
    line_data = df.groupby(['Month'])['ArrDelay'].mean().reset_index()

    # Implement figure
    fig = go.Figure(data=go.Scatter(
        x=line_data['Month'], 
        y=line_data['ArrDelay'],
        mode='lines',
        marker=dict(color='green')))
    fig.update_layout(title='Month vs Average Flight Delay Time',
                      xaxis_title="Month", yaxis_title="Average Flight Delay Time")
    return fig


# Run the app
if __name__ == "__main__":
    app.run()