import dash
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import callback, dcc, html, Input, Output, ctx

dash.register_page(__name__, path='/')

layout = html.Div([
    html.Div([
                # dcc.Link(html.Button("中漢語",
                #                     id="jongwen",
                #                     style={
                #                         'backgroundColor':"#800080",
                #                         'color':"white",
                #                         'marginBottom':"10px",
                #                         'borderRadius':"8px",
                #                         'borderWidth': "thin",
                #                         'borderStyle':"solid",
                #                         'borderColor':"#C6C4C4",
                #                         }), href=""),
                # dcc.Link(html.Button("English",
                #                     id="eng",
                #                     style={
                #                         'backgroundColor':"#800080",
                #                         'color':"white",
                #                         'marginBottom':"10px",
                #                         'marginLeft':"5px",
                #                         'borderRadius':"8px",
                #                         'borderWidth': "thin",
                #                         'borderStyle':"solid",
                #                         'borderColor':"#C6C4C4",
                #                         }), href=""),
        
                dbc.Tabs(id="tabs",
                children=[
                    dbc.Tab(label="Student", tab_id="stdent"),
                    # dbc.Tab(label="Faculty", tab_id="facult"),
                    dbc.Tab(label="School Affair", tab_id="schafr")
                ],
                active_tab="stdent",
                ## dont know it's work or not
                style={
                    'color':"purple",
                }),
                
                html.Div(id='tab-Out',
                         style={
                             'width':"100%",
                             }),
            ], style={
                    'width': "100%",
             }),
])

#########################TRANSLATE TAB########################################
# @callback(
#     Output('stddistbyyear-lang-out','children'),
#     Input('stddistbyyear-jongwen','n_clicks'),
#     Input('stddistbyyear-eng','n_clicks')
# )

# def change_lang(btn1, btn2):
#     if "eng" == ctx.triggered_id:
#         return "Student Distribution for Academic Year"
#     else:
#         return "學年學生分佈"

########################TAB CONTAINERS########################################
@callback(Output('tab-Out','children'),
              Input('tabs','active_tab'))

