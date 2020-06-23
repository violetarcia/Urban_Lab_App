import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from app.client.components.map import map_graph, output_container
from app.client.utils.header import header

layout = html.Div([ 
    header,
    output_container,
    html.Br(),
    map_graph
])