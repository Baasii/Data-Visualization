import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go


from layouts import mapLayout, pointsLayout, goalsLayout, teamsLayout, teamMapLayout 
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


from dash.dependencies import Input, Output, State, MATCH, ALL

from app import app



@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)

def render_page_content(pathname):
    
    if pathname == "/":
        
        return mapLayout
                           
    elif pathname == "/pisteet":

        return pointsLayout
                                         
    elif pathname == "/maalit":

        return goalsLayout

    elif pathname == "/joukkue":

        return teamsLayout

    elif pathname == "/joukkue2":
        
        return teamMapLayout

    # 404
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
        ]
    )





