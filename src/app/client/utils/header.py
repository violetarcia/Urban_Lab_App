import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app.dash import app
from config.config import name


header = html.Header(
    children=[
        dbc.Nav(
            html.Div([
                html.Div([
                    html.Div([
                        html.Div([
                            html.Img(
                                src=app.get_asset_url('logo.png'),
                                height='40px',
                                className='mr-3'),
                            html.H4(
                                name,
                                className='m-auto text-primary font-weight-bold')
                        ], className='d-flex flex-row')
                    ], className='col-12 col-sm-12 col-md-8 col-lg-8 col-xl-8'),
                    html.Div([
                        dcc.Dropdown(
                            id='slct_map',
                            options=[
                                {'label': 'Estrés Económico',
                                    'value': 'Estres'},
                                {'label': 'Adaptabilidad',
                                    'value': 'Adaptabilidad'},
                                {'label': 'Predicción de Precios',
                                    'value': 'Precios'}
                            ],
                            multi=False,
                            clearable=False,
                            value='Estres',
                            style={
                                'color': '#272E42',
                                'background-color': '#D1D8EE',
                                'fontSize': '20px'
                            },
                            className='w-100 h-100 m-auto')
                    ], className='col-12 col-sm-12 col-md-4 col-lg-4 col-xl-4 m-0 p-0')
                ], className='row w-100 m-0 p-0')
            ], className='container-fluid'),
            className='navbar navbar-white bg-white m-0 p-0'
        )
    ],
    className='sticky-top bg-white w-100 border-bottom')
