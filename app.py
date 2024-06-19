import dash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output

# switch_lang = ""

app = Dash( __name__, 
            use_pages=True, 
            external_stylesheets=[dbc.themes.BOOTSTRAP],
            meta_tags=[{'name': 'viewport',
                        'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
           )

server = app.server

app.layout = html.Div([
    # NAVBAR ################################################
    html.Div([
        html.Div([], style={
            # 'height':"25px",
            'backgroundColor' : "#FFFFFF", #"#5B005C",
            }),
        html.Div([
            html.Img(src=app.get_asset_url("logo.png"),
                 style={
                     'marginLeft':"30%",
                     'height':"75px", #90px
                     'width':"300px",
                     }),
            html.P('校務永續發展中心',
                   style={
                    #    'display':"table-cell",
                       'marginLeft':"0px",
                       'verticalAlign':"middle",
                       'textAlign':"center",
                       'color':"#800080",
                       'fontSize':"36px",
                       'fontWeight': "bold",
                   }),
            # dcc.Dropdown(id='lang-in',
            #             options=['中漢語', 'English'],
            #             value='中漢語',
            #              clearable=False,
            #              style={
            #                  'marginLeft':"15%",
            #                  'width':"150px",
            #                  }),
            ], style={
            'height':"70px",
            'marginTop':"10px",
            'display' : "flex",
            'flexDirection': 'row',
            'backgroundColor' : "#FFFFFF", #"#800080",
            }),
        # html.Img(src=app.get_asset_url("logo.png"),
        #          style={
        #              'height':"90px",
        #              'width':"300px",
        #              }),
        ],style={
            'height':"90px",
            'backgroundColor' : "#FFFFFF",
            'marginBottom':"20px",
        }),
    
    # BODY ################################################
    # CONTAINER 1 ###########
    html.Div([
        html.Div([
            html.Div([
                dash.page_container,
                # html.P(id='lang-out'),
            ], style={
                'width':"100%",
                # 'overflow':'scroll',
                }),
        ],style={
            'width': "100%",
            'height':"1000px",
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
    'marginBottom':"5px",
    # 'marginBottom':"0",
    'height': "100px",
    'backgroundColor' : "#800080",
    }),
    
],style = {
    'backgroundColor' : "#F9F9F9",
})

##########################SUNBURST FUNCTION###############################
# @app.callback(
#     Output('lang-out', 'children'),
#     Input('lang-in', 'value')
# )
# def lang_process(value):
#     global switch_lang
#     if value=="English":
#         switch_lang = "eng"
#     else:
#         switch_lang = "jongwen"
#     return switch_lang
    # return f'{value}'

#########################################################

# server = app.server

if __name__ == '__main__':
    app.run(debug=True,
            dev_tools_ui=True # use it when there is an undetected error
            )