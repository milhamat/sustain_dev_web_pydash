import dash
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from dash import dcc, html, Input, Output, callback_context, callback

dash.register_page(__name__)

df = pd.read_parquet('./datas/assosusdept.parquet')

# 確保數據欄位為字串格式
df['系所'] = df['系所'].astype(str)
df['休學原因'] = df['休學原因'].astype(str)
df['Edu_Short'] = df['Edu_Short'].astype(str)


# 所有學制選項
edu_short_options = [{'label': x, 'value': x} for x in df['Edu_Short'].unique()]

# Dash 應用的 HTML 布局
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
    
    html.H1('大學休學原因與學系之間的熱圖及分佈情況', style={'text-align': 'center'}),
    html.H3('學制選取:', style={'margin-top': '20px', 'text-align': 'left'}),
    dcc.Checklist(
        id='edu-short-checklist-asso',
        options=edu_short_options,
        value=[df['Edu_Short'].unique()[0]],  # 預設選擇第一個學制
        inline=True,
        style={'text-align': 'left', 'margin': '10px'}
    ),
    # html.Div([
    #     html.Button('全選', id='select-all-button-asso', n_clicks=0),
    #     html.Button('取消全選', id='deselect-all-button-asso', n_clicks=0)
    # ], style={'text-align': 'center', 'margin': '10px'}),
    
    dcc.Graph(id='heatmap-graph-asso')
])

# Callbacks to handle the select-all and deselect-all functionality
# @callback(
#     Output('edu-short-checklist-asso', 'value'),
#     [Input('select-all-button', 'n_clicks'),
#      Input('deselect-all-button-asso', 'n_clicks')],
#     prevent_initial_call=True
# )
# def update_selection(select_all_clicks, deselect_all_clicks):
#     triggered_id = callback_context.triggered[0]['prop_id'].split('.')[0]
#     if triggered_id == 'select-all-button-asso':
#         return [option['value'] for option in edu_short_options]
#     elif triggered_id == 'deselect-all-button-asso':
#         return []
    # raise PreventUpdate

# Callback to update the heatmap based on selected education shorts
@callback(
    Output('heatmap-graph-asso', 'figure'),
    Input('edu-short-checklist-asso', 'value')
)
def update_graph(selected_edu_shorts):
    filtered_df = df[df['Edu_Short'].isin(selected_edu_shorts)]
    top_reasons = filtered_df['休學原因'].value_counts().nlargest(10).index
    top_departments = filtered_df['系所'].value_counts().nlargest(10).index
    filtered_df = filtered_df[filtered_df['休學原因'].isin(top_reasons) & filtered_df['系所'].isin(top_departments)]
    heatmap_data = filtered_df.groupby(['系所', '休學原因']).size().reset_index(name='人數')
    fig = px.density_heatmap(
        heatmap_data, x='系所', y='休學原因', z='人數',
#        title='大學休學原因與學系之間的熱圖及分佈情況'
    )
    fig.add_trace(go.Histogram(x=filtered_df['系所'], yaxis='y2', name='系所休學總人數'))
    fig.add_trace(go.Histogram(y=filtered_df['休學原因'], xaxis='x2', name='休學原因總人數'))
    fig.update_layout(
        barmode='overlay', xaxis=dict(domain=[0, 0.85], title='系所'), yaxis=dict(domain=[0, 0.85], title='休學原因'),
        xaxis2=dict(domain=[0.85, 1], showticklabels=False), yaxis2=dict(domain=[0.85, 1], showticklabels=False),
        coloraxis_colorbar=dict(x=1.01, y=0.5, yanchor="middle", title='人數', len=0.7)
    )
    return fig


