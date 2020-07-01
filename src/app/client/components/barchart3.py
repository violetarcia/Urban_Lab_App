import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app.dash import app
from model.visualizaciones import table_giro, treemap_prices
from model.datos import dict_metrics_table, df_pymes, predicciones

barchart3 = dcc.Graph(id='barchart3', figure={}, className='')
@app.callback(
    Output(component_id='barchart3', component_property='figure'),
    [Input(component_id='slct_map', component_property='value')]
)
def update_graph(option_map):

    # Visualizations
    if option_map == 'Precios':
        fig = treemap_prices(predicciones)
    else:
        fig = table_giro(df_pymes, option_map, dict_metrics_table[option_map])
    
    return fig

