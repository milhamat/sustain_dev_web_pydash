# https://dash.plotly.com/tutorial
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

PLOTLY_LOGO = "./assets/logo.png"

navbar = dbc.Navbar(
    dbc.Container(
        [   
         dbc.Row(
            [
                dbc.Col(html.Img(src=PLOTLY_LOGO, height="60px")),
                dbc.Col(dbc.NavbarBrand("校務永續發展中心", className="ms-2")),
            ],
            align="center",
            className="g-0",
         ),
        ],
    ),
    color="#800080",
    dark=True,
    className="mb-5",
    # height="50px"
)

app.layout = html.Div([
    navbar,
    
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ],style = {
    'backgroundColor' : "#FFFFFF"
})
],style = {
    'backgroundColor' : "#F9F9F9",
})

if __name__ == '__main__':
    app.run(debug=True)