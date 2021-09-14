import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go


from layouts import mapLayout, pointsLayout, teamsLayout
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import data

from dash.dependencies import Input, Output, State, MATCH, ALL

from app import app



@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)

def render_page_content(pathname):
    
    if pathname == "/":
        
        return 
                           
    elif pathname == "/pisteet":

        return pointsLayout                                      

    elif pathname == "/joukkue":

        return teamsLayout

    elif pathname == "/joukkue2":
        
        return mapLayout

    # 404
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
        ]
    )
##########   Player bar and scatter    ################
@app.callback(
    Output(component_id='pointsGraph', component_property='figure'),
    Input(component_id='pointsDropdown', component_property='value')
)
def update_graph(option_slctd):
   
    figPoints = px.bar(
    data.dfPoints,
        x= option_slctd,
        y="Name",
        color="Pos",
        height=900
    )
    figPoints.update_layout(yaxis={'categoryorder':'total ascending'})
    return figPoints

@app.callback(
    Output(component_id='pointsScatter', component_property='figure'),
    Input(component_id='pointsDropdown', component_property='value')
)
def update_graph(option_slctd):
   
    figScatterPoints = px.scatter(
        data.dfPoints,
        x="GP", 
        y=option_slctd,
        color="Pos",
        hover_data=["Name"]
        )
    figScatterPoints.update_layout(yaxis={'categoryorder':'total ascending'})
    return figScatterPoints

##########   Team scatter plots   ################
@app.callback(
    Output(component_id='teamScatter', component_property='figure'),
    Input(component_id='teamDropdown', component_property='value')
)
def update_graph(option_slctd):
   
    figScatterPoints = px.scatter(
        data.dfTeams,
        x="Points", 
        y=option_slctd,
        trendline="lowess",
        hover_data=["Team"]
        )
    figScatterPoints.update_layout(yaxis={'categoryorder':'total ascending'})
    return figScatterPoints

##########   Nationalities map   ################
@app.callback(
    Output(component_id='map', component_property='figure'),
    Input(component_id='team', component_property='value')
)


def update_graph(option_slctd):

    dfteamMap = data.dfteamMap[data.dfteamMap['Team'] == option_slctd]
   
    figMap = px.choropleth(
    data_frame=dfteamMap,
    locationmode='ISO-3',
    locations='Nationality',
    color='count',
    #hover_data=['Nationality'],
    #color_continuous_scale=px.colors.sequential.YlOrRd,
    #labels={'Nationality'},
    height=800,
    
    )
    return figMap

