import dash
from dash import html


dash.register_page(
    __name__,
    title='Home',
    name='Home',
    path='/',
)


layout = html.Div(
    [
        html.H1('Hello Home Page!!!'),
        html.Div('Dash: A web application framework for Python.'),
    ]
)
