import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.client.components.map import map_graph, output_container
from app.client.components.barchart1 import barchart1
from app.client.components.barchart2 import barchart2, dropdown
from app.client.components.barchart3 import barchart3
from app.client.components.piechart1 import piechart1
from app.client.components.piechart2 import piechart2

body = html.Div([
    html.Div([
        html.Div([
                dbc.Card(
                    [
                        output_container,
                            map_graph
                    ],
                    body=True,
                    className='card h-100 ',
                    style={'backgroundColor': '#F9F9F9'})
                ],
            className='col-12 col-sm-12 col-md-12 col-lg-6 col-xl-6',
        ),
        html.Div([
            dbc.Card([
                dropdown,
                barchart2
            ],
            body=True,
            className='card h-100',
            style={'backgroundColor': '#F9F9F9'})
        ], className='col-12 col-sm-12 col-md-12 col-lg-6 col-xl-6')
    ], className='row mt-3 mb-3'),
    html.Div([
        html.Div([
            dbc.Card([
                barchart3
            ],
            body=True,
            className='card h-100',
            style={'backgroundColor': '#F9F9F9'})
        ], className='col-12 col-sm-12 col-md-12 col-lg-12 col-xl-12')
    ], className='row mb-3')
], className='container-fluid mr-1 ml-1 mb-auto', style={'backgroundColor': '#F2F2F2'})

