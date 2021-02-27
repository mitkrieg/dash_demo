import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app import app
import plotly.express as px
import plotly.graph_objects as go


#####################################
# Add your data
#####################################

#example iris dataset
df = px.data.iris()

#####################################
# Styles & Colors
#####################################

NAVBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

CONTENT_STYLE = {
    "top":0,
    "margin-left": "20rem",
    "margin-right": "2rem",
}

#####################################
# Create Components Here
#####################################

def nav_bar():
    """
    Creates Navigation bar
    """
    navbar = html.Div(
    [
        html.H4("System Performance Dashboard", className="display-10",style={'textAlign':'center'}),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Page 1", href="/page1",active="exact", external_link=True),
                dbc.NavLink("Page 2", href="/page2", active="exact", external_link=True)
            ],
            pills=True,
            vertical=True
        ),
    ],
    style=NAVBAR_STYLE,
    )
    
    return navbar

example_graph1 = px.scatter(df, x="sepal_length",y="sepal_width",color="species")

example_graph2 = px.histogram(df, x="sepal_length", color = "species",nbins=20)
example_graph2.update_layout(barmode='overlay')
example_graph2.update_traces(opacity=0.55)


#####################################
# Page Layouts
#####################################

### Layout 1
layout1 = html.Div([
    html.H2("Page 1"),
    html.Hr(),
    dbc.Container([
        dbc.Row(
            [
                dbc.Col(
                    [
                        html.Div(
                            [
                            html.H4('Example Graph Page'),
                            dbc.Tabs(
                                [
                                    dbc.Tab(label='graph1',tab_id='graph1'),
                                    dbc.Tab(label='graph2',tab_id='graph2')
                                ],
                                id="tabs",
                                active_tab='graph1',
                                ),
                            html.Div(id="tab-content",className="p-4")
                            ]
                        ),
                    ],
                    width=6 #half page
                ),
                
                dbc.Col(
                    [
                        html.H4('Additional Components here'),
                        html.P('Text Example')
                    ],
                    width=6 #half page
                )
                
            ],
        ), 
    ]),
])


### Layout 2
layout2 = html.Div(
    [
        dbc.Container(
            [
                dbc.Row(
                    [
                        dbc.Col(
                            [
                                html.H4('Country'),
                                html.Hr(),
                                dcc.Dropdown(
                                    id='page2-dropdown',
                                    options=[
                                        {'label': '{}'.format(i), 'value': i} for i in [
                                        'United States', 'Canada', 'Mexico'
                                        ]
        ]
                                ),
                                html.Div(id='selected-dropdown')
                            ],
                            width=6
                        ),
                        dbc.Col(
                            [
                                html.H4('Fruit'),
                                html.Hr(),
                                dcc.RadioItems(
                                    id='page2-buttons',
                                    options = [
                                        {'label':'{}'.format(i), 'value': i} for i in [
                                        'Yes', 'No', 'Maybe'
                                        ]
                                    ]
                                ),
                                html.Div(id='selected-button')
                            ],
                        )
                    ]
                ),
            ]
        )
    ])