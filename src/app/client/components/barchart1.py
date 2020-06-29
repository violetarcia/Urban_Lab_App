import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app.dash import app
from model.visualizaciones import velocimeter_size
from model.datos import dict_metrics_table, df_pymes

barchart1 = dcc.Graph(id='barchar1', figure={})


# Connect the Plotly graphs with Dash Components
@app.callback(
    Output(component_id='barchar1', component_property='figure'),
    [Input(component_id='slct_map', component_property='value')]
)
def update_graph(option_map):

    # Visualizations
    fig = velocimeter_size(df_pymes, option_map, dict_metrics_table[option_map])
    
    return fig