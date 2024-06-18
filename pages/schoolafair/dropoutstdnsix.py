import pandas as pd
import dash
from dash import dcc, html, Input, Output, callback
import plotly.express as px
from dash.exceptions import PreventUpdate

dash.register_page(__name__)

df_out = pd.read_parquet('./datas/dropoutoutsix.parquet')
df_rest = pd.read_parquet('./datas/dropoutrestsix.parquet')

# Filter data for the years 108 to 112 and exclude "夜二專"
filtered_out_df = df_out[df_out['退學學年'].between(108, 112) & (df_out['Edu_Short'] != '夜二專')]
filtered_rest_df = df_rest[df_rest['休學學年'].between(108, 112) & (df_rest['Edu_Short'] != '夜二專')]

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
        options=[{'label': edu_short, 'value': edu_short} for edu_short in set(filtered_out_df['Edu_Short'].unique()) | set(filtered_rest_df['Edu_Short'].unique())],
        value=list(set(filtered_out_df['Edu_Short'].unique()) | set(filtered_rest_df['Edu_Short'].unique()))[0],
        inline=True
    ),
    html.Div(id='bar-chart-drp', style={
            'overflowY':"scroll",
            'height':"850px",
        })
])

@callback(
    Output('bar-chart-drp', 'children'),
    [Input('status-drp-dropdown', 'value'), Input('edu-short-drp-radioitems', 'value')]
)
def update_bar_charts(selected_status, selected_edu_short):
    if selected_status == 'Withdrawals':
        filtered_df = filtered_out_df[filtered_out_df['Edu_Short'] == selected_edu_short]
    else:
        filtered_df = filtered_rest_df[filtered_rest_df['Edu_Short'] == selected_edu_short]

    if filtered_df.empty:
        raise PreventUpdate

    charts = []

    # Generate a bar chart for each '系所'
    for department in filtered_df['系所'].unique():
        dept_data = filtered_df[filtered_df['系所'] == department]
        enrollment_channel_counts = dept_data.groupby('入學管道').size().reset_index(name='Count')

        if selected_status == 'Withdrawals':
            title = f'{department} 系所的入學管道退學人數 (學年度 108-112)'
        else:
            title = f'{department} 系所的入學管道休學人數 (學年度 108-112)'

        fig = px.bar(enrollment_channel_counts, x='Count', y='入學管道', orientation='h',
                     title=title, labels={'入學管道': '入學管道', 'Count': '人數'})
        
        fig.update_layout(yaxis={'categoryorder': 'total ascending'})

        charts.append(html.Div(dcc.Graph(figure=fig), 
        #                        style={
        #     'overflowY':"scroll",
        #     'height':"500px",
        # }
        ))

    return charts
