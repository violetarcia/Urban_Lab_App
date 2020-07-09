import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.client.components.map import map_graph, txt_variables
from app.client.components.barchart import barchart, txt_barchart, output_barchart
from app.client.components.treemap import treemap, tabs_barchart

body = html.Div([
    html.Div([
        html.Div([
                dbc.Card(
                    [
                       txt_variables, 
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
                html.Div([
                    txt_barchart,
                    output_barchart
                ]),
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
                tabs_barchart,
                treemap
            ],
                body=True,
                className='card h-100',
                style={'backgroundColor': '#F9F9F9'})
        ], className='col-12 col-sm-12 col-md-12 col-lg-12 col-xl-12')
    ], className='row mb-3')
], className='container-fluid mr-1 ml-1 mb-auto', style={'backgroundColor': '#F2F2F2'})
