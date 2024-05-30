import pandas as pd
import dash
from dash import callback, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

df = pd.read_excel('./datas/學20.學生實習情形-以「系(所)」統計.xlsx')

df = df[['學年度', '學制班別', '系所名稱', '實習總時數']]  
df_110 = df[df['學年度'] == 110]
df_111 = df[df['學年度'] == 111]

dash.register_page(__name__)

checklist_options = [
    {'label': '學士班(日間)', 'value': '學士班(日間)'},  #Bachelor's Degree (Daytime)
    {'label': '五專', 'value': '五專'},  #Five specialties
    {'label': '學士班(進修)', 'value': '學士班(進修)'},  #Bachelor's degree (further study)
    {'label': '碩士班(日間)', 'value': '碩士班(日間)'}  #Master's class (day time
]

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
    
    dcc.Tabs(id="tabs", value='tab-110', children=[
        dcc.Tab(label='110學年度', value='tab-110'),
        dcc.Tab(label='111學年度', value='tab-111'),
    ]),
    html.Div([
        dcc.Checklist(
            id='checklist',
            options=checklist_options,
            value=[checklist_options[0]['value']] ,
             inline=True,
             style = {
                 'marginTop':"10px"
             }
        )
    ]),
    html.Div(id='tabs-content')
])

@callback(
    Output('tabs-content', 'children'),
    [Input('tabs', 'value'),
     Input('checklist', 'value')],
)

def render_content(tab, selected_classes):
    if tab == 'tab-110':
        filtered_df = df_110[df_110['學制班別'].isin(selected_classes)]  #Academic class
        pivot_table = filtered_df.pivot_table(index='學制班別', columns='系所名稱', values='實習總時數', aggfunc='sum').reset_index()
        fig = px.bar(pivot_table.melt(id_vars='學制班別', var_name='系所名稱', value_name='實習總時數'),
                     x='學制班別', y='實習總時數', color='系所名稱', barmode='group',
                     title=f'110學年度 {", ".join(selected_classes)} 各系所名稱的實習總時數')
    elif tab == 'tab-111':
        filtered_df = df_111[df_111['學制班別'].isin(selected_classes)]
        pivot_table = filtered_df.pivot_table(index='學制班別', columns='系所名稱', values='實習總時數', aggfunc='sum').reset_index()
        fig = px.bar(pivot_table.melt(id_vars='學制班別', var_name='系所名稱', value_name='實習總時數'),
                     x='學制班別', y='實習總時數', color='系所名稱', barmode='group',
                     title=f'111學年度 {", ".join(selected_classes)} 各系所名稱的實習總時數')

    return dcc.Graph(figure=fig)

