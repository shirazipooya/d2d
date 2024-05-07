from dash import html
import dash_bootstrap_components as dbc

from src.pages import HOME_PAGE_URL, DOWNLOAD_PAGE_URL




def sidebar():
    return html.Nav(
        id='sidebar',
        className='active',
        children=[
            html.Div(
                className="sidebar-header",
                children=[
                    html.Img(
                        src="assets/img/bootstraper-logo.png",
                        className="app-logo"
                    )
                ]
            ),
            html.Ul(
                className="list-unstyled components text-secondary",
                children=[
                    html.Li(
                        children=[
                            html.A(
                                href=HOME_PAGE_URL,
                                children=[
                                    html.I(
                                        className="fas fa-home"
                                    ),
                                    "Dashboard"
                                ]
                            )
                        ]
                    )
                ]
            )
        ]
    )
    
    

# def sidebar():
#     return html.Div(className='position-sticky', children=[
#         html.Ul(className='nav flex-column', children=[
#             html.Li(className='nav-item', children=[
#                 dbc.NavLink(html.H6([html.I(className="bi bi-house me-2"), "Home"]), href=HOME_PAGE_URL, active="exact"),
#             ]),
#             html.Li(className='nav-item', children=[
#                 dbc.NavLink(html.H6([html.I(className="bi bi-cloud-arrow-down me-2"), "Download"]), href=DOWNLOAD_PAGE_URL, active="exact")
#             ]),
#         ])
#     ])
