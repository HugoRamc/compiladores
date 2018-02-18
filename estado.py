from transicion import *
class estado(object):
	"""docstring for estado"""
	def __init__(self,idEstado):
		self.idEstado = idEstado
		self.TransicionesSalientes = []
		self.estadoAceptacion = False

	def addTransicion(self,simbolo,idEstadoDestino):
		trans = transcion(simbolo,idEstadoDestino)
		self.transicionesSalientes[self.idEstado] = trans


	def enableFinalState(self):
		self.estadoFinal = True

	def disableFinalState(self):
		self.estadoFinal = False

