
import dash
from dash import Dash, Input, Output, callback, dash_table
import pandas as pd


dash.register_page(
    __name__,
    path='/table',
    title='table',
    name='table'
)

#Here we can try to make a request call to put api

df = pd.read_csv('http://127.0.0.1:5000/users/table')

layout = dash_table.DataTable(df.to_dict('records'), [{"name": i, "id": i} for i in df.columns])