import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app.dash import app
from model.visualizaciones import bars_city, velocimeter_size, dif_prices
from model.datos import dict_metrics_table, df_pymes, predicciones

barchart2 = dcc.Graph(id='barchart2', figure={},className='pt-1 pb-1')


# Connect the Plotly graphs with Dash Components
@app.callback(
    Output(component_id='barchart2', component_property='figure'),
    [Input(component_id='slct_map', component_property='value'),
     Input(component_id='slct_fig', component_property='value')]
)
def update_graph(option_map, figura_n):
    # Visualizations
    if option_map == 'Precios':
        if figura_n == "1":
            fig = dif_prices(predicciones, 'Alimentos')
        else:
            fig = dif_prices(predicciones, figura_n)
    else:
        if figura_n == "1":
            fig = bars_city(df_pymes, option_map, dict_metrics_table[option_map])
        else:
            fig = velocimeter_size(df_pymes, option_map, dict_metrics_table[option_map])

    return fig



@app.callback(
    Output('slct_fig', 'options'),
    [Input('slct_map', 'value')]
)
def update_date_dropdown(opt_map):
    if opt_map == 'Estres' or opt_map == 'Adaptabilidad':
        return [{'label': 'Barras', 'value': '1'}, {'label': 'Velocimetro', 'value': '2'}]
    else:
        return [{'label': 'Alimentos', 'value': '1'},
                {'label': 'Ropa', 'value': 'Ropa'},
                {'label': 'Cuidado personal', 'value': 'Cuidado personal'},
                {'label': 'Salud', 'value': 'Salud'},
                {'label': 'Transporte público', 'value': 'Transporte público'}
                ]


# Alimentos, 'Bebidas alcohólicas y tabaco', 'Cuidado personal', 'Electricidad y combustibles',
# 'Ropa',  'Salud','Transporte por cuenta propia', 'Transporte público'