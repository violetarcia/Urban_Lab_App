
# .. ................................................................................... .. #
# .. Proyecto: UrbanLab - Plataforma de ayuda para micro y pequeñas empresas             .. #
# .. Archivo: datos.py - procesos de obtencion y almacenamiento de datos                 .. #
# .. Desarrolla: ITERA LABS, SAPI de CV                                                  .. #
# .. Licencia: Todos los derechos reservados                                             .. #
# .. Repositorio: https://github.com/IFFranciscoME/Urban_Lab.git                         .. #
# .. ................................................................................... .. #

import pandas as pd
import numpy as np
from config.config import root

class Data():
	
	# -- -------------------------------------------------------------------------------- -- #
	# -- Read data file and storing it in df_data
	# -- -------------------------------------------------------------------------------- -- #
	def get_data(self):
		self.df_data = pd.read_excel(root +'\\app\\assets\\files\\' +
                                     'Base_de_datos.xlsx', sheet_name='IIEG_E_1')
		
	# -- -------------------------------------------------------------------------------- -- #
	# -- Cleaning Database that is in a DataFrame
	# -- -------------------------------------------------------------------------------- -- #
	@staticmethod
	def clean_data(df_data):
        # Replace
		df = df_data.copy()
		df.replace([998, 999, 'No contesto', 'No sé'], np.nan, inplace=True)
		df.replace(
            {
                "Más de 52": 52,
                "De 26 a 52": 26,
                "No aplica": 100,
                "No contesto": 101,
                "No sé": 102,
                "Más de un año": 12}, inplace=True)

        # Specific columns
		df['aumento_precios'].replace(100, np.nan, inplace=True)
		return df


