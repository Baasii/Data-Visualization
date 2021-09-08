# Dash components, html, and dash tables
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px  
import data
# Import Bootstrap components
import dash_bootstrap_components as dbc

figPoints = px.bar(
        data.dfPoints,
        color="Pos",
        x="P",
        y="Name",
        height=900
    )
figPoints.update_layout(yaxis={'categoryorder':'total descending'})

figTeam3 =px.scatter(
        data.dfTeams,
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
        text="Underperforming",
        showarrow=False,
        align="left"
)
figTeam3.add_annotation(
        x=61, y=40,
        text="Overperforming",
        showarrow=False,
        align="left"
)
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

mapLayout = html.Div([
    dcc.Dropdown(id='team',
                    options=[
                        {"label": "FIN", "value": "FIN"},
                        {"label": "CAN", "value": "CAN"},
                        {"label": "USA", "value": "USA"},
                        {"label": "SWE", "value": "SWE"}],
                    multi=False,
                    value="FIN",
                    style={'width': "40%"}
                    ),
    dcc.Graph(id='map', figure={})
])

pointsLayout = html.Div([
     html.H1('Top 50 players in points',
                        style={'textAlign':'center'}),

                dcc.Graph(figure=figPoints),


                dcc.Graph(id='scatterPoints',
                        figure=px.scatter(
                        data.dfPoints,
                        x="GP", 
                        y="P",
                        color="Pos",
                        hover_data=["Name"],)),
])

goalsLayout = html.Div([
     html.H1('Top 50 goal scorers',
                        style={'textAlign':'center'}),

                dcc.Graph(id='bargraph',
                        figure=px.bar(
                        data.dfGoals,
                        color="Pos",
                        x="G",
                        y="Name",
                        height=900)),

                dcc.Graph(id='scatterGoals',
                        figure=px.scatter(
                            data.dfGoals,
                            x="GP", 
                            y="G",
                            color="Pos",
                            hover_data=["Name"]))
])

teamsLayout = html.Div([
     html.H1('TEAM 1',
                        style={'textAlign':'center'}),

                dcc.Graph(id='scatterTeam',
                        figure=px.scatter(
                            data.dfTeams,
                            x="Points", 
                            y="SF",
                            trendline="lowess",
                            hover_data=["Team"])),

                dcc.Graph(id='scatterTeam2',
                        figure=px.scatter(
                            data.dfTeams,
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
])
teamMapLayout = html.Div([
     html.H1('NHL players by nationality',
                style={'textAlign':'center'}),
                # https://gist.github.com/roblivian/7623180?short_path=6c39835
                # http://rstudio-pubs-static.s3.amazonaws.com/257443_6639015f2f144de7af35ce4615902dfd.html

    dcc.Graph(figure=figMap),
])