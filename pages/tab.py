import dash
import dash_bootstrap_components as dbc
from dash import callback, dcc, html, Input, Output

dash.register_page(__name__, path='/',
                   external_stylesheets=[dbc.themes.BOOTSTRAP],
                   meta_tags=[{'name': 'viewport',
                        'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}]
                   )

lang = ["中文", 'English']


layout = html.Div([
    html.Div([
        dbc.Row([dbc.Col(dcc.RadioItems(id='tab_lang_checklist', 
                            options=lang,
                            value="中文",
                            labelStyle={"margin":"0.2rem"},
                            inline=True,
                            ),
                         )], align="end"),
                
        
                dbc.Tabs(id="tabs",
                children=[
                    dbc.Tab(label="學生", tab_id="stdent"), 
                    dbc.Tab(label="學校事務", tab_id="schafr") 
                ],
                active_tab="stdent",
                ),
                
                html.Div(id='tab-Out', 
                         ),
            ]),
])
########################TAB LABEL########################################
@callback(Output('tabs', 'children'),
          Input('tab_lang_checklist', 'value')
          )

def change_tab(select):
    if select == "English":
        return dbc.Tab(label="Student", tab_id="stdent"),dbc.Tab(label="School Affair", tab_id="schafr") 
    else:
        return dbc.Tab(label="學生", tab_id="stdent"),dbc.Tab(label="學校事務", tab_id="schafr") 

########################TAB CONTAINERS########################################
@callback(Output('tab-Out','children'),
         Input('tabs','active_tab'),
         Input('tab_lang_checklist', 'value')
         )

##############################################################################
def render_content(tab, select):
    
    font = "32px"
    def lang_translate(id_triger):
        container = []
        if id_triger == "English":
            container = ["Student Distribution for Academic Year", "Entry Path, Gender, and College", "Total Student Internship Hours","Gender Ratio",
                         "Spread of Work Areas After Graduation","Graduation Job Type","Number of Graduate by Department and Institutes","Association Suspension with Departments",
                         "Number of students dropping out of the top ten schools","Number of dropouts withdrawals in the admission","Library Resources","Brother and Sister Schools",
                         "Number of Students Free from Tuition and Fees","Registration Rate of New Student Enrolled each Department","Student Teacher Ratio in Day Programs by Academic Year","Number Full-time, Part-time Teacher",
                         "Detail"]
            return container
        else:
            container = ["學年學生分佈", "入學途徑, 性別和大學", "學生實習總時數","性別比例",
                         "畢業後工作領域分佈","畢業工作類型","各系畢業生人數","大學休學原因與學系之間的熱圖及分佈情況",
                         "退學學生數排名前十的學校","入學中退學人數","圖書館資源","兄弟姊妹學校",
                         "免學費學生人數","各系新生報到率","按學年劃分的日間課程師生比例","專職、兼職教師人數",
                         "細節"]
            return container
    
    translate = lang_translate(select)
    
    
    if tab == 'stdent':
        return html.Div([
            ################################ ROW 1
            dbc.Row(
            [
                ############## 1
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[0],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/stddistbyyear", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
                ############## 2
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[1],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/entrypathgender", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
                ############## 3
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[2],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/stdintern", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
                ############## 4
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[3],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/stdngenderratio", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
            ],
            # align="start",
            className="g-0",
            style={'marginLeft':"10px"},
        ),
            ################################ ROW 2
            dbc.Row(
            [
                ############## 5
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[4],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/gradworkarea", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
                ############## 6
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[5],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/gradjobtype", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
                ############## 7
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[6],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/numgradbydepinst", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
                ############## 8
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[7],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/assosusdept", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
            ],
            className="g-0",
            style={'marginLeft':"10px"},
            # align="start",
        ),
            ################################ ROW 3
            dbc.Row(
            [
                ############## 9
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[8],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/dropoutstdn", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
                ############## 10
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[9],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/student/dropoutstdnsix", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
                ############## 
                dbc.Col(html.Div([
                    ########
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"white", ##C6C4C4
                                 'backgroundColor':"white"
                                 })),
                ##############
                dbc.Col(html.Div([
                    ########
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"white", ##C6C4C4
                                 'backgroundColor':"white"
                                 })),
            ],
            # justify="start",
            className="g-0",
            style={'marginLeft':"10px"},
            # align="start",
        ),
            ####################################
        ])
        ###############################SCHOOL AFFAIR#########################################
    elif tab == 'schafr':
        return html.Div([
            ################################ ROW 1
            dbc.Row(
            [
                ############## 11
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[10],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/schoolafair/libraryresources", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
                ############## 12
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[11],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/schoolafair/brosischool", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
                ############## 13
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[12],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/schoolafair/nmstdfrtuition", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
                ############## 14
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[13],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/schoolafair/regratenewenroll", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
            ],
            # align="start",
            className="g-0",
            style={'marginLeft':"10px"},
        ),
            ################################ ROW 2
            dbc.Row(
            [
                ############## 15
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[14],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/schoolafair/stdtchrratio", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
                ############## 16
                dbc.Col(html.Div([
                    dbc.Row([dbc.Col(html.Div([
                        html.P(translate[15],
                                style={
                                    'height':"80px",
                                    'marginTop':"10px",
                                    'marginLeft':"10px",
                                    'fontSize': "28px"
                                    }),
                                ])),
                             ]),
                    dbc.Row([dbc.Col(html.Div([
                        dcc.Link(html.Button(translate[16], 
                                            style={
                                                'marginTop':"30px",
                                                'backgroundColor':"#800080",
                                                'color':"white",
                                                'marginLeft':"78%",
                                                'borderRadius':"8px",
                                                'borderWidth': "thin",
                                                'borderStyle':"solid",
                                                'borderColor':"#C6C4C4",
                                    }), href="/schoolafair/numfulltimparttim", refresh=True,)
                                ])),
                             ]),
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
                ############## 
                dbc.Col(html.Div([
                    ########
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"white",#"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
                ##############
                dbc.Col(html.Div([
                    ########
                    ],
                                 style={
                                 'marginTop':"20px",
                                 'marginLeft':"10px",
                                 'height':"180px",
                                 'width':"350px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"white",#"#C6C4C4",
                                 'backgroundColor':"white"
                                 })),
            ],
            # align="start",
            className="g-0",
            style={'marginLeft':"10px"},
        ),
            #########################################################
        ])

