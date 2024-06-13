import pandas as pd
import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px


file_out_path = './datas/dropoutoutsix.parquet'
file_rest_path = './datas/dropoutrestsix.parquet'

df_out = pd.read_parquet(file_out_path)
df_rest = pd.read_parquet(file_rest_path)

# Filter data for the years 108 to 112 and exclude "夜二專"
filtered_out_df = df_out[df_out['退學學年'].between(108, 112) & (df_out['Edu_Short'] != '夜二專')]
filtered_rest_df = df_rest[df_rest['休學學年'].between(108, 112) & (df_rest['Edu_Short'] != '夜二專')]

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
    
    dcc.Dropdown(
        id='status-drp-dropdown',
        options=[
            {'label': '退學', 'value': 'Withdrawals'},
            {'label': '休學', 'value': 'Suspensions'}
        ],
        value='Withdrawals'
    ),
    dcc.RadioItems(
        id='edu-short-drp-radioitems',
        options=[{'label': edu_short, 'value': edu_short} for edu_short in filtered_out_df['Edu_Short'].unique()],
        value=filtered_out_df['Edu_Short'].unique()[0],
        inline=True
    ),
    dcc.Graph(id='bar-chart-drp')
])

@callback(
    Output('bar-chart-drp', 'figure'),
    [Input('status-drp-dropdown', 'value'), Input('edu-short-drp-radioitems', 'value')]
)

def update_bar_chart(selected_status, selected_edu_short):
    if selected_status == 'Withdrawals':
        filtered_df = filtered_out_df[filtered_out_df['Edu_Short'] == selected_edu_short]
    else:
        filtered_df = filtered_rest_df[filtered_rest_df['Edu_Short'] == selected_edu_short]
    
    # Group by '入學管道' and '系所' and count occurrences
    enrollment_channel_counts = filtered_df.groupby(['入學管道', '系所']).size().reset_index(name='Count')
    
    # Get top 10 '入學管道'
    top_channels = enrollment_channel_counts.groupby('入學管道')['Count'].sum().nlargest(10).index
    top_df = enrollment_channel_counts[enrollment_channel_counts['入學管道'].isin(top_channels)]
    
    if selected_status == 'Withdrawals':
        title = '入學管道的退學人數 (學年度 108-112)'
    else:
        title = '入學管道的休學人數 (學年度 108-112)'
    
    fig = px.bar(top_df, x='Count', y='入學管道', color='系所', orientation='h', 
                 title=title, labels={'入學管道': '入學管道', 'Count': '人數'})

    # Sort bars from small to large
    fig.update_layout(yaxis={'categoryorder':'total ascending'})

    return fig
