import dash
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import callback, dcc, html, Input, Output

dash.register_page(__name__, path='/')

layout = html.Div([
    html.Div([
                dbc.Tabs(id="tabs",
                children=[
                    dbc.Tab(label="School Affair", tab_id="schafr"),
                    dbc.Tab(label="Faculty", tab_id="facult"),
                    dbc.Tab(label="Student", tab_id="stdent")
                ],
                active_tab="schafr",
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
    ##############################SCHOOL AFFAIR################
    if tab == 'schafr':
        return html.Div([
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
                                }), href="/sunburst", refresh=True,),
                        ], style={
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
                                }), href="/sankey", refresh=True,),
                        ], style={
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
            }),
            ##########
               
        ], style={
            'display' : "flex",
            }),
        ])
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
    ##############################STUDENT################
    elif tab == "stdent":
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