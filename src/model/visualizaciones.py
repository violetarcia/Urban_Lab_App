# .. ................................................................................... .. #
# .. Proyecto: SocialSim - Plataforma de simulacion de proyectos socioproductivos        .. #
# .. Archivo: visualizaciones.py - diccionario con datos de entrada                      .. #
# .. Desarrolla: ITERA LABS, SAPI de CV                                                  .. #
# .. Licencia: Todos los derechos reservados                                             .. #
# .. Repositorio: https://github.com/IFFranciscoME/Urban_Lab.git                         .. #
# .. ................................................................................... .. #

# Importing and initializing main Python libraries
import plotly.express as px
import geopandas as gpd
from config.config import root
import json

# -- ------------------------------------------------------------------------------------ -- #
# -- Function: Read shape file and storing it in to a DataFrame
# -- ------------------------------------------------------------------------------------ -- #
def read_map_files(path_shape, path_kml):
    """
    Parameters
    ---------
    :param:
        path: str : path of shape file

    Returns
    ---------
    :return:
        geodf: DataFrame : clean data in DF

    Debuggin
    ---------
        path = ent.map_path

	"""
    gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'
    geodf_kml = gpd.read_file(root + "\\app\\assets\\files\\" + path_kml)
    geodf_shp = gpd.read_file(root + "\\app\\assets\\files\\" + path_shape)

    geodf_kml.to_file(root + "\\app\\assets\\files\\" + path_kml, driver="GeoJSON")  # aqui falla

    with open(root + "\\app\\assets\\files\\" + path_kml) as geofile:
        j_file = json.load(geofile)
    # Asignar el id al kml
    i = 0
    for feature in j_file["features"]:
        feature['id'] = geodf_shp['d_cp'][i]
        i += 1

    return j_file

# -- ------------------------------------------------------------------------------------ -- #
# -- Function: Map
# -- ------------------------------------------------------------------------------------ -- #

def map_metric(df_data, metric, path_shape, path_kml):
    """
    Parameters
    ---------
    :param:
        df_data: DataFrame : data in a DF
		metric: str : name of column of metric
		path: str : "cp_jal_2/CP_14_Jal_v6.shp"

    Returns
    ---------
    :return:
        figure

    Debuggin
    ---------
        df_data = metric_quantification(df_data, ent.conditions_stress, 'Estres')
		metric = 'estres'
		path: str : "cp_jal_2/CP_14_Jal_v6.shp"
	"""
    j_file = read_map_files(path_shape, path_kml)
    fig = px.choropleth_mapbox(df_data, geojson=j_file, locations='CP', color=metric,
                               color_continuous_scale="Viridis",
                               range_color=(0, max(df_data[metric])),
                               mapbox_style="carto-positron",
                               zoom=10, center={"lat": 20.666820, "lon": -103.3918228},
                               opacity=0.5,
                               labels={metric: 'Nivel de ' + metric}
                               )
    fig.update_layout(margin={"r": 0, "t": 0, "l": 0, "b": 0})

    return fig
