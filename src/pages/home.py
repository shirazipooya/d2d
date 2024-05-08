import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import dash

dash.register_page(
    module=__name__,
    name="Home",
    path="/"
)


def jumbotron():
    return html.Div(
        dbc.Container(
            [
                html.H1("Jumbotron", className="display-3"),
                html.P(
                    "Use Containers to create a jumbotron to call attention to "
                    "featured content or information.",
                    className="lead",
                ),
                html.Hr(className="my-2"),
                html.P(
                    "Use utility classes for typography and spacing to suit the "
                    "larger container."
                ),
                html.P(
                    dbc.Button("Learn more", color="primary"), className="lead"
                ),
            ],
            fluid=True,
            className="py-3",
        ),
        className="p-1 m-1 bg-body-secondary rounded-3",
    )


def card():
    return html.Div([
        dbc.Card(
            [
                dbc.CardHeader("This is the header"),
                dbc.CardBody(
                    [
                        html.H4("Card title", className="card-title"),
                        html.P("This is some card text", className="card-text"),
                    ]
                ),
                dbc.CardFooter("This is the footer"),
            ],
        )
    ])


layout = html.Div(
    id="page-content",
    children=[
        html.Div(id='', className='row', children=[
            html.Div(id='', className='col-sm-12 col-md-12 col-lg-6', children=[
                jumbotron()
            ]),
            html.Div(id='', className='col-sm-12 col-md-12 col-lg-6', children=[
                jumbotron()
            ]),
        ]),
        html.Div(id='', className='row mt-2', children=[
            html.Div(id='', className='col-sm-12 col-md-12 col-lg-4 my-1', children=[
                card()
            ]),
            html.Div(id='', className='col-sm-12 col-md-12 col-lg-4 my-1', children=[
                card()
            ]),
            html.Div(id='', className='col-sm-12 col-md-12 col-lg-4 my-1', children=[
                card()
            ]),
        ])
    ]
)


# @callback(Output("heatmaps-graph", "figure"), Input("heatmaps-medals", "value"))
# def filter_heatmap(cols):
#     fig = px.imshow(df[cols])
#     return fig
