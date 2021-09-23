
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc




from app import app
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



    



if __name__ == '__main__':
    app.run_server(debug=True)
