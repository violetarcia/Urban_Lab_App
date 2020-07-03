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
                         src=app.get_asset_url('logo2.png'),
                         className='w-100 m-auto rounded mt-3'
                     )
                     ], className='col d-flex flex-colum'),
                html.Hr(className='clearfix w-100 d-md-none'),
                html.Div([
                    html.P(children=[
                        'Este proyecto fue elaborado por estudiantes del PAP 4J05 de la universidad ITESO, durante el periodo de Verano 2020. Para consultar detalles dirigirse a: ',
                        html.A(children=[html.I(className='fab fa-github'), ' Code'],
                               href='https://github.com/IFFranciscoME/Urban_Lab_App/',
                               target='_blank',
                               className='text-white'
                               )
                    ])

                ], className='col d-flex align-items-center '),
                html.Hr(className='clearfix w-100 d-md-none'),
                html.Div([
                    html.H5(
                        'Referencias', className='font-weight-bold mt-3 mb-4 text-warning'),
                    html.Ul(
                        children=[
                            html.Li(
                                children=[
                                    html.A(
                                        children=[
                                            html.I(className='fa fa-paperclip'), '  Github'],
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
                                            html.I(className='fa fa-paperclip'), '  Notas Tecnicas'],
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
                                            html.I(className='fa fa-paperclip'), '  Datos'],
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
            html.P(children=[
                   'Copyright @2020 | Diseñado por Laboratorio de econometría espacial urbana'], className='text-center mt-2')
        ],
            className='container text-center text-white')
    ],
    className='w-100 mt-auto bg-dark'
)
