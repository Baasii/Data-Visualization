import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

# ---------- Import and clean data (importing csv into pandas)
# df = pd.read_csv("intro_bees.csv")
df = pd.read_csv("https://raw.githubusercontent.com/Coding-with-Adam/Dash-by-Plotly/master/Other/Dash_Introduction/intro_bees.csv")

df = df.groupby(['State', 'ANSI', 'Affected by', 'Year', 'state_code'])[['Pct of Colonies Impacted']].mean()
df.reset_index(inplace=True)
print(df[:5])

app.layout = html.Div([

    html.H1("Web Application Dashboards with Dash", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_disease",
                 options=[
                     {"label": "Disease", "value": 'Disease'},
                     {"label": "Other", "value": 'Other'},
                     {"label": "Pesticides", "value": 'Pesticides'},
                     {"label": "Varroa_mites", "value": 'Varroa_mites'},
                     {"label": "Pests_excl_Varroa", "value": 'Pests_excl_Varroa'}],
                 multi=False,
                 value='Disease',
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bee_map', figure={})

])

# Dashin peruspilarit:
# 1. Components = napit sliderit yms
# 2. Plotly Graphs = kartat, scatterbox, pylväskaaviot
# 3. Callback = yhdistää componentit ja graphit interaktiiviseksi kokonaisuudeksi


@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bee_map', component_property='figure')],
    [Input(component_id='slct_disease', component_property='value')]

    
)
# yks argumentti per input, option slctd = component_property
def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The year chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[(dff["State"] == "Idaho") | (dff["State"] == "New York") | (dff["State"] == "Wyoming")]
    dff = dff[dff["Affected by"] == option_slctd]

    fig = px.choropleth(
      data_frame=dff,
      locationmode='USA-states',
      locations='state_code', #state code tulee .csv filusta
      scope='usa',
      color='Pct of Colonies Impacted',
      hover_data=['State', 'Pct of Colonies Impacted'],
      color_continuous_scale=px.colors.sequential.YlOrRd,
      labels={'Pct of Colonies Impacted': '% of Bee Colonies'},
      template='plotly_dark'
    )

    fig = px.bar(
        data_frame=dff,
        x='State',
        y='Pct of Colonies Impacted')

    fig = px.line(
        data_frame=dff,
        x="Year",
        y="Pct of Colonies Impacted",
        color='State'
        
    )

    return container, fig #Returnaa @app.callbackin outputtiin


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)
