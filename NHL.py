import pandas as pd
import plotly.express as px  
import plotly.graph_objects as go


import dash  
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc


from dash.dependencies import Input, Output




app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


#dfcities = pd.read_csv("Cities.csv", sep=";", usecols=[2,19])   # Lähteenä https://github.com/drei01/geojson-world-cities
dfplayercities = pd.read_csv("PlayerCities.csv", sep=",", usecols=[9])

dfplayercities = dfplayercities.groupby(['Nationality']).size().reset_index(name='count')
print(dfplayercities)

#def dataframe_difference(df1, df2, which):
   # """Find rows which are different between two DataFrames."""
 #   comparison_df = df1.merge(
  #      df2,
   #     indicator=True,
    #    how='outer'
    #)
    #if which is None:
     #   diff_df = comparison_df[comparison_df['_merge'] != 'both']
    #else:
    #    diff_df = comparison_df[comparison_df['_merge'] == which]
    #diff_df[['lat','lon']] = diff_df['Coordinates'].str.split(',',expand=True)
    #diff_df.to_csv('diff.csv')
    #print(diff_df)
    #return diff_df

#dataframe_difference(dfcities, dfplayercities, which='both')



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
    "margin-left": "10%",
    "margin-right": "10%",
    "padding": "2rem 1rem",
}

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Players", header=True),
                dbc.DropdownMenuItem("Top point scorers", href="/page-1"),
                dbc.DropdownMenuItem("Top goal scorers", href="/page-2"),
            ],
            nav=True,
            in_navbar=True,
            label="Players",
        ),
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Teams", header=True),
                dbc.DropdownMenuItem("Page 2", href="/page-3"),
                dbc.DropdownMenuItem("Page 3", href="/page-4"),
            ],
            nav=True,
            in_navbar=True,
            label="Teams",
        ),
    ],
    brand="Stats",
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

@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)

def render_page_content(pathname):
    dfPoints = pd.read_csv("Points.csv", nrows=50, sep=";")
    dfGoals = pd.read_csv("Goals.csv", nrows=50, sep=";")
    dfTeams = pd.read_csv("2020-2021Team.csv", nrows=50, sep=",")

    
    figPoints = px.bar(
        dfPoints,
        color="Pos",
        x="P",
        y="Name",
        height=900
    )
    figPoints.update_layout(yaxis={'categoryorder':'total descending'})

    figTeam3 =px.scatter(
        dfTeams,
        x="GF%", 
        y="xGF%",
        hover_data=["Team"],
        width=800,
        height=600,
        
        
    )

    figTeam3.add_shape(type="line",
    x0=50, y0=38, x1=50, y1=62,
        line=dict(
            color="LightSeaGreen",
            width=1,
        )
    )
    figTeam3.add_shape(type="line",
    x0=38, y0=50, x1=62, y1=50,
        line=dict(
            color="LightSeaGreen",
            width=1,
        )
    )
    figTeam3.add_annotation(
            x=39, y=40,
            text="Bad",
            showarrow=False,
            align="left"
    )
    figTeam3.add_annotation(
            x=61, y=60,
            text="Good",
            showarrow=False,
            align="left"
    )
    figTeam3.add_annotation(
            x=39, y=60,
            text="Overperforming",
            showarrow=False,
            align="left"
    )
    figTeam3.add_annotation(
            x=61, y=40,
            text="Underperforming",
            showarrow=False,
            align="left"
    )

    #cities = pd.read_csv("diff.csv")


    #figMap = px.scatter_mapbox(cities, 
    #lat="lat", 
    #lon="lon",  
    #color_discrete_sequence=["fuchsia"], 
    #zoom=3, 
    #height=300)


    #figMap.update_layout(mapbox_style="open-street-map")
    #figMap.update_layout(margin={"r":0,"t":0,"l":0,"b":0})

    figMap2 = px.choropleth(
        data_frame=dfplayercities,
        locationmode='ISO-3',
        locations='Nationality',
        color='count',
        hover_data=['Nationality'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Nationality'},
        
    )



    if pathname == "/":
        return [
                
                
                ]
    
    elif pathname == "/page-1":
        return [
                
                html.H1('Top 50 players in points',
                        style={'textAlign':'center'}),

                dcc.Graph(figure=figPoints),


                dcc.Graph(id='scatterPoints',
                        figure=px.scatter(
                        dfPoints,
                        x="GP", 
                        y="P",
                        color="Pos",
                        hover_data=["Name"],)),
                
                
                            
             ]
    elif pathname == "/page-2":
        return [
                html.H1('Top 50 goal scorers',
                        style={'textAlign':'center'}),

                dcc.Graph(id='bargraph',
                        figure=px.bar(
                        dfGoals,
                        color="Pos",
                        x="G",
                        y="Name",
                        height=900)),

                dcc.Graph(id='scatterGoals',
                         figure=px.scatter(
                            dfGoals,
                            x="GP", 
                            y="G",
                            color="Pos",
                            hover_data=["Name"]))
                
                
                ]
    elif pathname == "/page-3":
        return [
                html.H1('TEAM 1',
                        style={'textAlign':'center'}),

                dcc.Graph(id='scatterTeam',
                         figure=px.scatter(
                            dfTeams,
                            x="Points", 
                            y="SF",
                            trendline="lowess",
                            hover_data=["Team"])),

                dcc.Graph(id='scatterTeam2',
                         figure=px.scatter(
                            dfTeams,
                            x="Points", 
                            y="SA",
                            trendline="lowess",
                            hover_data=["Team"])),

                dcc.Graph(figure=figTeam3),
                html.H1('ONKO VÄÄRIN ^ ?',
                        style={'textAlign':'center'}),


                html.H4('A team’s GF% is their goals-for percentage, representing their share of all goals scored at even-strength. If a team scores three goals and gives up two goals against, they have a goal-for percentage of 60%.But corsica also calculates each team’s expected goals-for percentage, which is the same as above but considers only xG and not actual goals. A team might generate 2.75 xG in a game and surrender 2.25 xG against, giving them an xGF% of 55%.This graph compares actual GF% (reality) and xGF% (expectation) to see how a team is performing relative to what we’d expect.'
                )
                            
                # KIRJOTA ETTÄ KUVIA EI VOI LISÄTÄ PISTEIDEN TILALLE
                
                ]
    elif pathname == "/page-4":
        return [
                html.H1('NHL players by nationality',
                        style={'textAlign':'center'}),
                        # https://gist.github.com/roblivian/7623180?short_path=6c39835
                        # http://rstudio-pubs-static.s3.amazonaws.com/257443_6639015f2f144de7af35ce4615902dfd.html
                
                dcc.Graph(figure=figMap2),
                
                ]
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )
    



