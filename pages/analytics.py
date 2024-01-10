#Analytics.py

import dash
from dash import Dash, dcc, html, Input, Output, State, callback
import requests
import json

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
    dcc.Input(id='input-1', type='text', value=''),
    dcc.Input(id='input-2', type='text', value=''),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
])

@callback(
    Output('analytics-output','children'),
    Input('analytics-input','value')
)

def update_city_selected(input_value):

    return f'you selected:{input_value}'


# @callback(
#     Output('container-button-basic', 'children'),
#     # Input('submit-val', 'n_clicks'),
#     [Input('input-1', 'value-1'),
# 	 Input('input-2', 'value-2')],
#     State('input-on-submit', 'value'),
#     prevent_initial_call=True
# )
@callback(
    Output('container-button-basic', 'children'),
    Input('submit-button', 'n_clicks'),
    State('input-1', 'value'),
    State('input-2', 'value'),
    prevent_initial_call=True
)

def get_api(n_clicks, input1_value, input2_value):
    # if value == None:
    #     return("Please provide input")
    print(input1_value, input2_value)


    url = "http://127.0.0.1:5000/user"
    headers = {"Content-Type": "application/json"}
    payload = {"name": input1_value, "email": input2_value}
    json_string = json.dumps(payload)

    userOBJ = {}
    try:
        response = requests.get(url, headers=headers, data=json_string)
        print(response.status_code)
        print(response.text)
        print(type(response.text))
        userOBJ = json.loads(response.text)
        
    except:
        print("server error")
        return("cannot find user")

    return("User ID = ", userOBJ['id'])




