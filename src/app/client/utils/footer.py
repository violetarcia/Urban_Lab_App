import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app.dash import app

footer = html.Footer(
    children=[
        html.Div(
            [
                html.Div(
                    [
                        html.Div(
                            [
                                html.Img(
                                    src=app.get_asset_url('logo2.png'),
                                    className='w-100 m-auto rounded'
                                )
                            ],
                            className='col-12 col-sm-12 col-md-4 col-lg-4 col-xl-4 mx-auto'),
                        html.Hr(
                            className='clearfix w-100 d-md-none bg-white'),
                        html.Div(
                            [
                                html.P(
                                    children=[
                                        'Este proyecto fue elaborado por estudiantes del PAP 4J05 de la universidad ITESO, durante el periodo de Verano 2020. Para consultar detalles dirigirse a: ',
                                        html.A(
                                            children=[
                                                html.I(
                                                    className='fab fa-github'),
                                                ' Code'
                                            ],
                                            href='https://github.com/IFFranciscoME/Urban_Lab_App/',
                                            target='_blank',
                                            className='text-white'
                                        )
                                    ]
                                )
                            ],
                            className='col-12 col-sm-12 col-md-5 col-lg-5 col-xl-5 mx-auto'),
                        html.Hr(
                            className='clearfix w-100 d-md-none bg-white'),
                        html.Div(
                            [
                                html.H5(
                                    'Referencias',
                                    className='font-weight-bold text-warning'
                                ),
                                html.Ul(
                                    children=[
                                        html.Li(
                                            children=[
                                                html.A(
                                                    children=[
                                                        html.I(
                                                            className='fa fa-paperclip'),
                                                        '  Github'
                                                    ],
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
                                                        html.I(
                                                            className='fa fa-paperclip'),
                                                        '  Notas Tecnicas'
                                                    ],
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
                                                        html.I(
                                                            className='fa fa-paperclip'),
                                                        '  Datos'
                                                    ],
                                                    href='https://github.com/IFFranciscoME/Urban_Lab_App/',
                                                    target='_blank',
                                                    className='text-white'
                                                )
                                            ]
                                        )
                                    ],
                                    className='list-unstyled'
                                )
                            ],
                            className='col-12 col-sm-12 col-md-3 col-lg-3 col-xl-3 mx-auto')
                    ],
                    className='row mb-3'
                ),
                html.Hr(className='bg-white p-0 m-0'),
                html.P(
                    children=[
                        'Copyright @2020 | Diseñado por Laboratorio de econometría espacial urbana'
                    ],
                    className='mt-2'
                )
            ],
            className='container-fluid mt-3 text-center text-white '
        )
    ],
    className='w-100 mt-auto bg-dark'
)
