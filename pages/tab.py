import dash
import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, callback, dcc, html, Input, Output

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
                html.H1('學年學生分佈 Student Distribution for Academic Year ', 
                        style={
                            'fontSize':"28px",
                            }),
                dcc.Link(html.Button("Detail", 
                                     style={
                                         'backgroundColor':"white",
                                         'marginTop':"40px",
                                         'marginLeft':"70%",
                                         'borderRadius':"8px",
                                         'borderWidth': "thin",
                                         'borderStyle':"solid",
                                         'borderColor':"#C6C4C4",
                             }), href="/sunburst", refresh=True,),
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
        ##############################FACULTY################
    elif tab == "facult":
        return html.Div([
            html.Div([
                html.H1('FACULTY ', 
                        style={
                        'fontSize':"28px",}),
                dcc.Link(html.Button("Detail", 
                                     style={
                                         'backgroundColor':"white",
                                         'marginTop':"40px",
                                         'marginLeft':"70%",
                                         'borderRadius':"8px",
                                         'borderWidth': "thin",
                                         'borderStyle':"solid",
                                         'borderColor':"#C6C4C4",
                             }), href="/sunburst", refresh=True,),
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
                html.H1('STUDENT ', 
                        style={
                        'fontSize':"28px",}),
                dcc.Link(html.Button("Detail", 
                                     style={
                                         'backgroundColor':"white",
                                         'marginTop':"40px",
                                         'marginLeft':"70%",
                                         'borderRadius':"8px",
                                         'borderWidth': "thin",
                                         'borderStyle':"solid",
                                         'borderColor':"#C6C4C4",
                             }), href="/sunburst", refresh=True,),
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