import pandas as pd
import dash
from dash import callback, dcc, html, Input, Output, ctx, no_update
# from dash.dependencies import 
import plotly.express as px

dash.register_page(__name__)

all_option = {
    '中漢語' : ['學士班(日間)','五專','學士班(進修)','碩士班(日間)'],
    'English' : ["Bachelor's Degree (Daytime)","Five specialties","Bachelor's degree (further study)","Master's class (day time)"],
}

layout = html.Div([
    html.Div([
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
    
        dcc.RadioItems(id='lang_checklist', 
                       options=[{'label':k, 'value':k} for k in all_option.keys()],
                       value="中漢語",
                       labelStyle={"margin":"0.2rem"},
                       inline=True,
                       style={
                            # 'marginBottom':"20px",
                            'marginLeft':"85%",
                            }
                    ),
        
    ], style={
        'display' : "flex",
    }),
    
    dcc.Tabs(id="tabs-intern", value='tab-110', children=[
        dcc.Tab(label='110學年度', value='tab-110'),
        dcc.Tab(label='111學年度', value='tab-111'),
    ]),
    
    html.Div([
        dcc.Checklist(
            id='checklist-intern',
            # options=checklist_options,
            value=[],#[checklist_options[0]['value']] ,
            labelStyle={"margin":"0.2rem"},
            inline=True,
            style = {
                 'marginTop':"10px"
             }
        )
    ]),
    
    html.Div(id='tabs-content-intern')
])

########################################################################
@callback(
    Output('checklist-intern', 'options'),
    Input('lang_checklist', 'value')
)

def set_lang(select):
    if not select:
        return no_update
    else:
        return [{'label': i, 'value': i} for i in all_option[select]]
########################################################################
@callback(
    Output('tabs-content-intern', 'children'),
    [Input('lang_checklist','value'),
     Input('tabs-intern', 'value'),
     Input('checklist-intern', 'value')],
)

def render_content(select, tab, selected_classes):
    if select == "English":
        df = pd.read_excel('./datas/std_intern_eng.xlsx')
        df_110 = df[df['Academic Year'] == 110]
        df_111 = df[df['Academic Year'] == 111]
            
        if tab == 'tab-110':
            filtered_df = df_110[df_110['Academic Class'].isin(selected_classes)]  # Academic class
            pivot_table = filtered_df.pivot_table(index='Academic Class', columns='Department Name', values='Total Internship Hours', aggfunc='sum').reset_index()
            melted_df = pivot_table.melt(id_vars='Academic Class', var_name='Department Name', value_name='Total Internship Hours')

            # Sort the data by Total Internship Hours
            melted_df = melted_df.sort_values(by='Total Internship Hours', ascending=True)

            fig = px.bar(melted_df,
                        x='Academic Class', y='Total Internship Hours', color='Department Name', barmode='group',
                        title=f'110 Academic Year {", ".join(selected_classes)} Total number of hours of internships in the name of each department',
                        color_discrete_sequence=px.colors.qualitative.Plotly)
                
        elif tab == 'tab-111':
            filtered_df = df_111[df_111['Academic Class'].isin(selected_classes)]
            pivot_table = filtered_df.pivot_table(index='Academic Class', columns='Department Name', values='Total Internship Hours', aggfunc='sum').reset_index()
            melted_df = pivot_table.melt(id_vars='Academic Class', var_name='Department Name', value_name='Total Internship Hours')

            # Sort the data by Total Internship Hours
            melted_df = melted_df.sort_values(by='Total Internship Hours', ascending=True)

            fig = px.bar(melted_df,
                        x='Academic Class', y='Total Internship Hours', color='Department Name', barmode='group',
                        title=f'111 Academic Year {", ".join(selected_classes)} Total number of hours of internships in the name of each department',
                        color_discrete_sequence=px.colors.qualitative.Plotly)

            # Add vertical lines to separate different academic classes
            fig.update_layout(
                shapes=[
                    dict(
                        type="line",
                        x0=i - 0.5,
                        x1=i - 0.5,
                        y0=0,
                        y1=1,
                        xref='x',
                        yref='paper',
                        line=dict(color="Black", width=1, dash="dot")
                    ) for i in range(1, len(pivot_table['Academic Class'].unique()))
                ]
            )
    
    else:
        df = pd.read_excel('./datas/std_intern.xlsx') 
        df_110 = df[df['學年度'] == 110]
        df_111 = df[df['學年度'] == 111]
        
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
#########################################################################

