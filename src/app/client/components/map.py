import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app.dash import app

from model.datos import dict_metrics_df, semaforo
from model.visualizaciones import map_metric, table_prices
from model.entradas import dict_colors
output_container = html.Div(id='output_container', children=[], className='text-center')

map_graph = dcc.Graph(id='map', figure={})

# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='map', component_property='figure')],
    [Input(component_id='slct_map', component_property='value')]
)
def update_graph_bar(option_map):
    container = 'La variable escogida por el usuario es: {}'.format(option_map)
    if option_map == 'Precios':
        fig = table_prices(semaforo)
    else:
        metric = dict_metrics_df[option_map]
        # Visualizations
        fig = map_metric(metric, option_map, dict_colors[option_map])
    return container, fig