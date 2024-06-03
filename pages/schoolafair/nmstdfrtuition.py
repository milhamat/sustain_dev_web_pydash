import dash
import pandas as pd
import plotly.express as px
from dash import dcc, html
import matplotlib.pyplot as plt
import numpy as np

dash.register_page(__name__)

# x = np.random.normal(170, 10, 250)

# fig = plt.hist(x)
# fig = plt.show()



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
    html.H1("Still Under Construct"),
    # dcc.Graph(figure=fig)
])


    
 