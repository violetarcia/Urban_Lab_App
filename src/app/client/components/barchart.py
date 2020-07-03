import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app.dash import app
from model.visualizaciones import bars_city, velocimeter_size, dif_prices
from model.datos import dict_metrics_table, df_pymes, predicciones

groups = [
    'Alimentos',
    'Ropa',
    'Cuidado personal',
    'Salud',
    'Transporte público'
]

options = {
    'noPrecios': [
        {'label': 'Municipio', 'value': 1},
        {'label': 'Tamaño', 'value': 2}
    ],
    'Precios': [
        {'label': 'Alimentos', 'value': 1},
        {'label': 'Ropa', 'value': 2},
        {'label': 'Cuidado personal', 'value': 3},
        {'label': 'Salud', 'value': 4},
        {'label': 'Transporte público', 'value': 5}
    ]
}

btn_barchart = dbc.Button(
        'Descripción',
        id='open-modal-barchart',
        className='float-left mr-auto d-none'
    )

dropdown_barchart = dcc.Dropdown(
    id='slct_fig',
    options=[
        {'label': 'Barras', 'value': 1},
        {'label': 'Velocimetro', 'value': 2}
    ],
    multi=False,
    clearable=False,
    value='1',
    className='float-right ml-auto w-25',
)

barchart = dcc.Graph(
    id='barchart',
    figure={},
    className=''
)


modal_barchart = dbc.Modal(
    [
        dbc.ModalHeader(children=['Grafica de variación de precios en pesos']),
        dbc.ModalBody(
            children=['En esta grafica se observa una predicción en pesos de lo que variaran los precios dentro de 6 meses. El numero representado al final de la gráfica es una media de los precios futuros de todos los productos dentro de esa categoría. Por lo que es un precio representativo de lo que estarán los precios en un futuro. El numero en color verde o rojo representa cuantos pesos van a subir o bajar los productos. Ejemplo en los Alimentos en la clase de Carnes se ve el numero verde 1.42, lo que significa que en general los productos de carne estarán 1.42 pesos más caros en noviembre. La grafica representa una barra horizontal y una línea vertical, la línea vertical representa los precios actuales  y la barra horizontal representa los precios futuros.'],
            className='text-center text-justify'
        ),
        dbc.ModalFooter(
            dbc.Button(
                'Cerrar', id='close-modal-barchart', className='ml-auto'
            )
        ),
    ],
    id='modal-barchart',
    centered=True,
)


# Connect the Plotly graphs with Dash Components
@app.callback(
    Output(
        component_id='barchart',
        component_property='figure'
    ),
    [
        Input(
            component_id='slct_map',
            component_property='value'
        ),
        Input(
            component_id='slct_fig',
            component_property='value'
        )
    ]
)
def update_graph(option_map, figura_n):
    # Visualizations
    if option_map == 'Precios':
        fig = dif_prices(predicciones, groups[int(figura_n)-1])
    else:
        if int(figura_n) == 1:
            fig = bars_city(
                df_pymes,
                option_map,
                dict_metrics_table[option_map]
            )
        else:
            fig = velocimeter_size(
                df_pymes,
                option_map,
                dict_metrics_table[option_map]
            )
    return fig

# Connect the Plotly graphs with Dash Components


@app.callback(
    [
        Output(
            component_id='open-modal-barchart',
            component_property='className'
        ),
        Output(
            component_id='slct_fig',
            component_property='options'
        )
    ]
    ,
    [Input(
        component_id='slct_map',
        component_property='value'
    )]
)
def update_graph(option_map):
    # Visualizations
    if option_map == 'Precios':
        return 'float-left mr-auto d-block', options['Precios']

    return 'd-none', options['noPrecios']


@app.callback(
    Output('modal-barchart', 'is_open'),
    [
        Input('open-modal-barchart', 'n_clicks'),
        Input('close-modal-barchart', 'n_clicks')
    ],
    [State('modal-barchart', 'is_open')],
)
def toggle_modal_barchart(n1, n2, is_open):
    if n1 or n2:
        return not is_open

    return is_open
