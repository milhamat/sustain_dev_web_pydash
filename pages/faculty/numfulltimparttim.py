import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output, State
import plotly.graph_objects as go
import pandas as pd

file_path_full_time = './datas/教1-1.專任教師數-以「系(所)」統計.csv'
file_path_part_time = './datas/教2-1.兼任教師數-以「系(所)」統計.csv'
data_full_time = pd.read_csv(file_path_full_time)
data_part_time = pd.read_csv(file_path_part_time)

categories = {
    "行政": ["體育室", "通識教育中心", "軍訓教官"],
    "系所": ["財務金融系", "國際商務系", "會計資訊系", "企業管理系", "財政稅務系", "會計與資料科學科", "資訊管理系", "創新經營學院", "應用外語系", "數位多媒體設計系", "創意科技與產品設計系", "商品創意經營系", "商業設計管理系"],
    "研究所": ["創意設計與經營研究所", "貿易實務法律暨談判碩士學位學程", "資訊與決策科學研究所"],
    "學院": ["財經學院", "財經學院博士班"]
}

dash.register_page(__name__)

# 定義選項
teacher_types = ['專任', '兼任'] # Full-time, Part-time

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
    
    html.H1("各學年度日間學制專/兼任教師人數"), # Number of Full-time/Part-time Teachers in Daytime Programs by Academic Year
    html.Div([
        html.Label("選擇分類:"), # Category Selection
        dcc.Checklist(
            id='category-selector',
            options=[{'label': cat, 'value': cat} for cat in categories.keys()],
            value=[],
            labelStyle={'display': 'inline-block'}
        )
    ]),
    html.Div(id='department-div', children=[
        html.Label("選擇系所類別:"), # Select Department Category
        dcc.Checklist(
            id='department-selector',
            options=[],
            value=[],
            labelStyle={'display': 'inline-block'}
        )
    ]),
    html.Div(id='teacher-type-div', children=[
        html.Label("選擇教師類型:"), # Select Teacher Type
        dcc.Checklist(
            id='teacher-type-selector',
            options=[{'label': '全選', 'value': 'all'}] + [{'label': t, 'value': t} for t in teacher_types],
            value=[],
            labelStyle={'display': 'inline-block'}
        )
    ]),
    dcc.Graph(id='line-chart')
])

def update_checklist(selected_options, all_options):
    if 'all' in selected_options:
        if set(selected_options) == set(['all'] + list(all_options)):
            return []
        else:
            return ['all'] + list(all_options)
    return selected_options

@callback(
    Output('department-selector', 'options'),
    [Input('category-selector', 'value')]
)
def update_department_options(selected_categories):
    if not selected_categories:
        return []
    departments = []
    for category in selected_categories:
        departments.extend(categories[category])
    return [{'label': '全選', 'value': 'all'}] + [{'label': dept, 'value': dept} for dept in departments]

@callback(
    Output('department-selector', 'value'),
    [Input('department-selector', 'value')],
    [State('department-selector', 'options')]
)
def update_department_selector(selected_options, options):
    if not options:
        return []
    all_options = [option['value'] for option in options if option['value'] != 'all']
    return update_checklist(selected_options, all_options)

@callback(
    Output('teacher-type-div', 'style'),
    [Input('department-selector', 'value')]
)
def update_teacher_type_visibility(selected_departments):
    if selected_departments:
        return {'display': 'block'}
    return {'display': 'none'}

@callback(
    Output('teacher-type-selector', 'value'),
    [Input('teacher-type-selector', 'value')],
    [State('teacher-type-selector', 'options')]
)
def update_teacher_type_selector(selected_options, options):
    if not options:
        return []
    all_options = [option['value'] for option in options if option['value'] != 'all']
    return update_checklist(selected_options, all_options)

@callback(
    Output('line-chart', 'figure'),
    [
        Input('teacher-type-selector', 'value'),
        Input('department-selector', 'value')
    ]
)
def update_chart(selected_teacher_types, selected_departments):
    fig = go.Figure()

    # 移除 'all' 選項
    selected_teacher_types = [t for t in selected_teacher_types if t != 'all']
    selected_departments = [d for d in selected_departments if d != 'all']

    # 如果未選擇任何教師類型或系所，不顯示資料
    if not selected_teacher_types or not selected_departments:
        fig.update_layout(
            title='各學年度日間學制專/兼任教師人數', # Number of Full-time/Part-time Teachers in Daytime Programs by Academic Year
            xaxis=dict(title='學年度'), # Academic Year
            yaxis=dict(title='總人數') # Total Number
        )
        return fig

    for teacher_type in selected_teacher_types:
        data = data_full_time if teacher_type == '專任' else data_part_time
        for dept in selected_departments:
            filtered_data = data[data['單位名稱'] == dept] # Unit Name
            total_column = f'{teacher_type}教師數-教師總數總計' # Number of Teachers - Total Teacher Count
            if total_column in filtered_data.columns:
                fig.add_trace(go.Scatter(
                    x=filtered_data['學年度'], # Academic Year
                    y=filtered_data[total_column],
                    mode='lines+markers',
                    name=f'{teacher_type} {dept} 總人數' # Total Number
                ))

    # 設定圖表佈局
    fig.update_layout(
        title='各學年度日間學制專/兼任教師人數', # Number of Full-time/Part-time Teachers in Daytime Programs by Academic Year
        xaxis=dict(title='學年度'), # Academic Year
        yaxis=dict(title='總人數'), # Total Number
        legend=dict(x=1.1, y=1),
    )

    return fig