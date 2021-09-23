import plotly.express as px  

from layouts import teamLayout, pointsLayout, teamsLayout
import dash_html_components as html
import dash_bootstrap_components as dbc
import data

from dash.dependencies import Input, Output

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
        
        return teamLayout

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
    Input(component_id='teamDropdownX', component_property='value'),
    Input(component_id='teamDropdownY', component_property='value')
)
def update_graph(option_slctd, option_slctd2):
   
    figScatterPoints = px.scatter_3d(
        data.dfTeams,
        x="Points", 
        y=option_slctd,
        z=option_slctd2,
        height=700,
        hover_data=["Team"]
        )
    return figScatterPoints

##########   Nationalities  choroplethmap   ################
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
    height=800,
    
    )
    return figMap

##########   Nationalities piechart   ################

@app.callback(
    Output(component_id='pie', component_property='figure'),
    Input(component_id='team', component_property='value')
)


def update_graph(option_slctd):

    dfteamMap = data.dfteamMap[data.dfteamMap['Team'] == option_slctd]
   
    figPie = px.pie(
    data_frame=dfteamMap,
    values='count',
    names='Nationality',
    
    )
    figPie.update_traces(textposition='inside', textinfo='percent+label')
    return figPie

