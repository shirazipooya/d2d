import sys
import threading
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import dash

sys.path.append("..")

import time
import requests


connected = False
connected_status = "Disconnected"


def check_network_connection_status(url="https://um.ac.ir", timeout=5):
    global connected
    global connected_status
    try:
        requests.get(url=url, timeout=timeout)
        connected = True
        connected_status = "Connected"
    except (requests.ConnectionError, requests.Timeout):
        connected = False
        connected_status = "Disconnected"

def run_check_network_connection_status(url="https://um.ac.ir", timeout=5, seconds=5):
    while True:
        check_network_connection_status(url=url, timeout=timeout)
        time.sleep(seconds)

dash.register_page(
    module=__name__,
    name="Home",
    path="/"
)


thread = threading.Thread(
    target=run_check_network_connection_status,
    args=("https://um.ac.ir", 5, 5),
    daemon=True
)
thread.start()


jumbotron_1 = html.Div(id='', className='p-1 m-1 bg-body-secondary rounded-3', children=[
    dbc.Container(id='', className='py-2', fluid=True, children=[
        html.H1(id='connected_status', className='display-3', children="Disconnected"),
        html.P(id='', className='lead', children="Use Containers to create a jumbotron to call attention to featured content or information."),
        html.Hr(id='', className='my-2', children=[]),
        html.P(id='time', className='lead display-5'),
        html.P(id='', className='lead', children=[
            dbc.Button("Learn more", id='', color="primary")            
        ]),
        
    ])
])


layout = html.Div(
    id="page-content",
    children=[
        dcc.Interval(
            id='interval-component-home',
            interval=1 * 1000,
            n_intervals=0
        ),
        html.Div(id='', className='row', children=[
            html.Div(id='', className='col-sm-12 col-md-12 col-lg-6', children=[
                jumbotron_1
            ]),
        ]),
    ]
)


import datetime

@callback(
    Output("connected_status", "children"),
    Output("time", "children"),
    Input("interval-component-home", "n_intervals"),
)
def update_connection_status(n):
    return [
        "Connected!" if connected else "Disconnected!",
        datetime.datetime.now().strftime("%H:%M:%S")
    ]


# @callback(Output("heatmaps-graph", "figure"), Input("heatmaps-medals", "value"))
# def filter_heatmap(cols):
#     fig = px.imshow(df[cols])
#     return fig
