from dash import Dash, html, page_container
import dash_bootstrap_components as dbc

app = Dash(__name__,
           use_pages=True, 
           external_stylesheets=[dbc.themes.BOOTSTRAP],
            meta_tags=[{'name': 'viewport',
                        'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
            )

app.layout = html.Div([
    dbc.Row([
        dbc.Col(html.Div([
                        html.Img(src=app.get_asset_url("logo.png"),
                                style={
                                    'marginTop':"5px",
                                    'marginLeft':"5px",
                                    'height':"70px", 
                                    'width':"70px",#"230px",
                                    }),
                        
                        html.P('校務永續發展中心',
                                            style={
                                                'marginTop':"5px",
                                                'marginLeft':"10px",
                                                'height':"70px", 
                                                'color':"#800080",
                                                'fontSize':"36px",
                                                'fontWeight': "bold",
                                            }),
                        
                        ],style={'backgroundColor':'white',
                                 'display':'flex'
                                 }), 
                ),
        ],
        className="g-0",
        justify='first',
        style={
            'backgroundColor':'white',
                            }),
    
    dbc.Row(dbc.Col(html.Div([html.Div([page_container,],style={
                                            'overflowY':"scroll",
                                            'margin':'20px 20px 20px 20px',
                                            'height':'1000px',
                                            'backgroundColor':'white',
                                        })],
            style={
                'backgroundColor':'#F9F9F9',
                }))),
    
    dbc.Row(dbc.Col(html.Footer([html.P('國立臺北商業大學校務研究中心', 
                                        style={
                                                'color':'white',
                                                'textAlign' : "center",}),
                                 html.P('校址：100 臺北市中正區濟南路一段321號　 總機：(02)3322-2777', 
                                        style={
                                            'color':'white',
                                            'textAlign' : "center",
                                            })],
                                style={
                                    'height':'100px',
                                    'backgroundColor':'purple',
                                }))),

],style = {
    'width':'100%',
    'backgroundColor' : "#F9F9F9",
})
######################################################################
if __name__ == '__main__':
    app.run(debug=False)
