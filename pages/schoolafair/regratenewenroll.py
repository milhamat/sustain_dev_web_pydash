import dash
from dash import dcc, html, callback
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import pandas as pd


data = pd.read_parquet('./datas/regratenewenroll.parquet')

dash.register_page(__name__)

# 檢查年份欄位
data['學年度'] = data['學年度'].astype(str).str.extract('(\d+)', expand=False).astype(int)

# 過濾需要的欄位
filtered_data = data[['學年度', '系所名稱', '日間/進修', '學制班別', 
                      '當學年度總量內核定新生招生名額(A)', '當學年度新生保留入學資格人數(B)', 
                      '當學年度總量內新生招生核定名額之實際註冊人數(C)', '當學年度各學系境外(新生)學生實際註冊人數 (E)', 
                      '當學年度新生註冊率(%)D=〔(C+E)/(A-B+E)〕＊100％']]

def create_checklist(id, options, all_selected):
    return html.Div([
        dcc.Checklist(
            id=id,
            options=[{'label': '全選', 'value': 'all'}] + [{'label': opt, 'value': opt} for opt in options],
            value=['all'] + list(all_selected) if len(all_selected) > 0 else [],
            labelStyle={'display': 'inline-block'}
        ),
    ])

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
    
    html.H2("各學年度各系新生註冊人數與註冊率"),
    html.Div([
        html.Label("選擇日間/進修:"),
        create_checklist('day-night-selector', list(filtered_data['日間/進修'].unique()), list(filtered_data['日間/進修'].unique()))
    ]),
    html.Div([
        html.Label("選擇學制班別:"),
        create_checklist('program-selector', list(filtered_data['學制班別'].unique()), list(filtered_data['學制班別'].unique()))
    ]),
    html.Div([
        html.Label("選擇系所名稱:"),
        create_checklist('department-selector', list(filtered_data['系所名稱'].unique()), list(filtered_data['系所名稱'].unique()))
    ]),
    dcc.Graph(id='stacked-bar-line-chart')
])

def update_checklist(selected_options, all_options):
    if 'all' in selected_options:
        if len(selected_options) == 1:
            return ['all'] + list(all_options)
        else:
            return []
    return selected_options

@callback(
    Output('stacked-bar-line-chart', 'figure'),
    [
        Input('day-night-selector', 'value'),
        Input('program-selector', 'value'),
        Input('department-selector', 'value')
        
    ],prevent_initial_call=True,
)
def update_chart(selected_day_night, selected_programs, selected_departments):
    selected_day_night = [opt for opt in selected_day_night if opt != 'all']
    selected_programs = [opt for opt in selected_programs if opt != 'all']
    selected_departments = [opt for opt in selected_departments if opt != 'all']
    
    filtered = filtered_data[
        (filtered_data['日間/進修'].isin(selected_day_night)) &
        (filtered_data['學制班別'].isin(selected_programs)) &
        (filtered_data['系所名稱'].isin(selected_departments))
    ]
    
    fig = go.Figure()

    color_pairs = [
        ('#1f77b4', '#aec7e8'),  # 深藍和淺藍
        ('#ff7f0e', '#ffbb78'),  # 深橙和淺橙
        ('#2ca02c', '#98df8a'),  # 深綠和淺綠
        ('#d62728', '#ff9896'),  # 深紅和粉紅
        ('#9467bd', '#c5b0d5'),  # 深紫和淺紫
        ('#8c564b', '#c49c94'),  # 深棕和淺棕
        ('#e377c2', '#f7b6d2'),  # 深粉和淺粉
        ('#7f7f7f', '#c7c7c7'),  # 深灰和淺灰
        ('#bcbd22', '#dbdb8d'),  # 深黃和淺黃
        ('#17becf', '#9edae5')   # 深青和淺青
    ]

    for i, department in enumerate(filtered['系所名稱'].unique()):
        department_data = filtered[filtered['系所名稱'] == department]
        color = color_pairs[i % len(color_pairs)]
        fig.add_trace(go.Bar(
            x=department_data['學年度'],
            y=department_data['當學年度總量內新生招生核定名額之實際註冊人數(C)'],
            name=department,
            text=department_data['當學年度總量內新生招生核定名額之實際註冊人數(C)'],
            hovertemplate='<b>%{x}</b><br>註冊人數: %{y}<extra></extra>',
            textposition='auto',
            marker_color=color[0]
        ))
        fig.add_trace(go.Scatter(
            x=department_data['學年度'],
            y=department_data['當學年度新生註冊率(%)D=〔(C+E)/(A-B+E)〕＊100％'],
            mode='lines+markers',
            name=f'{department} 註冊率',
            yaxis='y2',
            line=dict(color=color[1])
        ))

    # 設定圖表佈局
    fig.update_layout(
        title='各學年度各系新生註冊人數與註冊率',
        xaxis=dict(title='學年度', tickmode='linear'),
        yaxis=dict(title='新生註冊人數'),
        yaxis2=dict(title='新生註冊率(%)', overlaying='y', side='right'),
        barmode='group',
        legend=dict(x=1.1, y=1),
    )

    return fig

@callback(
    Output('program-selector', 'options'),
    [Input('day-night-selector', 'value')],
    
)
def update_program_selector_options(selected_day_night):
    selected_day_night = [opt for opt in selected_day_night if opt != 'all']
    filtered = filtered_data[filtered_data['日間/進修'].isin(selected_day_night)]
    program_options = [{'label': program, 'value': program} for program in filtered['學制班別'].unique()]
    return [{'label': '全選', 'value': 'all'}] + program_options

@callback(
    Output('program-selector', 'value'),
    [Input('program-selector', 'options'), Input('program-selector', 'value')],
    
)
def update_program_selector_value(program_options, selected_programs):
    all_programs = [opt['value'] for opt in program_options if opt['value'] != 'all']
    return update_checklist(selected_programs, all_programs)

# @callback(
#     Output('department-selector', 'options', allow_duplicate=True),
#     [Input('day-night-selector', 'value'), Input('program-selector', 'value')],
#     prevent_initial_call=True,
# )
# def update_department_selector_options(selected_day_night, selected_programs):
#     selected_day_night = [opt for opt in selected_day_night if opt != 'all']
#     selected_programs = [opt for opt in selected_programs if opt != 'all']
#     filtered = filtered_data[
#         (filtered_data['日間/進修'].isin(selected_day_night)) &
#         (filtered_data['學制班別'].isin(selected_programs))
#     ]
#     department_options = [{'label': dept, 'value': dept} for dept in filtered['系所名稱'].unique()]
#     return [{'label': '全選', 'value': 'all'}] + department_options

# @callback(
#     Output('department-selector', 'value'),
#     [Input('department-selector', 'options'), Input('department-selector', 'value')],
    
# )
# def update_department_selector_value(department_options, selected_departments):
#     all_departments = [opt['value'] for opt in department_options if opt['value'] != 'all']
#     return update_checklist(selected_departments, all_departments)

@callback(
    Output('day-night-selector', 'value'),
    [Input('day-night-selector', 'value')],
    
)
def update_day_night_selector(selected_options):
    all_options = filtered_data['日間/進修'].unique().tolist()
    return update_checklist(selected_options, all_options)


