import datetime
import requests
import time
import sys
import threading
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import dash

sys.path.append("..")


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
    args=("https://um.ac.ir", 5, 3),
    daemon=True
)
thread.start()


jumbotron_1 = html.Div(id='', className='p-1 m-1 bg-body-secondary rounded-3', children=[
    dbc.Container(id='jumbotron', className='py-2 border-top border-success border-5', fluid=True, children=[
        html.H1(id='connected_status', className='display-3 fw-bolder',
                children="Disconnected"),
        # html.P(id='', className='lead',
        #        children="Use Containers to create a jumbotron to call attention to featured content or information."),
        # html.Hr(id='', className='my-2', children=[]),
        html.P(id='time', className='lead display-5'),
        # html.P(id='', className='lead', children=[
        #     dbc.Button("Learn more", id='', color="primary")
        # ]),

    ])
])


cal = html.Div(id='', className='row justify-content-center', children=[
    html.Div(id='', className='box', children=[
        html.Div(id='', className='calendar', children=[
            html.Div(id='', className='year', children=[
                html.Div(id='', className='previous', children=[
                    html.P(id='', className='prevYear', children=[])                    
                ]),
                html.Div(id='', className='current', children=[
                    html.P(id='', className='currentYear', children=[]),
                    html.Span(id='', className='', children="Year")                   
                ]),
                html.Div(id='', className='next', children=[
                    html.P(id='', className='nextYear', children=[])                    
                ]),
            ]),
            html.Div(id='', className='month', children=[
                html.Div(id='', className='previous', children=[
                    html.P(id='', className='prevMonth', children=[])                    
                ]),
                html.Div(id='', className='current', children=[
                    html.P(id='', className='currentMonth', children=[]),
                    html.Span(id='', className='', children="Month")                   
                ]),
                html.Div(id='', className='next', children=[
                    html.P(id='', className='nextMonth', children=[])                    
                ]),
            ]),
            html.Div(id='', className='day', children=[
                html.Div(id='', className='previous', children=[
                    html.P(id='', className='prevDay', children=[])                    
                ]),
                html.Div(id='', className='current', children=[
                    html.P(id='', className='currentDay', children=[]),
                    html.Span(id='', className='', children="Day")                   
                ]),
                html.Div(id='', className='next', children=[
                    html.P(id='', className='nextDay', children=[])                    
                ]),
            ])
        ])        
    ])
])


layout = html.Div(
    id="page-content",
    children=[
        html.Div(id='', className='row', children=[
            html.Div(id='', className='col-sm-12 col-md-12 col-lg-6 p-1', children=[
                jumbotron_1
            ]),
            html.Div(id='', className='col-sm-12 col-md-12 col-lg-6 p-1', children=[
                cal
            ]),
        ]),
    ]
)


@callback(
    Output("connected_status", "children"),
    Output("connected_status", "className"),
    Output("jumbotron", "className"),
    Output("time", "children"),
    Input("interval", "n_intervals"),
)
def update_connection_status(n):
    return [
        'Connected!' if connected else 'Disconnected!',
        'display-3 fw-bolder text-success' if connected else 'display-3 fw-bolder text-danger',
        'py-2 border-top border-success border-5' if connected else 'py-2 border-top border-danger border-5',
        datetime.datetime.now().strftime("%H:%M:%S")
    ]


# @callback(Output("heatmaps-graph", "figure"), Input("heatmaps-medals", "value"))
# def filter_heatmap(cols):
#     fig = px.imshow(df[cols])
#     return fig
