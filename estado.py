from transicion import *

class Estado:

	idEstadoGlobal = 0 #Sirve para identificar a los estados
	def __init__(self):
		self.transicionesSalientes = {}
		self.estadoAceptacion = False
		self.idTransicion = 0 #Sirve para identificar a las transiciones
		Estado.idEstadoGlobal += 1
		self.idEstadoGeneral = Estado.idEstadoGlobal #Sirve para identificar al estado

	def addTransicion(self,simbolo,idEstadoDestino):
		trans = Transicion(simbolo,idEstadoDestino)
		self.idTransicion += 1
		self.transicionesSalientes[self.idTransicion] = trans


	def enableFinalState(self):
		self.estadoFinal = True

	def disableFinalState(self):
		self.estadoFinal = False
