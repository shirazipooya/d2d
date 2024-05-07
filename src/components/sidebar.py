from dash import html
import dash_bootstrap_components as dbc

from src.pages import HOME_PAGE_URL, DOWNLOAD_PAGE_URL


sidebar_header = dbc.Row(
    [
        dbc.Col(html.H2("Sidebar", className="display-4")),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)



def sidebar():
    return html.Nav(
        className='sidebar active',
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
