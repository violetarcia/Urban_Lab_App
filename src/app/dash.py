
# -- --------------------------------------------------------------------------------------------------- -- #
# -- project: Urban Lab / Laboratorio de econometría espacial urbana - PAP4J05                           -- #
# -- script: dash.py : script con el codigo funcional del dashboard                                      -- #
# -- author: FranciscoME / PAP4J05                                                                       -- #
# -- license: MIT                                                                                        -- #
# -- repository: https://github.com/IFFranciscoME/Urban_Lab_App                                          -- #
# -- --------------------------------------------------------------------------------------------------- -- #

import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from config import config, about
from api.server import server

from model.datos import Data
from model.proceso import metric_quantification
from model.visualizaciones import map_metric, bar_chart
import model.entradas as ent

# Datos que se utilizaran
data = Data()
data.get_data()

# limpiar base de datos
df_data = data.clean_data(data.df_data)

# Metrica
metric_s = metric_quantification(df_data, ent.conditions_stress, 'Estres')

# Visualizacion
fig = map_metric(metric_s, 'Estres', ent.shp_path, ent.kml_path)

'''
app = dash.Dash(name=config.name,
                server=server,
                routes_pathname_prefix='/',
                assets_folder=config.root+'/app/assets',
                external_stylesheets=[dbc.themes.LUX, config.fontawesome])


app.title = config.name

navbar = dbc.Nav(className="nav nav-pills", children=[
    # logo/home
    dbc.NavItem(html.Img(src=app.get_asset_url("logo.PNG"), height="40px")),
    # about
    dbc.NavItem(html.Div([
        dbc.NavLink("About", href="/", id="about-popover", active=False),
        dbc.Popover(id="about", is_open=False, target="about-popover", children=[
            dbc.PopoverHeader("How it works"), dbc.PopoverBody(about.txt)
        ])
    ])),
    # links
    dbc.DropdownMenu(label="Links", nav=True, children=[
        dbc.DropdownMenuItem([html.I(className="fa fa-linkedin"),
                              "  Contacts"], href=config.contacts, target="_blank"),
        dbc.DropdownMenuItem(
            [html.I(className="fa fa-github"), "  Code"], href=config.code, target="_blank")
    ])
])
'''


app = dash.Dash(__name__)

# ------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("Urban Lab: Datos de ZMG", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_map",
                 options=[
                     {"label": "Estrés Economico", "value": "Estres"},
                     {"label": "Adaptabilidad", "value": "Adaptabilidad"}
                      ],
                 multi=False,
                 value="Estres",
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='map', figure={})

])

# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='map', component_property='figure')],
    [Input(component_id='slct_map', component_property='value')]
)
def update_graph(option_map):
    container = "The map chosen by user was: {}".format(option_map)
    # Using metric_quantification with stress conditions
    metric_s = metric_quantification(df_data, ent.dict_conditions[option_map], option_map)
    # Visualizations
    fig = map_metric(metric_s, 'Estres', ent.shp_path, ent.kml_path)

    #fig = bar_chart(metric_s, option_map)
    return container, fig
	

#-----------------------------------------------------------------------------

'''
@app.callback(output=Output("plot-total", "figure"), inputs=[Input("df_data_or", "value")])
def plot_total_cases(df_data_or):

    # Using metric_quantification with stress conditions
    metric_s = metric_quantification(df_data, ent.conditions_stress, 'Estres')
    # Visualizations
    figure = map_metric(metric_s, 'Estres', ent.shp_path, ent.kml_path)
    #fig.show()
    # Python function to plot active cases
    return figure
'''
'''
@app.callback(output=Output("plot-active", "figure"), inputs=[Input("country", "value")])
def plot_active_cases(country):
    data.process_data(country)
    model = Model(data.dtf)
    model.forecast()
    model.add_deaths(data.mortality)
    result = Result(model.dtf)
    # Python function to render output panel
    return result.plot_active(model.today)


@app.callback(output=Output("output-panel", "children"), inputs=[Input("country", "value")])
def render_output_panel(country):
    data.process_data(country)
    model = Model(data.dtf)
    model.forecast()
    model.add_deaths(data.mortality)
    result = Result(model.dtf)
    peak_day, num_max, total_cases_until_today, total_cases_in_30days, active_cases_today, active_cases_in_30days = result.get_panel()
    peak_color = "white" if model.today > peak_day else "red"
    panel = html.Div([
        html.H4(country),
        dbc.Card(body=True, className="text-white bg-primary", children=[
            html.H6("Total cases until today:", style={"color": "white"}),
            html.H3("{:,.0f}".format(total_cases_until_today),
                    style={"color": "white"}),

            html.H6("Total cases in 30 days:", className="text-danger"),
            html.H3("{:,.0f}".format(total_cases_in_30days),
                    className="text-danger"),

            html.H6("Active cases today:", style={"color": "white"}),
            html.H3("{:,.0f}".format(active_cases_today),
                    style={"color": "white"}),

            html.H6("Active cases in 30 days:", className="text-danger"),
            html.H3("{:,.0f}".format(active_cases_in_30days),
                    className="text-danger"),

            html.H6("Peak day:", style={"color": peak_color}),
            html.H3(peak_day.strftime("%Y-%m-%d"),
                    style={"color": peak_color}),
            html.H6("with {:,.0f} cases".format(
                num_max), style={"color": peak_color})

        ])
    ])
    return panel
    
'''

