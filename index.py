import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, server 
#import your navigation, styles and layouts from layouts.py here
from layouts import nav_bar, layout1, layout2, CONTENT_STYLE 
import callbacks

# Define basic structure of app:
# A horizontal navigation bar on the left side with page content on the right.
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    nav_bar(),
    html.Div(id='page-content',style=CONTENT_STYLE) #we'll use a callback to change the layout of this section 
])

# This callback changes the layout of the page based on the URL
# For each layout define a URL page "/pagename" and return the layout
@app.callback(Output('page-content', 'children'), #this changes the content
              [Input('url', 'pathname')]) #this listens for the url in use
def display_page(pathname):
    if pathname == '/':
        return layout1
    elif pathname == '/page1':
        return layout1
    elif pathname == '/page2':
         return layout2
    else:
        return '404' #If page not found return 404

#Runs the server      
if __name__ == '__main__':
    app.run_server(port=5000, host= '127.0.01',debug=True)