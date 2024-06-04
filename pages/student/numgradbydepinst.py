import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html

url = 'https://raw.githubusercontent.com/milhamat/NtubDashboardDatas/main/barchart_std.csv'
data = pd.read_csv(url)
# data = pd.read_csv('./datas/barchart_std.csv')

dash.register_page(__name__)

# STEP 2: 過濾出已畢業的學生
graduated_data = data[data['Status'] == '畢業']

# STEP 3: 組織需要的數據欄位
organized_data = graduated_data[['Dept_Short', 'End_Year', 'Edu_Short', '畢業滿_年']]

    # STEP 4: 計算各系所的畢業人數
grad_counts = organized_data.groupby(['Dept_Short', 'Edu_Short', '畢業滿_年']).size().reset_index(name='畢業人數')

    # 過濾已畢業的學生
graduated_data = data[data['Status'] == '畢業']

# 組織所需的數據欄位
organized_data = graduated_data[['Dept_Short', 'Edu_Short', '畢業滿_年']]

# 計算各系所的畢業人數，不考慮畢業年
grad_counts = organized_data.groupby(['Dept_Short', 'Edu_Short']).size().reset_index(name='畢業人數')

# 按照每個學制進行排序
sorted_grad_counts = grad_counts.sort_values(by=['Edu_Short', '畢業人數'], ascending=[True, False])

# 創建分組長條圖
fig = px.bar(sorted_grad_counts, 
                x='Dept_Short', 
                y='畢業人數', 
                color='Edu_Short',
                title='各系所畢業人數分布',
                labels={'畢業人數': '人數', 'Dept_Short': '系所', 'Edu_Short': '學制'},
                height=600, 
                width=1000)


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
    dcc.Graph(figure=fig)
])


    
