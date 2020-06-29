
# .. ................................................................................... .. #
# .. Proyecto: UrbanLab - Plataforma de ayuda para micro y pequeñas empresas             .. #
# .. Archivo: datos.py - procesos de obtencion y almacenamiento de datos                 .. #
# .. Desarrolla: ITERA LABS, SAPI de CV                                                  .. #
# .. Licencia: Todos los derechos reservados                                             .. #
# .. Repositorio: https://github.com/IFFranciscoME/Urban_Lab.git                         .. #
# .. ................................................................................... .. #

import pandas as pd
import numpy as np
import model.entradas as ent
from model.proceso import metric_quantification
from config.config import db

class Data():

	# -- -------------------------------------------------------------------------------- -- #
	# -- Read data file and storing it in df_data
	# -- -------------------------------------------------------------------------------- -- #
	def get_data(self):
		self.df_data = pd.read_excel(db + 'Base_de_datos.xlsx', sheet_name='IIEG_E_1')
		
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
		# Tomar solo la ZMG
		df_final = df.loc[df['Municipio'].isin(['Zapopan','Tonalá','Tlaquepaque','Tlajomulco de Zúñiga','El Salto','Guadalajara'])]	
		# Reiniciar el index
		df_final.reset_index(drop=True, inplace=True)
		return df_final

# Datos que se utilizaran
data = Data()
data.get_data()

# limpiar base de datos
df_pymes = data.clean_data(data.df_data)

# -- Estres --
metric_s = metric_quantification(df_pymes, ent.conditions_stress, 'Estres')

# Dataframe de metrica de estres
df_stress = metric_s['df_prices']
# tabla de metrica
metric_s_table = metric_s['metric_table']

# -- Adaptabilidad
metric_a = metric_quantification(df_pymes, ent.conditions_adaptability, 'Adaptabilidad')

# Dataframe de metrica de estres
df_adapt = metric_a['df_prices']
# tabla de metrica
metric_a_table = metric_a['metric_table']

dict_metrics_df = {'Estres': df_stress, 'Adaptabilidad': df_adapt}
dict_metrics_table = {'Estres': metric_s_table, 'Adaptabilidad': metric_a_table}



