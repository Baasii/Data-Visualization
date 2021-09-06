# Dash components, html, and dash tables
import dash_core_components as dcc
import dash_html_components as html
import dash_table

# Import Bootstrap components
import dash_bootstrap_components as dbc

mapLayout = html.Div([
dcc.Dropdown(id="slct_team",
                        options=[
                            {"label": "FIN", "value": "FIN"},
                            {"label": "CAN", "value": "CAN"},
                            {"label": "2017", "value": 2017},
                            {"label": "2018", "value": 2018}],
                        multi=False,
                        value="CAN",
                        style={'width': "40%"}
                        ),
dcc.Graph(id='map', figure={})
])