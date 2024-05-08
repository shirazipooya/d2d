import dash
from flask import Flask
from dash import Input, Output, State, html, dcc
import dash_bootstrap_components as dbc


external_stylesheets = [
    dbc.themes.BOOTSTRAP,
    "/static/vendor/fontawesome/v6.5.1/css/fontawesome.min.css",
    "/static/vendor/fontawesome/v6.5.1/css/solid.min.css",
    "/static/vendor/fontawesome/v6.5.1/css/brands.min.css",
    "/static/vendor/bootstrap/v5.3.3/css/bootstrap.min.css",
    "/static/css/style.css",
]

external_scripts = [
    "/static/vendor/jquery/v3.7.1/jquery.min.js",
    "/static/vendor/popper/v2.11.8/popper.min.js",
    "/static/vendor/bootstrap/v5.3.3/js/bootstrap.min.js",
    "/static/js/script.js",
]


server = Flask(__name__)


app = dash.Dash(
    name=__name__,
    server=server,
    use_pages=True,
    pages_folder="pages",
    assets_folder="assets",
    assets_url_path="assets",
    title='D2D Dashboard',
    # update_title="",
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


sidebar_header = dbc.Row(
    [
        dbc.Col(
            html.H5(
                "Pooya's Dashboard",
            ),
            style={"text-align": "center"}
        ),
        dbc.Col(
            [
                html.Button(
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="navbar-toggle",
                ),
            ],
            width="auto",
            align="center",
        ),
    ],
)

sidebar = html.Div(
    [
        sidebar_header,
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink(page["name"], href=page["path"], active="exact")
                    for page in dash.page_registry.values()
                    if page["module"] != "pages.404"
                ],
                vertical=True,
                pills=True,
                className="my-0 py-0"
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
)


app.layout = html.Div(
    children=[
        dcc.Store(id="store", data={}),
        dcc.Interval(id='interval', interval=1 * 1000, n_intervals=0),
        sidebar,
        dash.page_container
    ],
)


@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(
        debug=True
    )
    