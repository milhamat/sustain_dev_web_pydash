import dash
import pandas as pd
# import plotly.express as px
from dash import dcc, html
import plotly.graph_objects as go

dash.register_page(__name__)

file_path = './datas/freetuition.csv'
df = pd.read_csv(file_path)

# Process the data
years = df['學年度'].unique()
data = {year: {} for year in years}

for index, row in df.iterrows():
    year = row['學年度']
    for column in df.columns[6:]:
        category = column.replace('學雜費減免人數-', '')
        if category not in data[year]:
            data[year][category] = 0
        data[year][category] += row[column]

for year in years:
    data[year] = dict(sorted(data[year].items(), key=lambda x: x[1]))

# Create the Plotly bar chart
fig = go.Figure()

bar_width = 0.15
index = list(range(len(years)))

for i, category in enumerate(data[years[0]].keys()):
    fig.add_trace(go.Bar(
        x=[x + i * bar_width for x in index],
        y=[data[year][category] for year in years],
        name=category,
        text=[data[year][category] for year in years],
        textposition='auto'
    ))

# Update the layout
fig.update_layout(
    # title='不同學年度的學雜費減免人數',
    xaxis=dict(
        title='學年度',
        tickvals=[r + bar_width * ((len(data[years[0]]) - 1) / 2) for r in range(len(years))],
        ticktext=years
    ),
    yaxis=dict(
        title='減免人數'
    ),
    barmode='group',
    legend=dict(
        title='類別',
        x=1.05,
        y=1,
        xanchor='left',
        yanchor='top'
    ),
    margin=dict(t=40, b=40, l=40, r=40),
    width=800,
    height=600
)


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
    html.H2("不同學年度的學雜費減免人數"),
    
    dcc.Graph(figure=fig),
    html.P("Teamwork by Sandy, Emily, Debbie, and Ilham , directed by Prof. Ching-Shih Tsou. All rights reserved",
               style={
                   'marginTop' : "10px",
                   'textAlign' : "center",
                   }),
])


    
 