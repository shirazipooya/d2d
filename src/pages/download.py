import dash
from dash import html

from src.app import r


dash.register_page(
    __name__,
    title='Download',
    name='Download',
)


layout = html.Div(
    [
        html.H1(f'Hello {r.get("name").decode()}!!!'),
        html.Div('Dash: A web application framework for Python.'),
    ]
)
