import dash
import pandas as pd
from dash import dcc, html, Input, Output, callback
import plotly.express as px

# url = 'https://raw.githubusercontent.com/milhamat/NtubDashboardDatas/main/libraryresources.csv'
# df = pd.read_csv(url)

# df = pd.read_csv('./datas/libraryresources.csv')

df = pd.read_parquet('./datas/libraryresources.parquet')

dash.register_page(__name__)

# 將列轉為行(Pivot columns into rows)
df_melted = df.melt(id_vars=['學年度'], var_name='館藏類型', value_name='數量')

# 分割館藏類型為大標題和子分類，對特定標題設置子分類為空白 (Split the collection type into main category and subcategory, set subcategory to blank for specific titles)
df_melted['大標題'] = df_melted['館藏類型'].apply(lambda x: x.split('-')[0] if '-' in x else x)  # '大標題' is 'Main Category'
df_melted['子分類'] = df_melted['館藏類型'].apply(lambda x: x.split('-')[1] if '-' in x else '')  # '子分類' is 'Subcategory'

# 將特定的沒有子分類的大標題子分類設置為空白 (Set subcategory to blank for main categories without a subcategory)
no_subcategory_titles = ['外文紙本圖書', '期刊合訂本(冊)', '視聽資料(件)']
df_melted.loc[df_melted['大標題'].isin(no_subcategory_titles), '子分類'] = ''

# 應用佈局(Application layout)
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
        id='yrlib-dropdown',
        options=[{'label': year, 'value': year} for year in df['學年度'].unique()],# '學年度' is 'Academic Year'
        value=df['學年度'].unique()[0]
    ),
    dcc.Graph(id='sblib-chart', style={
                'height':"450px",
                'marginTop':"20px",}),
])

# 回調函數，更新旭日圖 (Callback function to update the sunburst chart)
@callback(
    Output('sblib-chart', 'figure'),
    Input('yrlib-dropdown', 'value')
)
def update_chart(selected_year):
    filtered_df = df_melted[df_melted['學年度'] == selected_year]
    category_counts = filtered_df.groupby(['大標題', '子分類']).sum().reset_index()

    fig = px.sunburst(
        category_counts,
        path=['大標題', '子分類'],  # '大標題' is 'Main Category', '子分類' is 'Subcategory'
        values='數量',  # '數量' is 'Quantity'
        title=f'{selected_year} 學年度圖書館館藏分類',  # '學年度圖書館館藏分類' is 'Academic Year Library Collection Classification'
        color_discrete_sequence=px.colors.qualitative.Pastel
    )
    fig.update_layout(
        margin = dict(t=30, l=25, r=25, b=10)
    )
    return fig