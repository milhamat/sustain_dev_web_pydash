import dash
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import callback, dcc, html, Input, Output

dash.register_page(__name__, path='/')

layout = html.Div([
    html.Div([
                dbc.Tabs(id="tabs",
                children=[
                    dbc.Tab(label="Student", tab_id="stdent"),
                    dbc.Tab(label="Faculty", tab_id="facult"),
                    dbc.Tab(label="School Affair", tab_id="schafr")
                ],
                active_tab="stdent",
                ## dont know it's work or not
                style={
                    'color':"purple",
                }),
                html.Div(id='tab-Out'),
            ], style={
                    'width': "100%",
             }),
])

@callback(Output('tab-Out','children'),
              Input('tabs','active_tab'))

def render_content(tab):
    ##############################STUDENT################
    if tab == 'stdent':
        return html.Div([
            html.Div([
                # container row one
                html.Div([
                    ###### Container 1
                    html.Div([
                        html.Div([
                            html.H1('學年學生分佈', # Student Distribution for Academic Year 
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
                                    }), href="/student/sunburst", refresh=True,),
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
                ###### Container 2
                    html.Div([
                        html.Div([
                            html.H1('Sankey Enrollment', # Student Distribution for Academic Year 
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
                                    }), href="/student/sankey", refresh=True,),
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
                ##########
                ###### Container 3
                    html.Div([
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
                    ##########
                    ###### Container 4
                    html.Div([
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
                        ],style={
                            'display' : "flex",
                            }),
                
                ##########
                ################################################################
                # container row one
                html.Div([
                    ###### Container 5
                html.Div([
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
                ##########
                    
                ], style={
                    'display' : "flex"
                })
                
                
        ], style={
            # 'display' : "flex",
            }),
        ]),
        ##############################FACULTY################
    elif tab == "facult":
        return html.Div([
            html.Div([
                html.Div([
                    html.H1('FACULTY', # Student Distribution for Academic Year 
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
                             }), href="/sunburst", refresh=True,),
                    ], style={
                        # 'width':"350px",
                        # 'borderWidth': "thin",
                        # 'borderStyle':"solid",
                        # 'borderColor':"#C6C4C4",
                        }),
                
            ], style={
                'backgroundColor':"white",
                'height':"180px",
                'width':"350px",
                'marginTop':"40px",
                'marginLeft':"20px",
                'borderRadius':"8px",
                'borderWidth': "thin",
                'borderStyle':"solid",
                'borderColor':"#C6C4C4",
            })
        ])
    ##############################SCHOOL AFFAIR################
    elif tab == "schafr":
        return html.Div([
            html.Div([
                html.Div([
                    html.H1('STUDENT', # Student Distribution for Academic Year 
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
                             }), href="/sunburst", refresh=True,),
                    ], style={
                        # 'width':"350px",
                        # 'borderWidth': "thin",
                        # 'borderStyle':"solid",
                        # 'borderColor':"#C6C4C4",
                        }),
                
            ], style={
                'backgroundColor':"white",
                'height':"180px",
                'width':"350px",
                'marginTop':"40px",
                'marginLeft':"20px",
                'borderRadius':"8px",
                'borderWidth': "thin",
                'borderStyle':"solid",
                'borderColor':"#C6C4C4",
            })
        ])