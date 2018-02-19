from estado import *
from transicion import *

class Automata:
	#al crear un objeto de la clase automata se crea un autómata básico con un caracter, dos estados y una transicion

	def __init__(self,alphabeto,idEstadoInicial):
		self.estadosDeAceptacion = {}
		self.estados = {} #Para crear un automata basico se usan dos estado, el de entrada y el aceptaciòn
		self.estadoInicial = IntVar()
		self.alphabeto = [alphabeto]
		edoInicial = Estado(idEstadoInicial)
		edoFinal = Estado(idEstadoInicial+1)
		edoFinal.enableFinalState()
		edoInicial.addTransicion(alphabeto,idEstadoInicial+1)
		self.estadosDeAceptacion[idEstadoInicial+1] = edoFinal
		self.estados[idEstadoInicial] = edoInicial
		self.estados[idEstadoInicial+1] = edoFinal
		self.estadoInicial = idEstadoInicial


	    def unir(self,Automata):
			#Oscar
			#Cuando se elija ombinar un automata o unir automatas, recordar que se tienen que combinar el alfabeto de cada uno
	        pass

	    def concatenar(self,Automata):
			#Oscar
	        pass

	    def cerradura_kleene(self):

			#Oscar
			pass

	    def cerradura_positiva(self):
			#Luis
	        pass

	    def ir_a(self):
			#Luis
			#Ir_a utiliza a mover para verificar un conjunto de estados y la direcciòn de a donde va con un simbolo del alfabeto.
			pass

	    def mover_C(self):
			#Oscar
			pass

	    def mover(self):
			#Oscar
			pass

	    def cerradura_epsilon_C(self):
			#Hugo
	        pass

	    def cerradura_epsilon(self,estado):
			#Hugo
	        conjEstados = []
	        pilaEstados = []

	        pilaEstados.append(estado)

	        while len(pilaEstados)==0:
	            pass
