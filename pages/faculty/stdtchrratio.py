import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd


data = pd.read_parquet('./datas/student_teacher_ratio.parquet')

dash.register_page(__name__)

layout = html.Div([
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
    
    html.H2("各學年度日間學制師生比與師生人數"),
    dcc.Graph(id='dual-axis-bar-line-chart')
])

@callback(
    Output('dual-axis-bar-line-chart', 'figure'),
    [Input('dual-axis-bar-line-chart', 'id')]
)
def update_chart(_):
    fig = go.Figure()

    fig.add_trace(go.Bar(
        x=data['學年度'],
        y=data['日間學制學生數'],
        name='學生數',
        text=data['日間學制學生數'],
        hovertemplate='<b>%{x}</b><br>學生數: %{y}<extra></extra>',
    ))

    fig.add_trace(go.Bar(
        x=data['學年度'],
        y=data['日間專任教師(含助教)'],
        name='老師數',
        text=data['日間專任教師(含助教)'],
        hovertemplate='<b>%{x}</b><br>老師數: %{y}<extra></extra>',
    ))

    fig.add_trace(go.Scatter(
        x=data['學年度'],
        y=data['日間生師比'],
        mode='lines+markers',
        name='日間生師比',
        yaxis='y2',
    ))

    # 設定圖表佈局
    fig.update_layout(
        title='各學年度日間學制師生比與師生人數',
        xaxis=dict(title='學年度'),
        yaxis=dict(title='人數'),
        yaxis2=dict(title='日間生師比', overlaying='y', side='right'),
        barmode='group',
        legend=dict(x=1.1, y=1),
    )

    return fig
