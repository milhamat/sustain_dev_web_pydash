import dash
from dash import callback, dcc, html
from dash.dependencies import Input, Output, State
import pandas as pd
import plotly.graph_objects as go

dash.register_page(__name__)

df = pd.read_parquet('./datas/male_female_ratio.parquet')

# 獲取不重複的年份和 Edu_Short (Get unique years and Edu_Short)
unique_years = df['Years'].unique()
unique_edu_short = df['Edu_Short'].unique()

# 設定應用佈局 (Set app layout)
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
    
    html.H1("男女生人數比較雷達圖"),
    html.H2("Radar Chart of Male and Female Count Comparison"),
    dcc.Dropdown(
        id='year-selector',
        options=[{'label': str(year), 'value': year} for year in unique_years],
        value=unique_years[0]
    ),
    html.Div([
        dcc.Checklist(
            id='select-all-checklist',
            options=[{'label': '全選 / 取消全選', 'value': 'all'}],# Select All / Deselect All
            value=[]
        ),
        dcc.Checklist(
            id='edu-short-selector',
            options=[{'label': edu, 'value': edu} for edu in unique_edu_short],
            value=unique_edu_short,
            labelStyle={'display': 'inline-block'}
        )
    ]),
    dcc.Graph(id='radar-chart'),
    html.P("Teamwork by Sandy, Emily, Debbie, and Ilham , directed by Prof. Ching-Shih Tsou. All rights reserved",
               style={
                   'textAlign' : "center",
                   'marginTop' : "10px",
                   }),
])

# 設定回調函數(Set callback function)
@callback(
    Output('edu-short-selector', 'value'),
    [Input('select-all-checklist', 'value')],
    [State('edu-short-selector', 'options')]
)
def update_edu_short_selector(select_all, options):
    if 'all' in select_all:
        # 全選(Select all)
        return [option['value'] for option in options]
    else:
        # 取消全選(Deselect all)
        return []


@callback(
    Output('radar-chart', 'figure'),
    [Input('year-selector', 'value'), Input('edu-short-selector', 'value')]
)
def update_radar_chart(selected_year, selected_edu_short):
    # 過濾數據 (Filter data)
    filtered_df = df[(df['Years'] == selected_year) & (df['Edu_Short'].isin(selected_edu_short))]
    grouped = filtered_df.groupby(['Dept_Short', 'Sex']).size().unstack(fill_value=0)

    # 創建雷達圖(Create radar chart)
    fig = go.Figure()

    # 添加女生數據(Add female data)
    if '女' in grouped.columns:
        fig.add_trace(go.Scatterpolar(
            r=grouped['女'],
            theta=grouped.index,
            fill='toself',
            name='女生(Female)',
            line_color='red'
        ))

    # 添加男生數據(Add male data)
    if '男' in grouped.columns:
        fig.add_trace(go.Scatterpolar(
            r=grouped['男'],
            theta=grouped.index,
            fill='toself',
            name='男生(Male)',
            line_color='blue'
        ))

    # 更新圖表佈局(Update chart layout)
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, max(grouped.max(), default=0)]
            )
        ),
        title=f"學年度 {selected_year} 的男女生人數比較<br>Comparison of Male and Female Count in Academic Year {selected_year}",  # 更新標題 (Update title)
        showlegend=True
    )
    
    return fig
