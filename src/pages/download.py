import plotly.express as px
from dash import Dash, dcc, html, Input, Output, callback
import dash

dash.register_page(
    module=__name__,
    name="Download",
    path="/download"
)

df = px.data.tips()
days = df.day.unique()

layout = html.Div(
    id="page-content",
    children=[
        dcc.Dropdown(
            id="dropdown",
            options=[{"label": x, "value": x} for x in days],
            value=days[0],
            clearable=False,
        ),
        dcc.Graph(id="bar-chart"),
    ]
)


@callback(Output("bar-chart", "figure"), Input("dropdown", "value"))
def update_bar_chart(day):
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill",
                 color="smoker", barmode="group")
    return fig
