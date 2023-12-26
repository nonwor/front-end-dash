#archive

import dash
from dash import html

dash.register_page(
	__name__,
	path="/archive",
	title="archive",
	name="archive"
)

layout = html.Div([
	html.H1('This is our Archive page'),
	html.Div('This is our Archive page content...'),
])