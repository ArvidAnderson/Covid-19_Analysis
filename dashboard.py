#Imports
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px # remove ?
import json # remove ?
from get import * #My own library for grabbing data from all the files.

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

# Used for styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

#Positioning the main content and adding padding
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

#Sidebar content
sidebar = html.Div(
    [
        html.H2("Covid-19 Analysis", className="display-4"),
        html.Hr(),
        html.P(
            "Arvid Anderson TE19D", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Regional Map", href="/map", active="exact"),
                dbc.NavLink("Age Groups", href="/age", active="exact"),
                dbc.NavLink("Page 1", href="/page-1", active="exact"),
                dbc.NavLink("Page 2", href="/page-2", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

#Creates content div
content = html.Div(id="page-content", style=CONTENT_STYLE)

#Setting the app layout, on url change content in the middle changes
app.layout = html.Div([dcc.Location(id="url"), sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        HomePage = html.Div([
            html.H1('DANK')
        ])
        return HomePage 
    elif pathname == "/map":
        REGIONALMAP_STYLE = {
            "width": "100%",
            "height": "100%",
        }
        RegionalMapLayout = html.Div(
            [
                dcc.Graph(figure=RegionalMap),
            ],
            style=REGIONALMAP_STYLE
        )
        return RegionalMapLayout
    elif pathname == "/age":
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
                            dbc.ListGroup(
                                [
                                    dbc.ListGroupItem(f"Total Cases: {TotalCasesByAgeGroup('40-49')}"),
                                    dbc.ListGroupItem(f"Total ICU: {TotalICUByAgeGroup('40-49')}"),
                                    dbc.ListGroupItem(f"Total Deaths: {TotalDeathsByAgeGroup('40-49')}"),
                                ]
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Age 50-59", className="card-title"),
                            dbc.ListGroup(
                                [
                                    dbc.ListGroupItem(f"Total Cases: {TotalCasesByAgeGroup('50-59')}"),
                                    dbc.ListGroupItem(f"Total ICU: {TotalICUByAgeGroup('50-59')}"),
                                    dbc.ListGroupItem(f"Total Deaths: {TotalDeathsByAgeGroup('50-59')}"),
                                ]
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Age 60-69", className="card-title"),
                            dbc.ListGroup(
                                [
                                    dbc.ListGroupItem(f"Total Cases: {TotalCasesByAgeGroup('60-69')}"),
                                    dbc.ListGroupItem(f"Total ICU: {TotalICUByAgeGroup('60-69')}"),
                                    dbc.ListGroupItem(f"Total Deaths: {TotalDeathsByAgeGroup('60-69')}"),
                                ]
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Age 70-79", className="card-title"),
                            dbc.ListGroup(
                                [
                                    dbc.ListGroupItem(f"Total Cases: {TotalCasesByAgeGroup('70-79')}"),
                                    dbc.ListGroupItem(f"Total ICU: {TotalICUByAgeGroup('70-79')}"),
                                    dbc.ListGroupItem(f"Total Deaths: {TotalDeathsByAgeGroup('70-79')}"),
                                ]
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Age 80-89", className="card-title"),
                            dbc.ListGroup(
                                [
                                    dbc.ListGroupItem(f"Total Cases: {TotalCasesByAgeGroup('80-89')}"),
                                    dbc.ListGroupItem(f"Total ICU: {TotalICUByAgeGroup('80-89')}"),
                                    dbc.ListGroupItem(f"Total Deaths: {TotalDeathsByAgeGroup('80-89')}"),
                                ]
                            ),
                        ]
                    )
                ),
                dbc.Card(
                    dbc.CardBody(
                        [
                            html.H5("Age 90+", className="card-title"),
                            dbc.ListGroup(
                                [
                                    dbc.ListGroupItem(f"Total Cases: {TotalCasesByAgeGroup('90+')}"),
                                    dbc.ListGroupItem(f"Total ICU: {TotalICUByAgeGroup('90+')}"),
                                    dbc.ListGroupItem(f"Total Deaths: {TotalDeathsByAgeGroup('90+')}"),
                                ]
                            ),
                        ]
                    )
                ),
            ]
        )
        TABS_STYLE = {
            "margin-top": "15px",
        }
        tab1_content = dbc.Card(
            dbc.CardBody(
                [
                    dcc.Graph(figure=AgeTotalCasesFig),
                ]
            ),
            className="mt-3",
        )

        tab2_content = dbc.Card(
            dbc.CardBody(
                [
                    dcc.Graph(figure=AgeTotalICUFig),
                ]
            ),
            className="mt-3",
        )
        tab3_content = dbc.Card(
            dbc.CardBody(
                [
                    dcc.Graph(figure=AgeTotalDeathsFig),
                ]
            ),
            className="mt-3",
        )


        tabs = dbc.Tabs(
            [
                dbc.Tab(label="Graphs", disabled="true"),
                dbc.Tab(tab1_content, label="Total Cases",),
                dbc.Tab(tab2_content, label="ICU"),
                dbc.Tab(tab3_content, label="Deaths"),
            ],
            active_tab="",
            style = TABS_STYLE,
        )
        return cards, tabs
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