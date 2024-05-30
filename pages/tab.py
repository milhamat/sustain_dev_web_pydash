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
                            html.H1('Student Distribution for Academic Year', # Student Distribution for Academic Year  # 學年學生分佈
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
                                    }), href="/student/stddistbyyear", refresh=True,),
                            ], style={
                                }),
                    
                ], style={
                    'backgroundColor':"white",
                    'height':"180px",
                    'width':"350px",
                    'marginTop':"20px",
                    'marginLeft':"15px",
                    'borderRadius':"8px",
                    'borderWidth': "thin",
                    'borderStyle':"solid",
                    'borderColor':"#C6C4C4",
                }),
                ###### Container 2
                    html.Div([
                        html.Div([
                            html.H1('Entry Path, Gender, and College', 
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
                                    }), href="/student/entrypathgender", refresh=True,),
                            ], style={
                                }),
                    
                ], style={
                    'backgroundColor':"white",
                    'height':"180px",
                    'width':"350px",
                    'marginTop':"20px",
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
                            html.H1('Total Student Internship Hours', 
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
                            ], style={
                                }),
                    
                ], style={
                    'backgroundColor':"white",
                    'height':"180px",
                    'width':"350px",
                    'marginTop':"20px",
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
                            html.H1('Gender Ratio', 
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
                                    }), href="/student/stdngenderratio", refresh=True,),
                            ], style={
                                }),
                    
                ], style={
                    'backgroundColor':"white",
                    'height':"180px",
                    'width':"350px",
                    'marginTop':"20px",
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
                # container row two
                html.Div([
                    ###### Container 5
                    html.Div([
                        html.Div([
                            html.H1('Spread of Work Areas After Graduation', 
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
                                    }), href="/student/gradworkarea", refresh=True,),
                            ], style={
                                }),
                    
                ], style={
                    'backgroundColor':"white",
                    'height':"180px",
                    'width':"350px",
                    'marginTop':"20px",
                    'marginLeft':"15px",
                    'borderRadius':"8px",
                    'borderWidth': "thin",
                    'borderStyle':"solid",
                    'borderColor':"#C6C4C4",
                }),
                ##########
                    ###### Container 6
                    html.Div([
                        html.Div([
                            html.H1('Graduation Job Type', 
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
                                    }), href="/student/gradjobtype", refresh=True,),
                                    # }), href="/student/gradworkarea", refresh=True,),
                            ], style={
                                }),
                    
                ], style={
                    'backgroundColor':"white",
                    'height':"180px",
                    'width':"350px",
                    'marginTop':"20px",
                    'marginLeft':"15px",
                    'borderRadius':"8px",
                    'borderWidth': "thin",
                    'borderStyle':"solid",
                    'borderColor':"#C6C4C4",
                }),
                #########
                ###### Container 7
                    html.Div([
                        html.Div([
                            html.H1('Number of Graduate by Department and Institutes', 
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
                                    }), href="/student/numgradbydepinst", refresh=True,),
                                    # }), href="/student/gradworkarea", refresh=True,),
                            ], style={
                                }),
                    
                ], style={
                    'backgroundColor':"white",
                    'height':"180px",
                    'width':"350px",
                    'marginTop':"20px",
                    'marginLeft':"15px",
                    'borderRadius':"8px",
                    'borderWidth': "thin",
                    'borderStyle':"solid",
                    'borderColor':"#C6C4C4",
                }),
                #########
                
                    
                ], style={
                    'display' : "flex"
                }),
                # container row three
                # html.Div([]), # in case if needed
                
                
        ], style={
            # 'display' : "flex",
            }),
        ]),
        ##############################FACULTY################
    elif tab == "facult":
        return html.Div([
            # container row one
                html.Div([
                    ###### Container 1
                    html.Div([
                        html.Div([
                            html.H1('Student Teacher Ratio in Day Programs by Academic Year', 
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
                                    }), href="/faculty/stdtchrratio", refresh=True,),
                            ], style={
                                
                                }),
                        
                    ], style={
                        'backgroundColor':"white",
                        'height':"180px",
                        'width':"350px",
                        'marginTop':"20px",
                        'marginLeft':"15px",
                        'borderRadius':"8px",
                        'borderWidth': "thin",
                        'borderStyle':"solid",
                        'borderColor':"#C6C4C4",
                    }),
                    
                ], style={
                    'display':"flex",
                    }),
            
        ])
    ##############################SCHOOL AFFAIR################
    elif tab == "schafr":
        return html.Div([
            html.Div([
                html.Div([
                    html.H1('STUDENT', 
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
                    ], style={
                     
                        }),
                
            ], style={
                'backgroundColor':"white",
                'height':"180px",
                'width':"350px",
                'marginTop':"20px",
                'marginLeft':"15px",
                'borderRadius':"8px",
                'borderWidth': "thin",
                'borderStyle':"solid",
                'borderColor':"#C6C4C4",
            })
        ])