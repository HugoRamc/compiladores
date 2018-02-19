from transicion import *

class Estado:
	
	idEstadoGlobal = 0
	def __init__(self,idEstado):
		self.idEstado = idEstado
		self.TransicionesSalientes = []
		self.estadoAceptacion = False
		estado.idEstadoGlobal += 1
		self.idEstadoGeneral = estado.idEstadoGlobal

	def addTransicion(self,simbolo,idEstadoDestino):
		trans = transcion(simbolo,idEstadoDestino)
		self.transicionesSalientes[self.idEstado] = trans


	def enableFinalState(self):
		self.estadoFinal = True

	def disableFinalState(self):
		self.estadoFinal = False
