from estado import *
from transicion import *

class automata(object):

	##al crear un objeto de la clase automata se crea un autómata básico con un caracter, dos estados y una transicion
	def __init__(self,alphabeto,idEstadoInicial):
		self.estadosDeAceptacion = {}
		self.estados = {}
		self.estadoInicial = IntVar()
		self.alphabeto = [alphabeto]


		edoInicial = estado(idEstadoInicial)
		edoFinal = estado(idEstadoInicial+1)
		edoFinal.enableFinalState()
		edoInicial.addTransicion(alphabeto,idEstadoInicial+1)

		self.estadosDeAceptacion[idEstadoInicial+1] = edoFinal
		self.estados[idEstadoInicial] = edoInicial
		self.estados[idEstadoInicial+1] = edoFinal
		self.estadoInicial = idEstadoInicial



	