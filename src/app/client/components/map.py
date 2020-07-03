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
        'modal-variables-header': 'Estrés',
        'modal-variables-body': '“Se denomina estresor económico a todo estímulo externo que recibe una empresa y genera inestabilidad económica como por ejemplo: despidos, disminución en las ventas, etc. La variable estrés económico representa el estrés contraído por los empresas a partir de la suma de estos factores externos. Esta métrica nos indica el estado de cansancio emocional y físico. Reacción del cuerpo ante un desafío o demanda. Y se requiere un cambio o adaptación. Se decidió utilizar la frecuencia del 0 al 4 ya que se consideró que con ese rango se nos permite de manera más sencilla poder agrupar y categorizar las variables y de esta forma se puede obtener un resultado mucho más acertado y exacto.”'
    },
    'Adaptabilidad': {
        'modal-variables-header': 'Adaptabilidad',
        'modal-variables-body': '“A raíz de la pandemia el ambiente físico ha sido alterado y manipulado, lo que ha generado nuevos patrones de actividad, por consiguiente la conducta de las empresas se ha visto modificada para poder responder de mejor o peor manera ante esta situación. A este tipo de acciones se las conoce como adaptabilidad, las cuales son habilidades sociales con las que cuentan los individuos para poder tener mayor funcionalidad, esto está representado en esta variable. Es importante tomar en cuenta la adaptabilidad en el trabajo a realizar debido a que es una capacidad en la que debería terminar el estrés, es decir, la reacción de estrés a los estímulos externos muchas veces demanda una adaptación. Además, la naturalidad de esta pandemia nos ha puesto a todos en una situación de nueva normalidad a la que es necesario adaptarse. Se decidió utilizar la frecuencia del 0 al 2 ya que se consideró que con ese rango se permite, de manera más sencilla, poder agrupar y categorizar las variables y de esta forma se puede obtener un resultado mucho más acertado y exacto.”'
    },
    'Precios': {
        'modal-variables-header': 'Precios',
        'modal-variables-body': '“Esta metrica se enfoca en la predicción de la variación de los precios de los insumos y algunos servicios en Guadalajara para los próximos 6 mes. Los insumos y servicios están organizados en 32 clases que a su vez forman parte de 14 grupos. Los colores que se presentan en la métrica tienen una dinámica de semáforo tomando como criterio el rojo siendo que los precios decrementen más de un 1%, el amarillo que no tengan un cambio muy significativo en el precio con una variación de -1% a 1% y el verde que tengan una variación al alza mayor a un 1%. Las grafica que se ve representada en pesos toma la mediana de los precios de los productos dentro de cada clase.”'
    }
}

btn_variables = dbc.Button('Descripción',
                           id='open-modal-variables',
                           className='float-left mr-auto')

map_graph = dcc.Graph(id='map', figure={}, className='pb-3 pr-3 pl-3 ')

modal_variables = dbc.Modal(
    [
        dbc.ModalHeader(children=[], id='modal-variables-header'),
        dbc.ModalBody(children=[], id='modal-variables-body',
                      className='text-center text-justify'),
        dbc.ModalFooter(
            dbc.Button(
                'Cerrar', id='close-modal-variables', className='ml-auto'
            )
        ),
    ],
    id='modal-variables',
    centered=True,
)


# Connect the Plotly graphs with Dash Components
@app.callback(
    [
        Output(
            component_id='modal-variables-header',
            component_property='children'),
        Output(
            component_id='modal-variables-body',
            component_property='children'
        ),
        Output(
            component_id='map',
            component_property='figure'
        )
    ],
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

    header = variables[option_map]['modal-variables-header']
    body = variables[option_map]['modal-variables-body']

    return header, body, fig


@app.callback(
    Output('modal-variables', 'is_open'),
    [
        Input('open-modal-variables', 'n_clicks'),
        Input('close-modal-variables', 'n_clicks')
    ],
    [State('modal-variables', 'is_open')],
)
def toggle_modal_variables(n1, n2, is_open):
    if n1 or n2:
        return not is_open

    return is_open
