# https://dash.plotly.com/tutorial

import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output

# df = pd.read_excel('./datas/102_111StdInfo1Acdm.xlsx')
df = pd.read_csv('./datas/sunburst.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    # NAVBAR ################################################
    html.Div([
        html.Div([], style={
            'height':"25px",
            'backgroundColor' : "#5B005C",
            }),
        html.Div([
            html.P('校務永續發展中心',
                   style={
                       'color':"white",
                       'fontSize':"40px",
                       'fontWeight': "bold",
                   })
            ], style={
            'height':"70px",
            'backgroundColor' : "#800080",
            }),
        html.Img(src=app.get_asset_url("logo.png"),
                 style={
                     'height':"90px",
                     'width':"300px",
                     }),
        ],style={
            'height':"200px",
            'backgroundColor' : "#FFFFFF",
            'marginBottom':"20px",
        }),
    
    # BODY ################################################
    #### CONTAINER 1 ###########
    html.Div([
        html.Div([
            html.Div([
                
            ]),
        ],style={
            'width': "100%",
            'height':"600px",
            'backgroundColor' : "#FFFFFF",
            'marginLeft':"20px",
            'marginRight':"20px",
            'marginBottom':"20px",
        }),
    ],style = {
    'backgroundColor' : "#F9F9F9",
    'display' : "flex",
        }),
    # FOOTER ################################################
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
    'bottom':"0",
    'marginBottom':"0",
    'height': "100px",
    'backgroundColor' : "#800080",
    }),
    
    
],style = {
    'backgroundColor' : "#F9F9F9",
})

##########################SUNBURST FUNCTION###############################

#########################################################

if __name__ == '__main__':
    app.run(debug=True,
            dev_tools_ui=False
            )