import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app.dash import app

from model.datos import dict_metrics_df
from model.visualizaciones import map_metric

output_container = html.Div(id='output_container', children=[], className='text-center')

map_graph = dcc.Graph(id='map', figure={})

# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='map', component_property='figure')],
    [Input(component_id='slct_map', component_property='value')]
)
def update_graph(option_map):
    container = 'La variable escogida por el usuario es: {}'.format(option_map)
    metric = dict_metrics_df[option_map]
    # Visualizations
    fig = map_metric(metric, option_map, ent.dict_colors[option_map])

    #fig = bar_chart(metric_s, option_map)
    return container, fig