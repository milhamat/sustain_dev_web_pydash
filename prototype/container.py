from dash import dcc, html  
  
def placeholder():
    return html.Div([
                        html.Div([
                            html.H1('Total student internship hours', # Student Distribution for Academic Year 
                                style={
                                    # 'textAlign':"center",
                                    'fontSize':"28px",
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("Detail", 
                                            style={
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                #  'marginTop':"5px",
                                                'marginLeft':"80%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/stdintern", refresh=True,),
                                    # }), href="/stdBarchart", refresh=True,),
                            ], style={
                                }),
                    
                ], style={
                    'backgroundColor':"white",
                    'height':"180px",
                    'width':"350px",
                    'marginTop':"40px",
                    'marginLeft':"15px",
                    'borderRadius':"8px",
                    'borderWidth': "thin",
                    'borderStyle':"solid",
                    'borderColor':"#C6C4C4",
                }),