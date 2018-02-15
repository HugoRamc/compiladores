from transcion import *
class estado(object):
	"""docstring for estado"""
	def __init__(self,idEstado):
		self.idEstado = idEstado
		self.TransicionesSalientes = []
		self.estadoFinal = False

	def añadirTransicion(self,simbolo,idEstadoDestino):
		trans = transcion(simbolo,idEstadoDestino)
		pass

	def enableEstadoFinal(self):
		self.estadoFinal = True
