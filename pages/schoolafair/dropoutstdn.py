import pandas as pd
import dash
from dash import callback, html, dcc, Input, Output, State
# from dash.dependencies import Input, Output, State
import plotly.express as px

dash.register_page(__name__)

# Load the data
file_out_path = './datas/dropoutout.parquet'
file_rest_path = './datas/dropoutrest.parquet'

df_out = pd.read_parquet(file_out_path)
df_rest = pd.read_parquet(file_rest_path)

# Filter data for the years 108 to 112
filtered_out_df = df_out[df_out['退學學年'].between(108, 112)]
filtered_rest_df = df_rest[df_rest['休學學年'].between(108, 112)]


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
        id='status-dropdown',
        options=[
            {'label': '退學', 'value': 'Withdrawals'},
            {'label': '休學', 'value': 'Suspensions'}
        ],
        value='Withdrawals'
    ),
    dcc.Checklist(
        id='edu-short-checklist',
        options=[{'label': edu_short, 'value': edu_short} for edu_short in filtered_out_df['Edu_Short'].unique()] + [{'label': '清空/全選', 'value': 'clear'}],
        value=[edu_short for edu_short in filtered_out_df['Edu_Short'].unique()],
        inline=True
    ),
    dcc.Graph(id='bar-chart')
])

@callback(
    Output('edu-short-checklist', 'value'),
    [Input('edu-short-checklist', 'value')],
    State('edu-short-checklist', 'options')
)
def update_checklist(selected_values, options):
    all_options = [option['value'] for option in options if option['value'] != 'clear']
    if 'clear' in selected_values:
        if len(selected_values) == 1:
            return all_options 
        return ['clear']
    return selected_values

@callback(
    Output('bar-chart', 'figure'),
    [Input('status-dropdown', 'value'), Input('edu-short-checklist', 'value')]
)
def update_bar_chart(selected_status, selected_edu_short):
    if 'clear' in selected_edu_short:
        selected_edu_short = []
    
    if selected_status == 'Withdrawals':
        filtered_df = filtered_out_df[filtered_out_df['Edu_Short'].isin(selected_edu_short)]
        top_10_schools = filtered_df['Sch_Name'].value_counts().head(10).reset_index(name='Count').rename(columns={'index': 'Sch_Name'})
        title = '前十名生源學校的退學人數 (學年度 108-112)'
    else:
        filtered_df = filtered_rest_df[filtered_rest_df['Edu_Short'].isin(selected_edu_short)]
        top_10_schools = filtered_df['Sch_Name'].value_counts().head(10).reset_index(name='Count').rename(columns={'index': 'Sch_Name'})
        title = '前十名生源學校的休學人數 (學年度 108-112)'

    fig = px.bar(top_10_schools, x='Count', y='Sch_Name', orientation='h', 
                 title=title, labels={'Sch_Name': '學校名稱', 'Count': '人數'})
    
    return fig


