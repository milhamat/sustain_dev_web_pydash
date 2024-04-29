# https://dash.plotly.com/tutorial

import pandas as pd
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output

# df = pd.read_excel('./datas/102_111StdInfo1Acdm.xlsx')
df = pd.read_csv('./datas/sunburst.csv')

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div([
    # NAVBAR ################################################
    html.Div([
        html.Div([], style={
            'height':"25px",
            'backgroundColor' : "#5B005C",
            }),
        html.Div([
            html.P('校務永續發展中心',
                   style={
                       'color':"white",
                       'fontSize':"40px",
                       'fontWeight': "bold",
                   })
            ], style={
            'height':"70px",
            'backgroundColor' : "#800080",
            }),
        html.Img(src=app.get_asset_url("logo.png"),
                 style={
                     'height':"90px",
                     'width':"300px",
                     }),
        ],style={
            'height':"200px",
            'backgroundColor' : "#FFFFFF",
            'marginBottom':"20px",
        }),
    
    # BODY ################################################
    html.Div([
        html.Div([
            # html.P('Student Distribution'),
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
        ],style={
            'width': "50%",
            'height':"500px",
            'float':"left",
            'backgroundColor' : "#FFFFFF",
            'marginLeft':"20px",
            'marginRight':"10px",
            
        }),
        
        html.Div([
            html.P('Dash converts Python classes into HTML'),
        ],style={
            'width': "50%",
            'height':"500px",
            'float':"right",
            'backgroundColor' : "#FFFFFF",
            'marginRight':"20px",
            'marginLeft':"10px",
            
        }),
        # html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ],style = {
    'backgroundColor' : "#F9F9F9",
    'display' : "flex",
}),
    
    html.Div([
        # html.P('Dash converts Python classes into HTML'),
        # html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ],style = {
    'backgroundColor' : "#FFFFFF",
    'height':"500px",
    'margin':"20px",
}),
    
    html.Div([
        # html.P('Dash converts Python classes into HTML'),
        # html.P("This conversion happens behind the scenes by Dash's JavaScript front-end")
    ],style = {
    'backgroundColor' : "#FFFFFF",
    'height':"500px",
    'margin':"20px",
}),
    
    # FOOTER ################################################
    html.Footer([
        html.Div([
            html.P('國立臺北商業大學校務研究中心', 
                   style = {
                       'color':"white",
                       }),
            html.P('校址：100 臺北市中正區濟南路一段321號　 總機：(02)3322-2777',
                   style = {
                       'color':"white",
                       }),
        ], style = {
        'backgroundColor' : "#800080",
        })
], style = {
    'textAlign' : "center",
    'bottom':"0",
    'marginBottom':"0",
    'height': "100px",
    'backgroundColor' : "#800080",
    }),
    
    
],style = {
    'backgroundColor' : "#F9F9F9",
})

##########################SUNBURST###############################
@app.callback(
    Output("sunburst-chart", "figure"), 
    [Input("year-dropdown", "value")])


def AcademicYearChart(selected_year):
    filtered_df = df[df['學年度'] == selected_year]
    student_counts = filtered_df.groupby(['學制', '學制/系科']).size().reset_index(name='Count')
    fig = px.sunburst(student_counts, path=['學制', '學制/系科'], values='Count',
                      title=f'Student Distribution for Academic Year {selected_year}'
                      )
    fig.update_layout(
        margin = dict(t=25, l=25, r=25, b=10)
    )
    return fig
#########################################################

if __name__ == '__main__':
    app.run(debug=True)