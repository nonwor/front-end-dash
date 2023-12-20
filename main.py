#main.py
from dash import Dash, html, dcc, callback, Output, Input
import page1
import page2

app = Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page1.layout
    elif pathname == '/page-2':
        return page2.layout
    else:
        return '404 Page Not Found'

if __name__ == '__main__':
    app.run_server(debug=True)