####app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.RadioItems(id="slct_stat",
                 options=[
                     {"label": "Top 50 in Goals", "value": "G"},
                     {"label": "Top 50 in Points", "value": "P"}],
                 value="G",
                 style={'width': "40%"}
                 ),
    

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='Scatter', figure={}),
    html.Br(),
    html.Br(),
    dcc.Graph(id='PointsBar', figure={}),
####])

# Dashin peruspilarit:
# 1. Components = napit sliderit yms
# 2. Plotly Graphs = kartat, scatterbox, pylväskaaviot
# 3. Callback = yhdistää componentit ja graphit interaktiiviseksi kokonaisuudeksi


####@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='PointsBar', component_property='figure'),
     Output(component_id='Scatter', component_property='figure'),],
    [Input(component_id='slct_stat', component_property='value')]

    
#####)
# yks argumentti per input, option slctd = component_property
##def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)
    
    if option_slctd == "G":
        dfPoints = pd.read_csv("Goals.csv", nrows=51, sep=";")

        figScatter = px.scatter(
        dfPoints,
        x="GP", 
        y=option_slctd,
        color="Pos",
        hover_data=["Name"]
    )
    else:
        dfPoints = pd.read_csv("Points.csv", nrows=51, sep=";")

        figScatter = px.scatter(
        dfPoints,
        x="GP", 
        y="P",
        color="Pos",
        hover_data=["Name"]
    )

    print(dfPoints)
    #dfPoints = df.copy()
    
    #dfPoints = dfPoints[dfPoints["Home" | "Visitor"] == option_slctd]

    #fig = px.line(
    #   data_frame=dfPoints,
    #    x="Year",
    #    y="Home"
    #)
    figPoints = px.bar(
        data_frame=dfPoints,
        color="Pos",
        x=option_slctd,
        y="Name",
        height=900,

    )
    figPoints.update_layout(yaxis={'categoryorder':'total descending'})
    return container, figPoints, figScatter #Returnaa @app.callbackin outputtiin

    

# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
