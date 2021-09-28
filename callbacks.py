from pandas.core.frame import DataFrame
import plotly.express as px  

from layouts import teamCountryLayout, pointsLayout, teamsLayout
import dash_html_components as html
import dash_bootstrap_components as dbc
import data
from PIL import Image
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
        
        return teamCountryLayout

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
        data.dfTeams20_21,
        x="Points", 
        y=option_slctd,
        z=option_slctd2,
        height=700,
        hover_data=["Team"]
        )
    
    return figScatterPoints


##########   Team GF% scatter ################
@app.callback(
    Output(component_id='teamGFScatter', component_property='figure'),
    Input(component_id='slider', component_property='value'),
    
)
def update_graph(option_slctd):
    dfGF = data.dfTeams20_21
    if option_slctd == 2016:
        dfGF = data.dfTeams16_17
    elif option_slctd == 2017:
        dfGF = data.dfTeams17_18
    elif option_slctd == 2018:
        dfGF = data.dfTeams18_19
    elif option_slctd == 2019:
        dfGF = data.dfTeams19_20
    elif option_slctd == 2020_2021:
        dfGF = data.dfTeams20_21

    figGFScatter = px.scatter(
        dfGF,
        x="GF%", 
        y="xGF%",
        #width=1000,
        height=700,
        hover_data=["Team"]
        )
    
    figGFScatter.add_shape(type="line",
    x0=50, y0=36, x1=50, y1=64,
        line=dict(
            color="LightSeaGreen",
            width=1,
        )
    )
    figGFScatter.add_shape(type="line",
    x0=36, y0=50, x1=64, y1=50,
        line=dict(
            color="LightSeaGreen",
            width=1,
        )
    )
    figGFScatter.add_annotation(
            x=39, y=40,
            text="Huono",
            showarrow=False,
    )
    figGFScatter.add_annotation(
            x=61, y=60,
            text="Hyvä",
            showarrow=False,
    )
    figGFScatter.add_annotation(
            x=39, y=60,
            text="Alisuorittaja",
            showarrow=False,
    )
    figGFScatter.add_annotation(
            x=61, y=40,
            text="Ylisuorittaja",
            showarrow=False,
    )
    figGFScatter.update_traces(marker_color="rgba(0,0,0,0)")

    for i, row in dfGF.iterrows():
        team = row['Team'].replace(" ", "-")
        figGFScatter.add_layout_image(
            dict(
                source=Image.open(f"images/{team}.png"),
                xref="x",
                yref="y",
                xanchor="center",
                yanchor="middle",
                x=row["GF%"],
                y=row["xGF%"],
                sizex=2,
                sizey=2,
                sizing="contain",
                opacity=1,
                layer="above"
            )
        )
    return figGFScatter


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

