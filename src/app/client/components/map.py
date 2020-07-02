import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
from app.dash import app

from model.datos import dict_metrics_df, semaforo
from model.visualizaciones import map_metric, table_prices
from model.entradas import dict_colors

variables = {
    'Estres': {
        'modal-header': 'Estrés',
        'modal-body': '“Esta métrica nos indica el estado de cansancio emocional y físico. Reacción del cuerpo ante un desafío o demanda. Y se requiere un cambio o adaptación. Se decidió utilizar la frecuencia del 0 al 4 ya que se consideró que con ese rango se nos permite de manera más sencilla poder agrupar y categorizar las variables y de esta forma se puede obtener un resultado mucho más acertado y exacto.”'
    },
    'Adaptabilidad': {
        'modal-header': 'Adaptabilidad',
        'modal-body': '“Es importante tomar en cuenta la adaptabilidad en el trabajo a realizar debido a que es una capacidad en la que debería terminar el estrés, es decir, la reacción de estrés a los estímulos externos muchas veces demanda una adaptación. Además, la naturalidad de esta pandemia nos ha puesto a todos en una situación de nueva normalidad a la que es necesario adaptarse. Se decidió utilizar la frecuencia del 0 al 2 ya que se consideró que con ese rango se permite, de manera más sencilla, poder agrupar y categorizar las variables y de esta forma se puede obtener un resultado mucho más acertado y exacto.”'
    },
    'Precios': {
        'modal-header': 'Precios',
        'modal-body': '“Con esto, se pretende enfocarse en la predicción de la variación de los precios de los insumos y algunos servicios en Guadalajara para el próximo mes. Los insumos y servicios están organizados en 32 clases que a su vez forman parte de 14 grupos. Los colores que se presentan en la métrica tienen una dinámica de semáforo tomando como criterio el verde siendo que los precios decrementen, el amarillo que no tengan un cambio muy significativo en el precio con una variación de -1% a 1% y el rojo que tengan una variación al alza mayor a un 1%. Las grafica que se ve representada en pesos toma la mediana de los precios de los productos dentro de cada clase.”'
    }
}

output_container = html.Div([
    dbc.Button(["Descripción", ], id="open-centered")
], className='row d-flex flex-row-reverse')

map_graph = dcc.Graph(id='map', figure={}, className='pb-3 pr-3 pl-3 ')

modal = dbc.Modal(
    [
        dbc.ModalHeader(children=[], id='modal-header'),
        dbc.ModalBody(children=[], id='modal-body',
                      className='text-center text-justify'),
        dbc.ModalFooter(
            dbc.Button(
                "Cerrar", id="close-centered", className="ml-auto"
            )
        ),
    ],
    id="modal-centered",
    centered=True,
)


# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='modal-header', component_property='children'),
     Output(component_id='modal-body', component_property='children'),
     Output(component_id='map', component_property='figure')],
    [Input(component_id='slct_map', component_property='value')]
)
def update_graph_bar(option_map):
    #container = 'La variable escogida por el usuario es: {}'.format(option_map)
    if option_map == 'Precios':
        fig = table_prices(semaforo)
    else:
        metric = dict_metrics_df[option_map]
        # Visualizations
        fig = map_metric(metric, option_map, dict_colors[option_map])

    header = variables[option_map]['modal-header']
    body = variables[option_map]['modal-body']

    return header, body, fig


@app.callback(
    Output("modal-centered", "is_open"),
    [Input("open-centered", "n_clicks"), Input("close-centered", "n_clicks")],
    [State("modal-centered", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open

    return is_open
