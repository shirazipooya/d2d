from dash import html
import dash_bootstrap_components as dbc

from src.pages import HOME_PAGE_URL, DOWNLOAD_PAGE_URL


def sidebar():
    return html.Div(className='position-sticky', children=[
        html.Ul(className='nav flex-column', children=[
            html.Li(className='nav-item', children=[
                dbc.NavLink(html.H5([html.I(className="bi bi-house me-2"), "Home"]), href=HOME_PAGE_URL, active="exact"),
            ]),
            html.Li(className='nav-item', children=[
                dbc.NavLink(html.H5([html.I(className="bi bi-cloud-arrow-down me-2"), "Download"]), href=DOWNLOAD_PAGE_URL, active="exact")
            ]),
        ])
    ])
