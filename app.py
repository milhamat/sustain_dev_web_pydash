# https://dash.plotly.com/tutorial
from dash import Dash, html
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# make a reuseable navitem for the different examples
# nav_item = dbc.NavItem(dbc.NavLink("Link", href="#"))

# make a reuseable dropdown for the different examples
# dropdown = dbc.DropdownMenu(
#     children=[
#         dbc.DropdownMenuItem("Entry 1"),
#         dbc.DropdownMenuItem("Entry 2"),
#         dbc.DropdownMenuItem(divider=True),
#         dbc.DropdownMenuItem("Entry 3"),
#     ],
#     nav=True,
#     in_navbar=True,
#     label="Menu",
# )

# navbar = dbc.Navbar(
#     dbc.Container(
#         [
#             html.A(
#                 # Use row and col to control vertical alignment of logo / brand
#                 dbc.Row(
#                     [
#                         # dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
#                         dbc.Col(dbc.NavbarBrand("校務永續發展中心", className="ms-2")),
#                     ],
#                     align="center",
#                     className="g-0",
#                 ),
#                 # href="https://plotly.com",
#                 style={"textDecoration": "none"},
#             ),
#             dbc.NavbarToggler(id="navbar-toggler2", n_clicks=0),
#             dbc.Collapse(
#                 dbc.Nav(
#                     # [nav_item, dropdown],
#                     className="ms-auto",
#                     navbar=True,
#                 ),
#                 id="navbar-collapse2",
#                 navbar=True,
#             ),
#         ],
#     ),
#     color="#800080",
#     dark=True,
#     className="mb-5",
#     height="50px"
# )

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
    # html.H1('Hello Dash', style = {
    #     'paddingLeft' : "20px",
    # }),
    
    # html.Div([
    #     html.Img(src=app.get_asset_url('logo.png'), style = {
    #     'height' : "50px",
    #     # 'width' : "80px",
    #     'paddingLeft' : "20px",
    #     })
    # ], style={
    #     'paddingTop' : "0px"
    #     }),
    
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