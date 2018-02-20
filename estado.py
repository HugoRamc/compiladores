from transicion import *

class Estado:

	idEstadoGlobal = 0
	def __init__(self):
		self.transicionesSalientes = {}
		self.estadoAceptacion = False
		Estado.idEstadoGlobal += 1
		self.idEstadoGeneral = Estado.idEstadoGlobal

	def addTransicion(self,simbolo,idEstadoDestino):
		trans = Transicion(simbolo,idEstadoDestino)
		self.transicionesSalientes[self.idEstadoGeneral] = trans


	def enableFinalState(self):
		self.estadoFinal = True

	def disableFinalState(self):
		self.estadoFinal = False