def render_content(tab):
    ##############################STUDENT################
    if tab == 'stdent':
        return html.Div([
            html.Div([
                # container row one
            dbc.Row([
                html.Div([
                    ###### Container 1
                    # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('學年學生分佈', # Student Distribution for Academic Year  # 學年學生分佈
                                style={
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
                # ]),
                ###### Container 2
                # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('Entry Path, Gender, and College', 
                                style={
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
                # ]),
                ##########
                ###### Container 3
                # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('Total Student Internship Hours', 
                                style={
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
                # ]),
                    ##########
                    ###### Container 4
                    # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('Gender Ratio', 
                                style={
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
            # ]),
                        ],style={
                            'display' : "flex",
                            }),
            ]),
                ##########
                ################################################################
                # container row two
                dbc.Row([
                html.Div([
                    ###### Container 5
                    # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('Spread of Work Areas After Graduation', 
                                style={
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
            # ]),
                ##########
                    ###### Container 6
                    # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('Graduation Job Type', 
                                style={
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
                                                'marginLeft':"80%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/gradjobtype", refresh=True,),
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
            # ]),
                #########
                ###### Container 7
                # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('Number of Graduate by Department and Institutes', 
                                style={
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
                                                'marginLeft':"80%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/numgradbydepinst", refresh=True,),
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
            # ]),
                #########
                ###### Container 8
                # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('Association Suspension with Departments', 
                                style={
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
                                                'marginLeft':"80%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/assosusdept", refresh=True,),
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
                ####################
                    
                    
                ], style={
                    'display' : "flex"
                }),
            ]),
                # container row three
                # html.Div([]), # in case if needed
                dbc.Row([
                html.Div([
                    ###### Container 9
                    # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('Number of students dropping out of the top ten schools', # Student Distribution for Academic Year  # 學年學生分佈
                                style={
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
                                                'marginLeft':"80%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/dropoutstdn", refresh=True,),
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
                 ###### Container 10
                    html.Div([
                        html.Div([
                            html.H1('Number of dropouts withdrawals in the admission', # Student Distribution for Academic Year  # 學年學生分佈
                                style={
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
                                                'marginLeft':"80%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/dropoutstdnsix", refresh=True,),
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
            'display' : "flex"
        }),
        ]),
                # container row four
                
                
        ], style={
            # 'display' : "flex",
            }),
        ]),
        ##############################FACULTY################
    # elif tab == "facult":
    #     return html.Div([
    #         # container row one
    #         dbc.Row([
    #             html.Div([
    #                 ###### Container 1
    #                 # dbc.Col([
    #                 html.Div([
    #                     html.Div([
    #                         html.H1('Student Teacher Ratio in Day Programs by Academic Year', 
    #                             style={
    #                                 'fontSize':"28px",
    #                                 }),
    #                         ], style={
    #                             # 'backgroundColor':"gray", # for debuging
    #                             'marginTop':"10px",
    #                             'marginLeft':"10px",
    #                             'height':"125px",
    #                             'width':"325px",
    #                             }),
    #                     html.Div([
    #                         dcc.Link(html.Button("Detail", 
    #                                         style={
    #                                             'backgroundColor':"#800080",
    #                                             'color':"white",
    #                                             'marginLeft':"80%",
    #                                             'borderRadius':"8px",
    #                                             'borderWidth': "thin",
    #                                             'borderStyle':"solid",
    #                                             'borderColor':"#C6C4C4",
    #                                 }), href="/faculty/stdtchrratio", refresh=True,),
    #                         ], style={
                                
    #                             }),
                        
    #                 ], style={
    #                     'backgroundColor':"white",
    #                     'height':"180px",
    #                     'width':"350px",
    #                     'marginTop':"20px",
    #                     'marginLeft':"15px",
    #                     'borderRadius':"8px",
    #                     'borderWidth': "thin",
    #                     'borderStyle':"solid",
    #                     'borderColor':"#C6C4C4",
    #                 }),
    #             # ]),
    #                 #############
    #                 ###### Container 2
    #                 # dbc.Col([
    #                 html.Div([
    #                     html.Div([
    #                         html.H1('Number Full-time, Part-time Teacher', 
    #                             style={
    #                                 'fontSize':"28px",
    #                                 }),
    #                         ], style={
    #                             # 'backgroundColor':"gray", # for debuging
    #                             'marginTop':"10px",
    #                             'marginLeft':"10px",
    #                             'height':"125px",
    #                             'width':"325px",
    #                             }),
    #                     html.Div([
    #                         dcc.Link(html.Button("Detail", 
    #                                         style={
    #                                             'backgroundColor':"#800080",
    #                                             'color':"white",
    #                                             'marginLeft':"80%",
    #                                             'borderRadius':"8px",
    #                                             'borderWidth': "thin",
    #                                             'borderStyle':"solid",
    #                                             'borderColor':"#C6C4C4",
    #                                 }), href="/faculty/numfulltimparttim", refresh=True,),
    #                         ], style={
                                
    #                             }),
                        
    #                 ], style={
    #                     'backgroundColor':"white",
    #                     'height':"180px",
    #                     'width':"350px",
    #                     'marginTop':"20px",
    #                     'marginLeft':"15px",
    #                     'borderRadius':"8px",
    #                     'borderWidth': "thin",
    #                     'borderStyle':"solid",
    #                     'borderColor':"#C6C4C4",
    #                 }),
    #             # ]),
    #                 ###########
                    
    #             ], style={
    #                 'display':"flex",
    #                 }),
    #             ]),
    #         # container row Two
            
    #     ])
    ##############################SCHOOL AFFAIR################
    elif tab == "schafr":
        return html.Div([
            # container row one
            dbc.Row([
                html.Div([
                    ###### Container 1
                    # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('Library Resources', 
                                style={
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
                                                'marginLeft':"80%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/schoolafair/libraryresources", refresh=True,),
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
                # ], xs=10, sm=5, md=5, lg=6, xl=5),
                    ###############################
                    ###### Container 2
                    # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('Brother and Sister Schools', 
                                style={
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
                                                'marginLeft':"80%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/schoolafair/brosischool", refresh=True,),
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
                # ], xs=10, sm=5, md=5, lg=6, xl=5),
                    ###############################
                    ###### Container 3
                    # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('Number of Students Free from Tuition and Fees', 
                                style={
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
                                                'marginLeft':"80%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/schoolafair/nmstdfrtuition", refresh=True,),
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
                # ], xs=10, sm=5, md=5, lg=6, xl=5),
                    ###############################
                    ###### Container 4
                    # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('Regristration Rate of New Student Enrolled each Department', 
                                style={
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
                                                'marginLeft':"80%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/schoolafair/regratenewenroll", refresh=True,),
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
                # ], xs=10, sm=5, md=5, lg=6, xl=5),
                    ###############################
                    
        ], style={
            'display' : "flex"
            }),
                ]),
        # container row two
        ###############################################################
        dbc.Row([
            html.Div([
                
                ###### Container 5
                # html.Div([
                #         html.Div([
                #             html.H1('Number of students dropping out of the top ten schools', 
                #                 style={
                #                     'fontSize':"28px",
                #                     }),
                #             ], style={
                #                 # 'backgroundColor':"gray", # for debuging
                #                 'marginTop':"10px",
                #                 'marginLeft':"10px",
                #                 'height':"125px",
                #                 'width':"325px",
                #                 }),
                #         html.Div([
                #             dcc.Link(html.Button("Detail", 
                #                             style={
                #                                 'backgroundColor':"#800080",
                #                                 'color':"white",
                #                                 'marginLeft':"80%",
                #                                 'borderRadius':"8px",
                #                                 'borderWidth': "thin",
                #                                 'borderStyle':"solid",
                #                                 'borderColor':"#C6C4C4",
                #                     }), href="/schoolafair/dropoutstdn", refresh=True,),
                #             ], style={
                            
                #                 }),
                        
                #     ], style={
                #         'backgroundColor':"white",
                #         'height':"180px",
                #         'width':"350px",
                #         'marginTop':"20px",
                #         'marginLeft':"15px",
                #         'borderRadius':"8px",
                #         'borderWidth': "thin",
                #         'borderStyle':"solid",
                #         'borderColor':"#C6C4C4",
                #     }),
                
                ###### Container 6
                # html.Div([
                #         html.Div([
                #             html.H1('Number of dropouts withdrawals in the admission', 
                #                 style={
                #                     'fontSize':"28px",
                #                     }),
                #             ], style={
                #                 # 'backgroundColor':"gray", # for debuging
                #                 'marginTop':"10px",
                #                 'marginLeft':"10px",
                #                 'height':"125px",
                #                 'width':"325px",
                #                 }),
                #         html.Div([
                #             dcc.Link(html.Button("Detail", 
                #                             style={
                #                                 'backgroundColor':"#800080",
                #                                 'color':"white",
                #                                 'marginLeft':"80%",
                #                                 'borderRadius':"8px",
                #                                 'borderWidth': "thin",
                #                                 'borderStyle':"solid",
                #                                 'borderColor':"#C6C4C4",
                #                     }), href="/schoolafair/dropoutstdnsix", refresh=True,),
                #             ], style={
                            
                #                 }),
                        
                #     ], style={
                #         'backgroundColor':"white",
                #         'height':"180px",
                #         'width':"350px",
                #         'marginTop':"20px",
                #         'marginLeft':"15px",
                #         'borderRadius':"8px",
                #         'borderWidth': "thin",
                #         'borderStyle':"solid",
                #         'borderColor':"#C6C4C4",
                #     }),
                
                #####################
                # container xx
                ###### Container 7
                    # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('Student Teacher Ratio in Day Programs by Academic Year', 
                                style={
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
                                                'marginLeft':"80%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/schoolafair/stdtchrratio", refresh=True,),
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
                # ]),
                    #############
                    ###### Container 8
                    # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('Number Full-time, Part-time Teacher', 
                                style={
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
                                                'marginLeft':"80%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/schoolafair/numfulltimparttim", refresh=True,),
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
                ##########################
                ],style={
                    'display':"flex",}),
            ]),
        ###############################################################
         # container row Three
        ###############################################################
        
    ])