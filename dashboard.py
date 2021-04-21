import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from get import *
print(TotalCasesByAgeGroup('10-19'))
#My own functions needed to display data.
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# the style arguments for the sidebar. We use position:fixed and a fixed width
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# the styles for the main content position it to the right of the sidebar and
# add some padding.
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Covid-19 Analysis", className="display-4"),
        html.Hr(),
        html.P(
            "Dashboard for easily viewing the statistics of the current situation", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        cards = dbc.CardGroup(
            [
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Age 0-9", className="card-title"),
                            dbc.ListGroup(
                                [
                                    dbc.ListGroupItem(f"Total Cases: {TotalCasesByAgeGroup('0-9')}"),
                                    dbc.ListGroupItem(f"Total ICU: {TotalICUByAgeGroup('0-9')}"),
                                    dbc.ListGroupItem(f"Total Deaths: {TotalDeathsByAgeGroup('0-9')}"),
                                ]
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Age 10-19", className="card-title"),
                            dbc.ListGroup(
                                [
                                    dbc.ListGroupItem(f"Total Cases: {TotalCasesByAgeGroup('10-19')}"),
                                    dbc.ListGroupItem(f"Total ICU: {TotalICUByAgeGroup('10-19')}"),
                                    dbc.ListGroupItem(f"Total Deaths: {TotalDeathsByAgeGroup('10-19')}"),
                                ]
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Age 20-29", className="card-title"),
                            dbc.ListGroup(
                                [
                                    dbc.ListGroupItem(f"Total Cases: {TotalCasesByAgeGroup('20-29')}"),
                                    dbc.ListGroupItem(f"Total ICU: {TotalICUByAgeGroup('20-29')}"),
                                    dbc.ListGroupItem(f"Total Deaths: {TotalDeathsByAgeGroup('20-29')}"),
                                ]
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Age 30-39", className="card-title"),
                            dbc.ListGroup(
                                [
                                    dbc.ListGroupItem(f"Total Cases: {TotalCasesByAgeGroup('30-39')}"),
                                    dbc.ListGroupItem(f"Total ICU: {TotalICUByAgeGroup('30-39')}"),
                                    dbc.ListGroupItem(f"Total Deaths: {TotalDeathsByAgeGroup('30-39')}"),
                                ]
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Age 40-49", className="card-title"),
                            html.P(
                                "This card has some text content, which is longer "
                                "than both of the other two cards, in order to "
                                "demonstrate the equal height property of cards in a "
                                "card group.",
                                className="card-text",
                            ),
                            dbc.Button(
                                "Click here", color="danger", className="mt-auto"
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Age 50-59", className="card-title"),
                            html.P(
                                "This card has some text content, which is longer "
                                "than both of the other two cards, in order to "
                                "demonstrate the equal height property of cards in a "
                                "card group.",
                                className="card-text",
                            ),
                            dbc.Button(
                                "Click here", color="danger", className="mt-auto"
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Age 60-69", className="card-title"),
                            html.P(
                                "This card has some text content, which is longer "
                                "than both of the other two cards, in order to "
                                "demonstrate the equal height property of cards in a "
                                "card group.",
                                className="card-text",
                            ),
                            dbc.Button(
                                "Click here", color="danger", className="mt-auto"
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Age 70-79", className="card-title"),
                            html.P(
                                "This card has some text content, which is longer "
                                "than both of the other two cards, in order to "
                                "demonstrate the equal height property of cards in a "
                                "card group.",
                                className="card-text",
                            ),
                            dbc.Button(
                                "Click here", color="danger", className="mt-auto"
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Age 80-89", className="card-title"),
                            html.P(
                                "This card has some text content, which is longer "
                                "than both of the other two cards, in order to "
                                "demonstrate the equal height property of cards in a "
                                "card group.",
                                className="card-text",
                            ),
                            dbc.Button(
                                "Click here", color="danger", className="mt-auto"
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Age 90+", className="card-title"),
                            html.P(
                                "This card has some text content, which is longer "
                                "than both of the other two cards, in order to "
                                "demonstrate the equal height property of cards in a "
                                "card group.",
                                className="card-text",
                            ),
                            dbc.Button(
                                "Click here", color="danger", className="mt-auto"
                            ),
                        ]
                    )
                ),
            ]
        )
        return cards
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == "__main__":
    app.run_server(port=8888)