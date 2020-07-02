import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app.dash import app
from model.visualizaciones import bars_city, velocimeter_size, dif_prices
from model.datos import dict_metrics_table, df_pymes, predicciones

groups = ['Alimentos', 'Ropa', 'Cuidado personal', 'Salud', 'Transporte público']
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

dropdown2 = dcc.Dropdown(id='slct_fig',
                        options=[
                            {'label': 'Barras', 'value': 1},
                            {'label': 'Velocimetro', 'value': 2}
                        ],
                        multi=False,
                        clearable=False,
                        value='1',
                        className='float-right ml-auto w-25',
                        )
barchart = dcc.Graph(id='barchart', figure={}, className='')


# Connect the Plotly graphs with Dash Components
@app.callback(
    Output(component_id='barchart', component_property='figure'),
    [Input(component_id='slct_map', component_property='value'),
     Input(component_id='slct_fig', component_property='value')]
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


@ app.callback(
    Output(component_id='slct_fig', component_property='options'),
    [Input(component_id='slct_map', component_property='value')]
)
def update_graph(option_map):
    # Visualizations
    if option_map == 'Precios':
        return options['Precios']

    return options['noPrecios']

