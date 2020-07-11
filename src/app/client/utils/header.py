import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app.dash import app
from config.config import name


header = html.Header(
    children=[
        dbc.Nav(
            className='navbar navbar-white bg-white',
            children=[
                # logo/home
                dbc.NavItem([
                    html.Img(
                        src=app.get_asset_url('logo.png'),
                        height='40px'
                    )],
                    className='navbar-brand ml-2'
                ),
                html.H4(name, className='m-auto text-primary font-weight-bold'),
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
                                'color': '#272E42',
                                'background-color': '#D1D8EE',
                                'fontSize' : '16px'
                                   }
                        )],
                        style={'width': '200px'},
                        className='ml-auto'
                    )
            ]
        )
    ], className='sticky-top bg-white w-100 border-bottom')
