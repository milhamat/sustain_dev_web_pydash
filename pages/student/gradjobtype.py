import pandas as pd
import dash
from dash import callback, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

dash.register_page(__name__)

df = pd.read_parquet('./datas/gradjobtype.parquet')

#Type of work occupation
job_types = df['工作職業類型'].unique()

# Define the contents of the option card
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
    
    html.H4("各學院畢業就業類型的橫條圖"),  #Banner Chart of Graduation Employment Types by Faculty
    html.P("工作職業類型:"), #Type of work occupation
    dcc.Checklist(
        id='job-types',
        options=[
            {"label": "金融財務類", "value": "金融財務類"},
            {"label": "教育與訓練類", "value": "教育與訓練類"},
            {"label": "行銷與銷售類", "value": "行銷與銷售類"},
            {"label": "政府公共事務類", "value": "政府公共事務類"},
            {"label": "製造業", "value": "製造業"},
            {"label": "企業經營管理類", "value": "企業經營管理類"},
            {"label": "個人及社會服務類", "value": "個人及社會服務類"},
            {"label": "醫療保健類", "value": "醫療保健類"},
            {"label": "建築營造業","value": "建築營造業"},
            {"label": "物流運輸類", "value": "物流運輸類"},
            {"label": "司法、法律與公共安全類", "value": "司法、法律與公共安全類"}, 
            {"label": "休閒與觀光旅遊類", "value": "休閒與觀光旅遊類"}, 
            {"label": "資訊科技類", "value": "資訊科技類"}, 
            {"label": "科學、技術、工程、數學類", "value": "科學、技術、工程、數學類"},
            {"label": "藝文與影音傳播類", "value": "藝文與影音傳播類"},
            {"label": "天然資源、食品與農業類", "value": "天然資源、食品與農業類"},
            ],
        # value=['金融財務類', '教育與訓練類'],
        value=job_types,
        inline=True,
    ),
    dcc.Tabs(id='tabs-job-type', value='1年', children=[
        dcc.Tab(label='畢業滿1年', value='1年'),#Graduated for 1 year
        dcc.Tab(label='畢業滿3年', value='3年'), #Graduated for 3 year
        # No information for 5 years after graduation
    ]),
    html.Div(id='tabs-content-job-type'),
])

# Define the callback function to update the content based on the value of the tabs
@callback(
    Output('tabs-content-job-type', 'children'),
    [Input('tabs-job-type', 'value'),
     Input('job-types', 'value')]
)
def update_content(selected_tab, selected_job_types):
    # Filter out data for selected years
    filtered_data = df[df['畢業滿_年'] == int(selected_tab[0])]

    # Remove data for which the Job Occupation Type field is unselected
    filtered_data = filtered_data[filtered_data['工作職業類型'].isin(selected_job_types)]

    # Grouping and counting by type of work occupation
    grouped_data = filtered_data.groupby(['工作職業類型']).size().reset_index(name='人數')

    # Drawing of horizontal stripes
    fig = px.bar(grouped_data, x='人數', y='工作職業類型', orientation='h',   
                 labels={'人數': '人數', '工作職業類型': '工作職業類型'})
    
    return dcc.Graph(figure=fig)


