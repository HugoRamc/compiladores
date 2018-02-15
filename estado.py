from transcion import *
class estado(object):
	"""docstring for estado"""
	def __init__(self):
		self.idEstado = 0
		self.TransicionesSalientes = []
		self.estadoFinal = False
		
	def añadirTransicion(self):
		trans = transcion()
		pass