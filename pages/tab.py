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
                    dbc.Tab(label="學生", tab_id="stdent"), #Student
                    dbc.Tab(label="學校事務", tab_id="schafr") #School Affair
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
                                    'fontSize':"36px", #"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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
                            html.H1('入學途徑、性別和大學',  #Entry Path, Gender, and College
                                style={
                                    'fontSize':"36px",#"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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
                            html.H1('學生實習總時數', #Total Student Internship Hours
                                style={
                                    'fontSize':"36px",#"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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
                            html.H1('性別比例', #Gender Ratio
                                style={
                                    'fontSize':"36px",#"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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
                            html.H1('畢業後工作領域分佈', #Spread of Work Areas After Graduation
                                style={
                                    'fontSize':"36px",#"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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
                            html.H1('畢業工作類型', #Graduation Job Type
                                style={
                                    'fontSize':"36px",#"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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
                            html.H1('各系畢業生人數', #Number of Graduate by Department and Institutes
                                style={
                                    'fontSize':"36px",#"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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
                            html.H1('與部門的關聯暫停', #Association Suspension with Departments
                                style={
                                    'fontSize':"36px",#"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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
                            html.H1('退學學生數排名前十的學校', # Number of students dropping out of the top ten schools
                                style={
                                    'fontSize':"36px",#"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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
                            html.H1('入學中退學人數', # Number of dropouts withdrawals in the admission
                                style={
                                    'fontSize':"36px",#"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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
                            html.H1('圖書館資源', #Library Resources
                                style={
                                    'fontSize':"36px",#"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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
                            html.H1('兄弟姊妹學校', #Brother and Sister Schools
                                style={
                                    'fontSize':"36px",#"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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
                            html.H1('免學費學生人數', #Number of Students Free from Tuition and Fees
                                style={
                                    'fontSize':"36px",#"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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
                            html.H1('各系新生報到率', #Registration Rate of New Student Enrolled each Department
                                style={
                                    'fontSize':"36px",#"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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
                
                #####################
                # container xx
                ###### Container 5
                    # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('按學年劃分的日間課程師生比例', #Student Teacher Ratio in Day Programs by Academic Year
                                style={
                                    'fontSize':"36px",#"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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
                    ###### Container 6
                    # dbc.Col([
                    html.Div([
                        html.Div([
                            html.H1('專職、兼職教師人數', #Number Full-time, Part-time Teacher
                                style={
                                    'fontSize':"36px",#"28px"
                                    }),
                            ], style={
                                # 'backgroundColor':"gray", # for debuging
                                'marginTop':"10px",
                                'marginLeft':"10px",
                                'height':"125px",
                                'width':"325px",
                                }),
                        html.Div([
                            dcc.Link(html.Button("細節", #Detail
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