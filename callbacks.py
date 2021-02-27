import dash_core_components as dcc
from dash.dependencies import Input, Output
from layouts import example_graph1, example_graph2
from app import app

import plotly.express as px

@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "active_tab"),
)
def render_tab_content(active_tab):
    """
    This callback takes the 'active_tab' property as input, and 
    renders the associated graph with the tab name on page 1.
    """
    if active_tab is not None:
        if active_tab == "graph1":
            return dcc.Graph(figure=example_graph1)
        elif active_tab == "graph2":
            return dcc.Graph(figure=example_graph2)
    return "No tab selected"

@app.callback(
    Output("selected-button","children"),
    Input("page2-buttons","value")
)
def button_choice(value):
    """
    This call takes in page2-buttons selected value and returns content to display
    in selected-button
    """
    return 'You have selected "{}"'.format(value)

@app.callback(
    Output("selected-dropdown","children"),
    Input("page2-dropdown","value")
)
def dropdown_choice(value):
    """
    This call takes in page2-dropdown's selected value and returns content to display
    in selected-button
    """
    return 'You have selected "{}"'.format(value)