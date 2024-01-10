from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd 

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv')

app = Dash(__name__)

#
var_selected = ["",""]

app.layout = html.Div([
	html.H1(children='Hello World Dash', style={'textAlign':'center'}),
	dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection-1'),
	dcc.Graph(id='graph-content-1'),
	dcc.Dropdown(df.country.unique(), 'Canada', id='dropdown-selection-2'),
	dcc.Graph(id='graph-content-2'),
	# This is how you do multi-input callback
	dcc.Input(id='input-1', type='text', value='1'),
	dcc.Input(id='input-2', type='text', value='1'),
	html.Div(id='output')
])

@callback(
	Output('graph-content-1', 'figure'),
	Input('dropdown-selection-1', 'value')
)

# Update_graph is associated with the callback function "value"
def update_graph(value):
	dff = df[df.country==value]
	# print("value:", value)
	var_selected[0]=value
	print("current value:", var_selected)
	return px.line(dff,x='year', y='pop')

@callback(
	Output('graph-content-2', 'figure'),
	Input('dropdown-selection-2', 'value')
)

def update_graph2(value):
	dff = df[df.country==value]
	print("value:", value)
	var_selected[1] = value
	print("current value:", var_selected)
	return px.line(dff,x='year', y='pop')

@callback(
	Output('output', 'children'),
	[Input('input-1', 'value'),
	 Input('input-2', 'value')]
)
def update_output(input1, input2):
	# return f'Input 1: {input1}, Input 2: {input2}'
	# Watch out for type casting with str input and str output
	firstInput = 0
	secondInput = 0
	# print(type(input1), type(input2))
	try:
		firstInput = int(input1)
	except:
		print("first input is not a number")

	try:
		secondInput = int(input2)
	except:
		print("second input is not a number")

	return str(firstInput + secondInput)

if __name__ == '__main__':
	app.run(debug=True)