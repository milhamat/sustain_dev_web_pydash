import dash
import pandas as pd
import plotly.express as px
from dash import callback, dcc, html
from dash.dependencies import Input, Output

df = pd.read_parquet('./datas/sankey_enroll.parquet')

# 獲取所有學年度(Get all academic years)
available_years = df['End_Year'].unique().tolist()

dash.register_page(__name__)

# 設定佈局 (Set layout)
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
    
    html.H1("入學管道、性別與學院之間的桑基圖"),  # Sankey Diagram between Entry Path, Gender, and Institute
    # html.H2("Sankey Diagram between Entry Path, Gender, and College"),  # 英文標題 (English Title)
    html.H4("來源資料:畢業流向問卷"),
    html.Label("選取學年度 (Select Academic Year):"),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': year, 'value': year} for year in available_years],
        value=available_years[0],  # 預設選擇第一個學年度 (Default select the first academic year)
        clearable=False
    ),
    html.Label("選取入學管道 (Entry Path Selection):"),
    dcc.RadioItems(
        id='top-entry-select',
        options=[
            {'label': '前5項(Top 5)', 'value': 5},  # Top 5
            {'label': '前10項(Top 10)', 'value': 10}  # Top 10
        ],
        value=5,  # Default to top 5
        labelStyle={'display': 'block'}
    ),
    dcc.Graph(id='parallel-categories-graph')
])

# 設置回調函數 (Set callback function)
@callback(
    Output('parallel-categories-graph', 'figure'),
    [Input('year-dropdown', 'value'), Input('top-entry-select', 'value')]
)

def update_parallel_categories(selected_year, top_n):
    # 根據選定的學年度過濾資料 (Filter data based on selected academic year)
    filtered_df = df[df['End_Year'] == selected_year]

    # 計算各分類的人數 (Calculate the count for each category)
    entry_counts = filtered_df.groupby(['Entry_Duct_Name'])['End_Year'].size().reset_index(name='Count')
    top_entries = entry_counts.nlargest(top_n, 'Count')['Entry_Duct_Name']
    filtered_df = filtered_df[filtered_df['Entry_Duct_Name'].isin(top_entries)]

    filtered_df['Count'] = filtered_df.groupby(['Entry_Duct_Name', 'Sex', 'Institute'])['End_Year'].transform('count')

    # 生成平行類別圖 (Generate parallel categories plot)
    fig = px.parallel_categories(
        filtered_df,
        dimensions=['Entry_Duct_Name', 'Sex', 'Institute'],
        color="Count",  # 根據計算出來的人數設置顏色 (Color coded by calculated counts)
        color_continuous_scale=px.colors.sequential.Inferno,
        labels={
            'Entry_Duct_Name': '入學管道名稱 (Entry Path)',  # Entry Path Name
            'Sex': '性別 (Gender)',  # Gender
            'Institute': '學院 (College)',  # College
            'Count': '人數 (Headcount)'  # Headcount
        }
    )

    return fig