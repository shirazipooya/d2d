import os
import redis
from flask import Flask
import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML
from dotenv import load_dotenv

from src.components import sidebar, navbar


# Load Environment Variables
load_dotenv(".env")

# REDIS DB
r = redis.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"))


external_stylesheets = [
    "/static/vendor/fontawesome/v6.5.1/css/fontawesome.min.css",
    "/static/vendor/fontawesome/v6.5.1/css/solid.min.css",
    "/static/vendor/fontawesome/v6.5.1/css/brands.min.css",    
    "/static/vendor/bootstrap/v5.3.3/css/bootstrap.min.css",    
    "/static/css/master.css",    
    "/static/vendor/flagiconcss/css/flag-icon.min.css",    
    # "/static/vendor/bootstrap/v5.0.0-alpha1/css/bootstrap.min.css",
    # dbc.icons.BOOTSTRAP,
    # dbc.themes.FLATLY,
    # "/static/css/style.css",
    # dbc.themes.BOOTSTRAP,
    # dbc.icons.FONT_AWESOME,
]

external_scripts = [
    "/static/vendor/jquery/v3.7.1/jquery.min.js",
    "/static/vendor/popper/v2.11.8/popper.min.js",
    "/static/vendor/bootstrap/v5.3.3/js/bootstrap.min.js",
    "/static/js/script.js",
    # "/static/vendor/bootstrap/v5.0.0-alpha1/js/bootstrap.min.js",
    # "/static/js/main.js",
    # "/static/vendor/bootstrap/v5.3.3/js/bootstrap.min.js",
]


server = Flask(__name__)
app = Dash(
    __name__,
    server=server,
    use_pages=True,
    title='D2D Dashboard',
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts
)


def app_layout():
    return html.Div(
        className='wrapper',
        children=[
            sidebar.sidebar(),            
            html.Div(
                id="body",
                className='active',
                children=[
                    navbar.navbar(),
                    html.Div(className='col-md-9 ml-sm-auto col-lg-10 px-md-4 py-4', children=[
                        dash.page_container,
                    ])
                ]
            )
        ]
    )









# def app_layout():
#     return html.Div(className='container-fluid px-0', children=[
#         html.Nav(className='navbar navbar-light bg-light px-3 py-1', children=[
#             html.Div(className='d-flex col-12 col-md-3 col-lg-2 mb-2 mb-lg-0 flex-wrap flex-md-nowrap justify-content-between align-items-center', children=[
#                 html.H6(className='p-0 m-0 py-2 pl-3', children=["D2D Dashboard"]),
#                 DangerouslySetInnerHTML('''
#                     <button class="navbar-toggler d-md-none collapsed my-2" type="button" data-toggle="collapse" data-target="#sidebar" aria-controls="sidebar" aria-expanded="false" aria-label="Toggle navigation">
#                         <span class="navbar-toggler-icon"></span>
#                     </button>
#                 ''')
#             ])
#         ]),
#         html.Div(className='container-fluid', children=[
#             html.Div(className='row', children=[
#                 html.Nav(id='sidebar', className='col-md-3 col-lg-2 d-md-block bg-light sidebar collapse', children=[
#                     sidebar.sidebar()
#                 ]),
#                 html.Div(className='col-md-9 ml-sm-auto col-lg-10 px-md-4 py-4', children=[
#                     dash.page_container,
#                 ])
#             ])
#         ])
#     ])


app.layout = app_layout


if __name__ == '__main__':
    app.run_server()
