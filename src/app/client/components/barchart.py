import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app.dash import app
from model.visualizaciones import bars_city, velocimeter_size, dif_prices, histogram_metric
from model.datos import dict_metrics_table, df_pymes, predicciones

groups = [
    'Alimentos',
    'Ropa',
    'Cuidado personal',
    'Salud',
    'Transporte público'
]

txt_barchart = html.Div([
    html.H5(children=['Grafica de variación de precios en pesos']),
    html.P(children=['En esta grafica se observa una predicción en pesos de lo que variaran los precios dentro de 6 meses. El numero representado al final de la gráfica es una media de los precios futuros de todos los productos dentro de esa categoría. Por lo que es un precio representativo de lo que estarán los precios en un futuro. El numero en color verde o rojo representa cuantos pesos van a subir o bajar los productos. Ejemplo en los Alimentos en la clase de Carnes se ve el numero verde 1.42, lo que significa que en general los productos de carne estarán 1.42 pesos más caros en noviembre. La grafica representa una barra horizontal y una línea vertical, la línea vertical representa los precios actuales  y la barra horizontal representa los precios futuros.'])
],
id='txt_barchart',
className='d-none')


dropdown_barchart = dcc.Dropdown(
    id='slct_fig',
    options=[
        {'label': groups[0], 'value': 0},
        {'label': groups[1], 'value': 1},
        {'label': groups[2], 'value': 2},
        {'label': groups[3], 'value': 3},
        {'label': groups[4], 'value': 4}
    ],
    multi=False,
    clearable=False,
    value='1',
    className='d-none',
)

tabs_barchart = dcc.Tabs(id='tabs_fig', value='0', children=[
    dcc.Tab(label='Distribución por Municipio', value='0'),
    dcc.Tab(label='Tamaño de Empresas', value='1'),
dcc.Tab(label='Histograma de Métrica', value='2'),
])

output_barchart = html.Div([
    dropdown_barchart,
    tabs_barchart
])

barchart = dcc.Graph(
    id='barchart',
    figure={},
    className='mt-auto mb-auto'
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
        ),
        Input(
            component_id='tabs_fig',
            component_property='value'
        )
    ]
)
def update_graph(option_map, figura_slct, figura_tabs ):
    # Visualizations
    if option_map == 'Precios':
        fig = dif_prices(predicciones, groups[int(figura_slct)])
    else:
        if int(figura_tabs) == 0:
            fig = bars_city(
                df_pymes,
                option_map,
                dict_metrics_table[option_map]
            )
        elif int(figura_tabs) == 1:
            fig = velocimeter_size(
                df_pymes,
                option_map,
                dict_metrics_table[option_map]
            )
        else:
            fig = histogram_metric(
                dict_metrics_table[option_map],
                option_map
            )
    return fig

# Connect the Plotly graphs with Dash Components
@app.callback(
    [
        Output(
            component_id='txt_barchart',
            component_property='className'
        ),
        Output(
            component_id='slct_fig',
            component_property='className'
        ),
        Output(
            component_id='tabs_fig',
            component_property='className'
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
        return 'd-block text-justify', 'd-block', 'd-none'

    return 'd-none', 'd-none', 'd-block'


