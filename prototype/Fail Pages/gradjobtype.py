import pandas as pd
import dash
from dash import callback, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_csv('./datas/gradjobtype.csv')

dash.register_page(__name__)

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
  {
    "label": "金融財務類", #Financial Services
    "value": "金融財務類"
  },
  {
    "label": "教育與訓練類", #Education and Training
    "value": "教育與訓練類"
  },
  {
    "label": "行銷與銷售類", #Marketing & Sales
    "value": "行銷與銷售類"
  },
  {
    "label": "政府公共事務類", #Governmental Public Affairs
    "value": "政府公共事務類"
  },
  {
    "label": "製造業",   #Manufacturing
    "value": "製造業"
  },
  {
    "label": "企業經營管理類", #Business Management
    "value": "企業經營管理類"
  },
  {
    "label": "個人及社會服務類", #Personal and Social Services
    "value": "個人及社會服務類"
  },
  {
    "label": "醫療保健類", #Healthcare
    "value": "醫療保健類"
  },
  {
    "label": "建築營造業", #Building construction
    "value": "建築營造業"
  },
  {
    "label": "物流運輸類", #Logistics & Transportation
    "value": "物流運輸類"
  },
  {
    "label": "司法、法律與公共安全類", #Justice, Law & Public Safety
    "value": "司法、法律與公共安全類"
  },
  {
    "label": "休閒與觀光旅遊類", #Leisure and Sightseeing Tourism
    "value": "休閒與觀光旅遊類"
  },
  {
    "label": "資訊科技類",  #Information Technology
    "value": "資訊科技類"
  },
  {
    "label": "科學、技術、工程、數學類", #Science, Technology, Engineering, Mathematics
    "value": "科學、技術、工程、數學類"
  },
  {
    "label": "藝文與影音傳播類", #Arts, Culture and Audio-visual Communication
    "value": "藝文與影音傳播類"
  },
  {
    "label": "天然資源、食品與農業類",  #Natural Resources, Food and Agriculture
    "value": "天然資源、食品與農業類"
  }],
        value=job_types,
        inline=True
    ),
    dcc.Tabs(id='tabs', value='1年', children=[
        dcc.Tab(label='畢業滿1年', value='1年'),#Graduated for 1 year
        dcc.Tab(label='畢業滿3年', value='3年'), #Graduated for 3 year
        # No information for 5 years after graduation
    ]),
    html.Div(id='tabs-content')
])

# Define the callback function to update the content based on the value of the tabs
@callback(
    Output('tabs-content', 'children'),
    [Input('tabs', 'value'),
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
    fig = px.bar(grouped_data, x='人數', y='工作職業類型', orientation='h',   # x : Number of People  y : Job Types
                 labels={'人數': '人數', '工作職業類型': '工作職業類型'})
                 # labels={'Number of people': 'Number of people', 'Job occupation type': 'Job occupation type'
    
    return dcc.Graph(figure=fig)


