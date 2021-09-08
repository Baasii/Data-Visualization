import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go


import dash  
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import data

from dash.dependencies import Input, Output

from app import app
from layouts import mapLayout
from callbacks import *




SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}


CONTENT_STYLE = {
    "marginLeft": "10%",
    "marginRight": "10%",
    "padding": "2rem 1rem",
}

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Koti", href="/")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Pelaajat", header=True),
                dbc.DropdownMenuItem("Pisteet", href="/pisteet"),
                dbc.DropdownMenuItem("Maalit", href="/maalit"),
            ],
            nav=True,
            in_navbar=True,
            label="Pelaajat",
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Joukkueet", header=True),
                dbc.DropdownMenuItem("Joukkuetilastot", href="/joukkue"),
                dbc.DropdownMenuItem("Kotimaat", href="/joukkue2"),
            ],
            nav=True,
            in_navbar=True,
            label="Joukkueet",
        ),
    ],
    brand="Tilastot",
    brand_href="#",
    color="primary",
    dark=True,
)


content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    navbar,
    content
])
# ,mapLayout
@app.callback(
    Output(component_id='map', component_property='figure'),
    Input(component_id='team', component_property='value')
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


    



if __name__ == '__main__':
    app.run_server(debug=True)
