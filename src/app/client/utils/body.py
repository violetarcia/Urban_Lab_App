import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.client.components.map import map_graph, btn_variables, modal_variables
from app.client.components.barchart import barchart, dropdown_barchart, btn_barchart, modal_barchart
from app.client.components.treemap import treemap, dropdown_treemap

body = html.Div([
    html.Div([
        html.Div([
                dbc.Card(
                    [
                        btn_variables,
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
                    btn_barchart,
                    dropdown_barchart
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
                dropdown_treemap,
                treemap
            ],
                body=True,
                className='card h-100',
                style={'backgroundColor': '#F9F9F9'})
        ], className='col-12 col-sm-12 col-md-12 col-lg-12 col-xl-12')
    ], className='row mb-3'),
    modal_variables,
    modal_barchart
], className='container-fluid mr-1 ml-1 mb-auto', style={'backgroundColor': '#F2F2F2'})
