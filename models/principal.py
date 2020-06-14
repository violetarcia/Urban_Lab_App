
# .. ................................................................................... .. #
# .. Proyecto: UrbanLab - Plataforma de ayuda para micro y pequeñas empresas             .. #
# .. Archivo: principal.py - flujo principal de uso                                      .. #
# .. Desarrolla: ITERA LABS, SAPI de CV                                                  .. #
# .. Licencia: Todos los derechos reservados                                             .. #
# .. Repositorio: https://github.com/IFFranciscoME/Urban_Lab.git                         .. #
# .. ................................................................................... .. #


# Importing and initializing main Python libraries
import proceso as pr
import datos as dat
import entradas as ent
import visualizaciones as vs
import numpy as np
import pandas as pd
from time import time

# Start time
t0 = time()

if __name__ == "__main__":
	
	# Using function: read_file (original)
	df_data_or = dat.read_file(ent.path, ent.sheet)
	
	# Using function: clean_data
	df_data = dat.clean_data(df_data_or)
	
	# Using metric_stress
	metric_s = pr.metric_stress(df_data)
	
	# End time
	t1 = time()
	print('el tiempo transcurrido fue: ' + str(t1-t0))