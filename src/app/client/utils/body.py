import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from app.client.components.map import map_graph, output_container
from app.client.components.barchart1 import barchart1
from app.client.components.barchart2 import barchart2
from app.client.components.barchart3 import barchart3
from app.client.components.piechart1 import piechart1
from app.client.components.piechart2 import piechart2

body = html.Div([
    html.Div([
        html.Div([
                output_container,
                map_graph
                ], 
                className='col-12 col-sm-12 col-md-12 col-lg-6 col-xl-6 m-auto',
                style = {'height':'100%'}
            ),
        html.Div([
            html.Div([
                html.Div(
                    [barchart1],
                    className='col-12 col-sm-12 col-md-6 col-lg-12 col-xl-12 m-0 p-0',
                    style={'height': 'auto'}
                    ),
                html.Div(
                    [barchart2],
                    className='col-12 col-sm-12 col-md-6 col-lg-12 col-xl-12 m-0 p-0',
                    style={'height': 'auto'}
                    )
            ], className='row m-0 p-0')
        ], className='col-12 col-sm-12 col-md-12 col-lg-6 col-xl-6 m-auto')
    ], className='row'),
    html.Div([
        html.Div([
            barchart3
        ], className='col-12 col-sm-12 col-md-12 col-lg-12 col-xl-12'),
        html.Div([
            piechart1
        ], className='col-12 col-sm-12 col-md-6 col-lg-4 col-xl-4'),
        html.Div([
            piechart2
        ], className='col-12 col-sm-12 col-md-12 col-lg-4 col-xl-4')
    ], className='row')
], className='container-fluid mr-1 ml-1 mb-auto')
