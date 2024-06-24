import dash
import pandas as pd
import plotly.express as px
from dash import dcc, callback, html, Input, Output, ctx

dash.register_page(__name__)

lang = ""

df = pd.read_parquet('./datas/sunburst.parquet')

layout = html.Div([
    html.Div([
        dcc.Link(html.Button("Home",
                             style={
                                 'backgroundColor':"#800080",
                                 'color':"white",
                                 'marginBottom':"20px",
                                 'borderRadius':"8px",
                                 'borderWidth': "thin",
                                 'borderStyle':"solid",
                                 'borderColor':"#C6C4C4",
                                 }), href="/", refresh=True),
        # dcc.Link(html.Button("中漢語",
        #                      id="jongwen",
        #                      style={
        #                          'backgroundColor':"#800080",
        #                          'color':"white",
        #                          'marginBottom':"20px",
        #                          'marginLeft':"85%",
        #                          'borderRadius':"8px",
        #                          'borderWidth': "thin",
        #                          'borderStyle':"solid",
        #                          'borderColor':"#C6C4C4",
        #                          }), href=""),
        # dcc.Link(html.Button("English",
        #                      id="eng",
        #                      style={
        #                          'backgroundColor':"#800080",
        #                          'color':"white",
        #                          'marginBottom':"20px",
        #                          'marginLeft':"5px",
        #                          'borderRadius':"8px",
        #                          'borderWidth': "thin",
        #                          'borderStyle':"solid",
        #                          'borderColor':"#C6C4C4",
        #                          }), href=""),
        
        dcc.Dropdown(
                id='year-dropdown',
                options=[{'label': year, 'value': year} for year in df['學年度'].unique()],
                value=df['學年度'].unique()[0],
                clearable=False,
                style={
                    'marginBottom':"8px",
                }
            ),
        dcc.Graph(id="sunburst-chart", style={
                'height':"450px",}),
        html.P("Teamwork by Sandy, Emily, Debbie, and Ilham , directed by Prof. Ching-Shih Tsou. All rights reserved",
               style={
                   'textAlign' : "center",
                   'marginTop' : "30px",
                   }),  
    ])
])


@callback(
    Output("sunburst-chart", "figure"), 
    [Input("year-dropdown", "value")]
)


def AcademicYearChart(selected_year):
    
    filtered_df = df[df['學年度'] == selected_year]
    student_counts = filtered_df.groupby(['學制', '學制/系科']).size().reset_index(name='Count')
    fig = px.sunburst(student_counts, path=['學制', '學制/系科'], values='Count',
                      title=f'{selected_year} 學年學生分佈'
                    #   title=f'Student Distribution for Academic Year {selected_year}' 
                      )
    fig.update_layout(
        margin = dict(t=30, l=25, r=25, b=10)
    )
    return fig



