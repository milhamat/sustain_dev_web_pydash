import dash
import pandas as pd
import plotly.express as px
from dash import callback, dcc, html

# url = 'https://raw.githubusercontent.com/milhamat/NtubDashboardDatas/main/brosischool.csv'
# df = pd.read_csv(url)

df = pd.read_csv('./datas/brosischool.csv')

# 計算每個國家的學校數量
country_counts = df.groupby(['區域別', '國家']).size().reset_index(name='學校數量')

dash.register_page(__name__)

# 生成 choropleth 地圖
fig = px.choropleth(country_counts,
                    locations="國家",
                    locationmode='country names',
                    color="學校數量",
                    hover_name="國家",
                    hover_data=['區域別', '學校數量'],
                    color_continuous_scale=px.colors.sequential.Plasma,
                    labels={'學校數量':'學校數量'},
                    projection="natural earth",
                    title="大學國際姊妹校分布圖")

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
    dcc.Graph(figure=fig)
])