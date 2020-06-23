import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from app.dash import app

from model.datos import Data
from model.proceso import metric_quantification
from model.visualizaciones import map_metric, bar_chart
import model.entradas as ent

# Datos que se utilizaran
data = Data()
data.get_data()

# limpiar base de datos
df_data = data.clean_data(data.df_data)

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
    # Using metric_quantification with stress conditions
    metric_s = metric_quantification(df_data, ent.dict_conditions[option_map], option_map)
    # Visualizations
    fig = map_metric(metric_s, option_map, ent.dict_colors[option_map])

    #fig = bar_chart(metric_s, option_map)
    return container, fig