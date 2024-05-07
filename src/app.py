import os
import redis
from flask import Flask
import dash
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc
from dash_dangerously_set_inner_html import DangerouslySetInnerHTML
from dotenv import load_dotenv

from src.components import sidebar


# Load Environment Variables
load_dotenv(".env")

# REDIS DB
r = redis.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"))


external_stylesheets = [
    "/static/vendor/fontawesome/v6.5.1/css/fontawesome.min.css",
    "/static/vendor/fontawesome/v6.5.1/css/solid.min.css",
    "/static/vendor/fontawesome/v6.5.1/css/brands.min.css",    
    "/static/vendor/bootstrap/v5.3.3/css/bootstrap.min.css",    
    "/static/css/style.css",
    # dbc.icons.BOOTSTRAP,
    # dbc.themes.FLATLY,
    # dbc.themes.BOOTSTRAP,
    # dbc.icons.FONT_AWESOME,
]

external_scripts = [
    "/static/vendor/jquery/v3.7.1/jquery.min.js",
    "/static/vendor/popper/v2.11.8/popper.min.js",
    "/static/vendor/bootstrap/v5.3.3/js/bootstrap.min.js",
    "/static/js/script.js",
]


server = Flask(__name__)

app = Dash(
    __name__,
    server=server,
    use_pages=True,
    pages_folder="pages",
    assets_folder="assets",
    assets_url_path="assets",
    title='D2D Dashboard',
    update_title="",
    suppress_callback_exceptions=True,
    external_stylesheets=external_stylesheets,
    external_scripts=external_scripts,
    meta_tags=[
        {
            "name": "viewport",
            "content": "width=device-width, initial-scale=1"
        }
    ],
)


def app_layout():
    return html.Div(
        children=[
            sidebar.sidebar(),
            dash.page_container,
        ]
    )


app.layout = app_layout


if __name__ == '__main__':
    app.run_server()
