#Analytics.py

import dash
from dash import Dash, dcc, html, Input, Output, State, callback
import requests

dash.register_page(
    __name__,
    path='/analytics-dashboard',
    title='Our analytics dashboard',
    name='Our analytics dashboard'
)

layout = html.Div([
    html.H1('This is our analytics page'),
    html.Div([
        "Select a city: ",
        dcc.RadioItems(
            options=["New York City", "Montreal","San Francisco"],
            value="Montreal",
            id='analytics-input'
        )

    ]),
    html.Br(),
    html.Div(id="analytics-output"),
    html.Br(),
    html.Br(),
    html.Div(dcc.Input(id='input-on-submit', type='text')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
])

@callback(
    Output('analytics-output','children'),
    Input('analytics-input','value')
)

def update_city_selected(input_value):

    return f'you selected:{input_value}'


@callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value'),
    prevent_initial_call=True
)

def get_api(n_clicks, value):
    if value == None:
        return("Please provide input")
    print(type(value),value)

    # api_endpoint = 'https://swapi.dev/api/people/'+value
    api_endpoint = "http://127.0.0.1:5000/user/" + value

    try: 
        response = requests.get(api_endpoint)

        if response.status_code == 200:
            # data = response.json()
            # print(data['name'])
            # return(data['name'])
            print(response.text)
            return(response.text)
        else:
            #Handle Data error
            print(response.text)
            print(response.status_code)
            return("API ERROR")
    except Exception as e:
        print(e)



