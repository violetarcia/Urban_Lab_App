import model
from model.datos import read_map_files
import model.entradas as ent
from config.config import root

df_file = read_map_files(root+'/app/assets/files/'+ent.shp_path, root+'/app/assets/files/'+ent.kml_path)

