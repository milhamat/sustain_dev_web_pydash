import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import json, requests

dash.register_page(__name__)

# url = 'https://raw.githubusercontent.com/milhamat/NtubDashboardDatas/main/grad_job.csv'
# url_json = 'https://raw.githubusercontent.com/milhamat/NtubDashboardDatas/main/taiwanjson.json'

# geojson_path = url_json
# data = pd.read_csv(url)

geojson_path = r'./datas/taiwanjson.json'
data = pd.read_csv('./datas/grad_job.csv')

# resp = requests.get(geojson_path)
# geojson = json.loads(resp.text)

with open(geojson_path, encoding='utf-8') as f:
    geojson = json.load(f)
#     geojson = json.loads(resp.text)

data_count = data.groupby(['工作所在地點_境內區域', '畢業滿_年']).size().reset_index(name='Count')


# 應用的布局
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
    
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': f"{year} 年後", 'value': year} for year in sorted(data_count['畢業滿_年'].unique())],
        value=sorted(data_count['畢業滿_年'].unique())[0]  # 預設選項
    ),
    dcc.Graph(id='bar-graph'),
    dcc.Graph(id='map-graph'),
    
])

# Callbacks 更新地圖和柱狀圖
@callback(
    [Output('map-graph', 'figure'),
     Output('bar-graph', 'figure')],
    [Input('year-dropdown', 'value')]
)
def update_content(selected_year):
    filtered_data = data_count[data_count['畢業滿_年'] == selected_year]
    
    # 更新地圖
    map_fig = px.scatter_geo(filtered_data,
                             geojson=geojson,
                             locations='工作所在地點_境內區域',
                             featureidkey='properties.name',
                             color='Count',
                             size='Count',
                             projection='mercator',
                             hover_name='工作所在地點_境內區域',
                             hover_data={'畢業滿_年': True, 'Count': True})
    map_fig.update_geos(fitbounds="locations")
    
    # 更新柱狀圖，按人數由多到少排序
    bar_fig = px.bar(filtered_data.sort_values(by='Count', ascending=False),
                     x='Count',
                     y='工作所在地點_境內區域',
                     color='Count',
                     orientation='h',
                     title=f'畢業後{selected_year}年在各縣市工作的人口數')
    bar_fig.update_layout(margin=dict(l=200), yaxis=dict(tickfont=dict(size=10)),
                          yaxis_title="縣市", xaxis_title="人數")

    return map_fig, bar_fig

