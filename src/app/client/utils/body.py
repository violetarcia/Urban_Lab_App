import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.client.components.map import map_graph, output_container, modal
from app.client.components.barchart import barchart, dropdown2
from app.client.components.treemap import treemap, dropdown3

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
                dropdown2,
                barchart
            ],
                body=True,
                className='card h-100',
                style={'backgroundColor': '#F9F9F9'})
        ], className='col-12 col-sm-12 col-md-12 col-lg-6 col-xl-6')
    ], className='row mt-3 mb-3'),
    html.Div([
        html.Div([
            dbc.Card([
                dropdown3,
                treemap
            ],
                body=True,
                className='card h-100',
                style={'backgroundColor': '#F9F9F9'})
        ], className='col-12 col-sm-12 col-md-12 col-lg-12 col-xl-12')
    ], className='row mb-3'),
    modal
], className='container-fluid mr-1 ml-1 mb-auto', style={'backgroundColor': '#F2F2F2'})
