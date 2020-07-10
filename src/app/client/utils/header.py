import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app.dash import app
from config.config import name


header = html.Header(
    children=[
        dbc.Nav(
            className='navbar navbar-expand-lg navbar-white bg-white  d-flex ',
            children=[
                # logo/home
                dbc.NavItem([
                    html.Img(
                        src=app.get_asset_url('logo.png'),
                        height='40px'
                    )],
                    className='ml-2'
                ),
                html.H4(name, className='m-auto text-primary font-weight-bold'),
                html.Div([
                    dbc.NavItem([
                        html.A(
                            children=[
                                html.I(className='fab fa-github'), '  Code'],
                            href='https://github.com/IFFranciscoME/Urban_Lab_App/',
                            target='_blank'
                        )],
                        className='mr-2 mt-auto mb-auto'
                    ),
                    dbc.NavItem([
                        dcc.Dropdown(
                            id='slct_map',
                            options=[
                                {'label': 'Estrés Económico', 'value': 'Estres'},
                                {'label': 'Adaptabilidad',
                                    'value': 'Adaptabilidad'},
                                {'label': 'Predicción de Precios', 'value': 'Precios'}
                            ],
                            multi=False,
                            clearable=False,
                            value='Estres',
                            style={'width': '200px',
                                'paddingBottom': '5px',
                                'color': '#325ADC',
                                'background-color': '#D1D8EE',
                                'fontSize' : '21px',
                                'fontColor': '#F1F2F5'
                                   }
                        )],
                        style={'width': '200px'},
                        className='m-auto'
                    )
                ], className='row ml-auto mr-2')
            ]
        )
    ], className='sticky-top bg-white w-100 border-bottom')
