import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app.dash import app
from config.config import name


header = dbc.Nav(
    className='navbar navbar-expand-lg navbar-light bg-light ', 
    children=[
        # logo/home
        dbc.NavItem(html.Img(src=app.get_asset_url('logo.png'), height='40px')),
        html.H5(name,className='mr-auto'),
        dbc.NavItem(
            html.A(
                children =[html.I(className='fa fa-github'), '  Code'],
                href='https://github.com/IFFranciscoME/Urban_Lab_App/',
                target='_blank'
            ),
            className='ml-auto mr-2'
        ),
        dbc.NavItem(
            dcc.Dropdown(
                id='slct_map',
                options=[
                    {'label': 'Estrés Economico', 'value': 'Estres'},
                    {'label': 'Adaptabilidad', 'value': 'Adaptabilidad'}
                ],
                multi=False,
                value='Estres',
                style={'width': '200px'}
            ),
            style={'width': '200px'},
            className='mr-5'
        )
    ]
)
