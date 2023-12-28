#Home
import dash
from dash import html

dash.register_page(__name__, path='/')

layout = html.Div([
	html.H1("Welcome to the home page!"),
	html.Div('This is our home page content...'),
])