import datetime
import requests
import time
import sys
import threading
import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback
import dash_bootstrap_components as dbc
import dash
import jalali

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


jumbotron_1 = html.Div(id='', className='h-100 p-1 m-1', style={"background-color": "#F5F5F5"}, children=[
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


cal = html.Div(id='', className='h-100 p-1 m-1 justify-content-center ', children=[
    html.Div(id='', className='box', children=[
        html.Div(id='', className='calendar', children=[
            html.Div(id='', className='year', children=[
                html.Div(id='', className='previous', children=[
                    html.P(id='prevYear', className='', children=[])                    
                ]),
                html.Div(id='', className='current', children=[
                    html.P(id='currentYear', className='', children=[]),
                    html.Span(id='currentYearJ', className='', children=[])                   
                ]),
                html.Div(id='', className='next', children=[
                    html.P(id='nextYear', className='', children=[])                    
                ]),
            ]),
            html.Div(id='', className='month', children=[
                html.Div(id='', className='previous', children=[
                    html.P(id='prevMonth', className='', children=[])                    
                ]),
                html.Div(id='', className='current', children=[
                    html.P(id='currentMonth', className='', children=[]),
                    html.Span(id='currentMonthJ', className='', children=[])                   
                ]),
                html.Div(id='', className='next', children=[
                    html.P(id='nextMonth', className='', children=[])                    
                ]),
            ]),
            html.Div(id='', className='day', children=[
                html.Div(id='', className='previous', children=[
                    html.P(id='prevDay', className='', children=[])                    
                ]),
                html.Div(id='', className='current', children=[
                    html.P(id='currentDay', className='', children=[]),
                    html.Span(id='currentDayJ', className='', children=[])                   
                ]),
                html.Div(id='', className='next', children=[
                    html.P(id='nextDay', className='', children=[])                    
                ]),
            ])
        ])        
    ])
])


layout = html.Div(
    id="page-content",
    children=[
        html.Div(id='', className='row w-100', children=[
            html.Div(id='', className='col-sm-12 col-md-12 col-lg-4 p-1', children=[
                jumbotron_1
            ]),
            html.Div(id='', className='col-sm-12 col-md-12 col-lg-4 p-1', children=[
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
        'display-5 fw-bolder text-success' if connected else 'display-5 fw-bolder text-danger',
        'py-2 border-top border-success border-5' if connected else 'py-2 border-top border-danger border-5',
        datetime.datetime.now().strftime("%H:%M:%S")
    ]

@callback(
    Output("prevYear", "children"),
    Output("currentYear", "children"),
    Output("nextYear", "children"),
    Output("prevMonth", "children"),
    Output("currentMonth", "children"),
    Output("nextMonth", "children"),
    Output("prevDay", "children"),
    Output("currentDay", "children"),
    Output("nextDay", "children"),
    Output("currentYearJ", "children"),
    Output("currentMonthJ", "children"),
    Output("currentDayJ", "children"),
    Input("interval", "n_intervals"),
)
def update_calendar(n):
    today_date = datetime.datetime.now()
    today_date_j = jalali.Gregorian(f'{today_date.year},{today_date.month},{today_date.day}').persian_tuple()
    return [
        today_date.year - 1,
        today_date.year,
        today_date.year + 1,
        today_date.month - 1,
        today_date.month,
        today_date.month + 1,
        today_date.day - 1,
        today_date.day,
        today_date.day + 1,
        today_date_j[0],
        today_date_j[1],
        today_date_j[2],
    ]





# @callback(Output("heatmaps-graph", "figure"), Input("heatmaps-medals", "value"))
# def filter_heatmap(cols):
#     fig = px.imshow(df[cols])
#     return fig
