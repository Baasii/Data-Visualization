import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go


import dash  
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


from dash.dependencies import Input, Output

from app import app

import data

@app.callback(
    [Output(component_id='map', component_property='figure')],
    [Input(component_id='slct_team', component_property='value')]
)

def update_graph(option_slctd):
    data.dfplayercities = data.dfplayercities[data.dfplayercities['Nationality'] == option_slctd]

    figMap = px.choropleth(
    data_frame=data.dfplayercities,
    locationmode='ISO-3',
    locations='Nationality',
    color='count',
    hover_data=['Nationality'],
    color_continuous_scale=px.colors.sequential.YlOrRd,
    labels={'Nationality'},
    height=800,
    
    )
    return figMap

