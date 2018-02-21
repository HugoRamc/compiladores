from estado import *
from transicion import *

class Automata:
	#al crear un objeto de la clase automata se crea un autómata básico con un caracter, dos estados y una transicion

	def __init__(self,s):
		#el alfabeto serà un caracter que sera convertido en ascii para hacer la transformaciòn
		self.estadosDeAceptacion = {}
		self.estados = {} #Para crear un automata basico se usan dos estado, el de entrada y el aceptaciòn
		self.estadoInicial = 0
		self.alfabeto = []
		#me mandan un arreglo para el alfabeto, si son 2 es porque es un rango.
		if len(s) == 2:
			minimo = ord(s[0])
			maximo = ord(s[1])
			i = 0
			while i <= maximo-minimo:
				self.alfabeto.append(chr(minimo+i))
				i += 1
		else:
			self.alfabeto = s

		edoInicial = Estado()
		edoFinal = Estado()
		edoFinal.enableFinalState()
		edoInicial.addTransicion(self.alfabeto,edoFinal)
		self.estadosDeAceptacion[edoFinal.idEstadoGeneral] = edoFinal
		self.estados[edoInicial.idEstadoGeneral] = edoInicial
		self.estados[edoFinal.idEstadoGeneral] = edoFinal
		self.estadoInicial = edoInicial
		#idEstadoGeneral es el id de todos los estados
		#SI mete un rango de valores, se crean tantos automatas simples que tenga ese rango y se unen.
		#. -alfabeto .
	def unir(self,f2):
	#Oscar
	#Cuando se elija combinar un automata o unir automatas, recordar que se tienen que combinar el alfabeto de cada uno
		nuevoIni = Estado()
		nuevoFin = Estado()
		nuevoIni.addTransicion(["Ǝ"],self.estadoInicial)
		nuevoIni.addTransicion(["Ǝ"],f2.estadoInicial)

		for idEstado in self.estadosDeAceptacion:
			self.estadosDeAceptacion[idEstado].addTransicion(["Ǝ"],nuevoFin)
			self.estadosDeAceptacion[idEstado].disableFinalState()

		for idEstado in f2.estadosDeAceptacion:
			f2.estadosDeAceptacion[idEstado].addTransicion(["Ǝ"],nuevoFin)
			f2.estadosDeAceptacion[idEstado].disableFinalState()

		nuevoFin.enableFinalState()
		self.estados[nuevoIni.idEstadoGeneral] = nuevoIni
		self.estados[nuevoFin.idEstadoGeneral] = nuevoFin
		self.estadoInicial = nuevoIni
		self.estadosDeAceptacion.clear()
		self.estadosDeAceptacion[nuevoFin.idEstadoGeneral] = nuevoFin
		self.estados.update(f2.estados)
		print(self.estados)
		print(self.estados[1].transicionesSalientes[1].simbolos)
		self.alfabeto.extend(f2.alfabeto)
		print(self.estados[1].transicionesSalientes[1].simbolos)

		for e in self.estados:
			for t in self.estados[e].transicionesSalientes:
				print('\t Estos de SELF con f2: ',e)
				print(self.estados[e].transicionesSalientes[t].simbolos)
				print('\t Transiciones de SELF con f2')
				print(self.estados[e].transicionesSalientes[t].idEstadoDestino)


	def concatenar(self,f2):
		for e in self.estadosDeAceptacion:
			self.estadosDeAceptacion[e].disableFinalState()
			for t in f2.estadoInicial.transicionesSalientes:
				self.estadosDeAceptacion[e].addTransicion(f2.estadoInicial.transicionesSalientes[t].simbolos,f2.estadoInicial.transicionesSalientes[t].idEstadoDestino)
		#Estados
		#Estados de aceptacion
		#Estado inicial
		f2.estados.pop(f2.estadoInicial.idEstadoGeneral)
		self.estadosDeAceptacion.clear()
		self.estadosDeAceptacion.update(f2.estadosDeAceptacion)
		self.estados.update(f2.estados)
		self.alfabeto.extend(f2.alfabeto)
		
	def cerradura_kleene(self):

	#Oscar
		return kleeneAutomata

	def cerradura_positiva(self):
	#Luis
		pass

	def ir_a(self):
	#Luis
	#Ir_a utiliza a mover para verificar un conjunto de estados y la direcciòn de a donde va con un simbolo del alfabeto.
		pass

	def mover_C(self):
	#Oscar
		return moverEstados

	def mover(self):
	#Oscar
		return moverEstados

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

	def epsilon():
		pass

if __name__ == "__main__":
	alfabeto = ["a","c"]
	a1 = Automata(alfabeto)
	alfabeto = ["d","e","f"]
	a2 = Automata(alfabeto)
	a1.unir(a2)
