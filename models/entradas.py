
# .. ................................................................................... .. #
# .. Proyecto: UrbanLab - Plataforma de ayuda para micro y pequeñas empresas             .. #
# .. Archivo: entrada.py - diccionario con datos de entrada                              .. #
# .. Desarrolla: ITERA LABS, SAPI de CV                                                  .. #
# .. Licencia: Todos los derechos reservados                                             .. #
# .. Repositorio: https://github.com/IFFranciscoME/Urban_Lab.git                         .. #
# .. ................................................................................... .. #

path = 'Base_de_datos.xlsx'
sheet = 'IIEG_E_1'

conditions_stress = {
				'ventas_porcentaje': {
							1: (-1, 25),
							2: (25, 50),
							3: (50, 75),
							4: (75, 100)
						},
				'perdidas_porcentaje': {
							1: (-1, 25),
							2: (25, 50),
							3: (50, 75),
							4: (75, 150) # 992
						},
				'capacidad': {
							1: (-1, 25),
							2: (25, 50),
							3: (50, 75),
							4: (75, 100)
						},
				'cerrar': {
							0: ['No'],
							2: ['Sí']
						},
				'despidos': {
							2: ['Sí', 'No, pero lo está considerando'],
							0: ['No', 'No cuenta con personal'],
							3: ['No, pero lo va a hacer en los próximos días']
						},
				'plantilla_porcentaje': {
							1: (-1, 25),
							2: (25, 50),
							3: (50, 75),
							4: (75, 100)
						},
				'pago_salarios': {
							0: [100, 101, 102],
							1: (-1, 6),
							2: (6, 12),
							3: (12, 18),
							4: (18, 52) # 367
						},
				'pago_impuestos': {
							0: [100, 101, 102],
							1: (-1, 6),
							2: (6, 12),
							3: (12, 18),
							4: (18, 52) # 82
						},
				'pago_creditos': {
							0: [100, 101, 102],
							1: (-1, 6),
							2: (6, 12),
							3: (12, 18),
							4: (18, 52) # 556
						},
				'pago_renta': {
							0: [100, 101, 102],
							1: (-1, 6),
							2: (6, 12),
							3: (12, 18),
							4: (18, 52) # 85
						},
				'pago_internet': {
							0: [100, 101, 102],
							1: (-1, 6),
							2: (6, 12),
							3: (12, 18),
							4: (18, 52) # 85
						},
				'pago_agua': {
							0: [100, 101, 102],
							1: (-1, 6),
							2: (6, 12),
							3: (12, 18),
							4: (18, 52) # 85
						},
				'pago_gas': {
							0: [100, 101, 102],
							1: (-1, 6),
							2: (-1, 12),
							3: (12, 18),
							4: (18, 52) # 367
						},
				'duracion': {
							0: [100, 101, 102],
							1: (-1, 6),
							2: (6, 12),
							3: (12, 18),
							4: (18, 24)
						},
				'capacidad_pago': {
							2: ['No'],
							1: ['Sí'],
							0: ['No sé']
						},
				'credito': {
							0: ['No'],
							2: ['Sí']
						},
				'aumento_insumos': {
							0: ['No'],
							3: ['Sí']
						},
				'aumento_precios': {
							0: ['No'],
							1: ['No, pero lo estoy considerando'],
							3: ['Sí']
						} ,
				'escasez_insumos': {
							0: ['No'],
							3: ['Sí']
						} ,
				'aumento_tipocambio': {
							0: ['No'],
							4: ['Sí']
						}
				}
