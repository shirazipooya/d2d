import dash
from dash import html
import dash_mantine_components as dmc


from src.app import r


dash.register_page(
    __name__,
    title='Download',
    name='Download',
)


layout = html.Div(
    [
        # dmc.Tabs(
        #     [
        #         dmc.TabsList(
        #             position="left",
        #             grow=False,
        #             children=[
        #                 dmc.TabsTab("Meteomanz.com", value="gallery"),
        #                 dmc.TabsTab("Messages", value="messages"),
        #                 dmc.TabsTab("Settings", value="settings"),
        #             ]
        #         ),
        #         dmc.TabsPanel("Gallery tab content", className="py-3 px-1", value="gallery"),
        #         dmc.TabsPanel("Messages tab content", className="py-3 px-1", value="messages"),
        #         dmc.TabsPanel("Settings tab content", className="py-3 px-1", value="settings"),
        #     ],
        #     value="gallery",
        #     color="blue",
        #     orientation="horizontal",
        #     variant="default"
        # )
    ]
)
