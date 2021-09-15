# Dash components, html, and dash tables
import dash_core_components as dcc
import dash_html_components as html
import dash_table
import plotly.express as px  
import data
# Import Bootstrap components
import dash_bootstrap_components as dbc

##### xGF CHART
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


teamLayout = html.Div([
    html.Div([
        html.H1('Pelaajien kotimaat joukkuettain',
                    style={'textAlign':'center'}),
        dcc.Dropdown(id='team',
                        options=[
                            {"label": "ANA", "value": "ANA"},
                            {"label": "ARI", "value": "ARI"},
                            {"label": "BOS", "value": "BOS"},
                            {"label": "BUF", "value": "BUF"},
                            {"label": "CAR", "value": "CAR"},
                            {"label": "CGY", "value": "CGY"},
                            {"label": "CBJ", "value": "CBJ"},
                            {"label": "COL", "value": "COL"},
                            {"label": "DAL", "value": "DAL"},
                            {"label": "DET", "value": "DET"},
                            {"label": "EDM", "value": "EDM"},
                            {"label": "FLA", "value": "FLA"},
                            {"label": "L.A", "value": "L.A"},
                            {"label": "MIN", "value": "MIN"},
                            {"label": "MTL", "value": "MTL"},
                            {"label": "NSH", "value": "NSH"},
                            {"label": "N.J", "value": "N.J"},
                            {"label": "NYI", "value": "NYI"},
                            {"label": "NYR", "value": "NYR"},
                            {"label": "OTT", "value": "OTT"},
                            {"label": "PHI", "value": "PHI"},
                            {"label": "PIT", "value": "PIT"},
                            {"label": "S.J", "value": "S.J"},
                            {"label": "STL", "value": "STL"},
                            {"label": "T.B", "value": "T.B"},
                            {"label": "TOR", "value": "TOR"},
                            {"label": "VAN", "value": "VAN"},
                            {"label": "VGK", "value": "VGK"},
                            {"label": "WPG", "value": "WPG"},
                            {"label": "WSH", "value": "WSH"},],
                        multi=False,
                        value="ANA",
                        style={'width': "40%"}
                        ),
        dcc.Graph(id='map', figure={}),
        
    ]),
    html.Div([
        dcc.Graph(id='pie', figure={})
    ])
])


pointsLayout = html.Div([
        html.H1('Kaikkien aikojen pistepörssin top 50',
                        style={'textAlign':'center'}),

        dcc.Dropdown(id='pointsDropdown',
                    options=[
                        {"label": "P", "value": "P"},
                        {"label": "G", "value": "G"},
                        {"label": "A", "value": "A"},
                        {"label": "PIM", "value": "PIM"},
                        {"label": "PPG", "value": "PPG"},
                        {"label": "SHG", "value": "SHG"},
                        {"label": "SHOTS", "value": "SHOTS"},],
                    multi=False,
                    value="G",
                    style={'width': "40%"}
                    ),
                dcc.Graph(id='pointsGraph', figure={}),
                dcc.Graph(id='pointsScatter', figure={}),

])

teamsLayout = html.Div([
                 html.H1('TEAM 1',
                        style={'textAlign':'center'}),
        
                dcc.Dropdown(id='teamDropdown',
                    options=[
                        {"label": "SF", "value": "SF"},
                        {"label": "SA", "value": "SA"},
                        {"label": "GF", "value": "GF"},
                        {"label": "GA", "value": "GA"},
                        {"label": "SH%", "value": "SH%"},
                        {"label": "SV%", "value": "SV%"},],
                    multi=False,
                    value="SF",
                    style={'width': "40%"}
                    ),

                dcc.Graph(id='teamScatter', figure={}),


                dcc.Graph(figure=figTeam3),
                html.H1('ONKO VÄÄRIN ^ ?  KIRJOTA ETTÄ KUVIA EI VOI LISÄTÄ PISTEIDEN TILALLE',
                        style={'textAlign':'center'}),


                html.H4('A team’s GF% is their goals-for percentage, representing their share of all goals scored at even-strength. If a team scores three goals and gives up two goals against, they have a goal-for percentage of 60%.But corsica also calculates each team’s expected goals-for percentage, which is the same as above but considers only xG and not actual goals. A team might generate 2.75 xG in a game and surrender 2.25 xG against, giving them an xGF% of 55%.This graph compares actual GF% (reality) and xGF% (expectation) to see how a team is performing relative to what we’d expect.'
                )
                            
                # KIRJOTA ETTÄ KUVIA EI VOI LISÄTÄ PISTEIDEN TILALLE
])