import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app.dash import app

footer = html.Footer(
    children=[
        html.Div([
            html.Div([
                html.Div([
                     html.Img(
                         src=app.get_asset_url('logo.png'),
                         width='50%'
                     )
                     ], className='col'),
                html.Hr(className='clearfix w-100 d-md-none'),
                html.Div([
                    '“Se resaltan los efectos espaciales en los que esta econometría se centra, se exponen las formas de incorporación de estos efectos en modelos espaciales y los principales tests para detectarlos y contrastarlos...” Dr. Jorge A. Pérez Pineda'
                ], className='col d-flex align-items-center '),
                html.Hr(className='clearfix w-100 d-md-none'),
                html.Div([
                    html.H5('Referencias',className='font-weight-bold mt-3 mb-4 text-warning'),
                    html.Ul(
                        children=[
                           html.Li(
                                children=[
                                    html.A(
                                        children=[
                                            html.I(className='fa fa-paperclip'), '  Link 1'],
                                        href='https://github.com/IFFranciscoME/Urban_Lab_App/',
                                        target='_blank',
                                        className='text-white'
                                    )
                                ]
                            ),
                            html.Li(
                                children=[
                                    html.A(
                                        children=[
                                            html.I(className='fa fa-paperclip'), '  Link 2'],
                                        href='https://github.com/IFFranciscoME/Urban_Lab_App/',
                                        target='_blank',
                                        className='text-white'
                                    )
                                ]
                            ) ,
                            html.Li(
                                children=[
                                    html.A(
                                        children=[
                                            html.I(className='fa fa-paperclip'), '  Link 3'],
                                        href='https://github.com/IFFranciscoME/Urban_Lab_App/',
                                        target='_blank',
                                        className='text-white'
                                    )
                                ]
                            )  
                        ], className='list-unstyled'
                    )
                ], className='col')
            ], className='row'),
            html.Hr(className='bg-white p-0 m-0'),
            html.Ul(
                children=[
                    html.Li(
                        children=[
                            html.A(
                                children=[
                                    html.I(className='fab fa-github'), '  Code'],
                                href='https://github.com/IFFranciscoME/Urban_Lab_App/',
                                target='_blank',
                                className='text-white'
                            )
                        ]
                    )
                ],
                style={
                    'display': 'table',
                    'list-style-type': 'none',
                },
                className='mt-0 mb-0 mr-auto ml-auto'
            ),
            html.Hr(className='bg-white p-0 m-0'),
            html.P(children=[
                   'Copyright @2020 | Diseñado por Laboratorio de econometría espacial urbana'], className='text-center mt-2')
        ],
            className='container text-center text-white')
    ],
    className='w-100 mt-auto bg-dark'
)
