import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app.dash import app
from model.visualizaciones import bars_city, velocimeter_size
from model.datos import dict_metrics_table, df_pymes

barchart2 = dcc.Graph(id='barchart2', figure={})


# Connect the Plotly graphs with Dash Components
@app.callback(
    Output(component_id='barchart2', component_property='figure'),
    [Input(component_id='slct_map', component_property='value'),
     Input(component_id='slct_fig', component_property='value')]
)
def update_graph(option_map, figura_n):

    # Visualizations
    if figura_n == "1":
        fig = bars_city(df_pymes, option_map, dict_metrics_table[option_map])
    else:
        fig = velocimeter_size(df_pymes, option_map, dict_metrics_table[option_map])

    return fig