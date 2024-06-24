import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html

dash.register_page(__name__)

df = pd.read_parquet('./datas/brosischool.parquet')

# 計算每個國家的學校數量
country_counts = df.groupby(['區域別', '國家']).size().reset_index(name='學校數量')

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
                    # title="大學國際姊妹校分布圖"
                    )

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
    html.H2("大學國際姊妹校分布圖"),
    dcc.Graph(figure=fig, 
              style={
                  'marginLeft': "10px",
                             }),
    html.P("Teamwork by Sandy, Emily, Debbie, and Ilham , directed by Prof. Ching-Shih Tsou. All rights reserved",
               style={
                   'marginTop' : "10px",
                   'textAlign' : "center",
                   }),
])