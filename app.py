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
)

app.layout = html.Div([
    # NAVBAR
    navbar,
    
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ],style = {
    'backgroundColor' : "#FFFFFF",
    'height':"300px",
    'margin':"20px",
    # 'paddingBottom':"20px",
}),
    
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ],style = {
    'backgroundColor' : "#FFFFFF",
    'height':"300px",
    'margin':"20px",
    # 'paddingTop':"20px",
    # 'paddingBottom':"20px",
}),
    
    html.Div([
        html.P('Dash converts Python classes into HTML'),
        html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ],style = {
    'backgroundColor' : "#FFFFFF",
    'height':"300px",
    'margin':"20px",
    # 'paddingTop':"20px",
    # 'paddingBottom':"20px",
}),
    
    # FOOTER
    html.Footer([
        html.Div([
            html.P('國立臺北商業大學校務研究中心', 
                   style = {
                       'color':"white",
                       }),
            html.P('校址：100 臺北市中正區濟南路一段321號　 總機：(02)3322-2777',
                   style = {
                       'color':"white",
                       }),
        ], style = {
        'backgroundColor' : "#800080",
        })
], style = {
    'textAlign' : "center",
    'bottom':"0px"
    }),
    
    
],style = {
    # 'backgroundColor' : "#F9F9F9",
    'backgroundColor' : "grey",
    'height':"1000px"
})

if __name__ == '__main__':
    app.run(debug=True)