from estado import *
from transicion import *

class Automata:

	#variable para controlar los tokens
	idToken = 0
	epsilon = ["Ǝ"]
	vacio = ["Ø"]
	#al crear un objeto de la clase automata se crea un autómata básico con un caracter, dos estados y una transicion
	def __init__(self,s):
		Automata.idToken +=1
		self.token = Automata.idToken
		self.estadosDeAceptacion = {}
		self.estados = {} #Para crear un automata basico se usan dos estado, el de entrada y el aceptaciòn
		#self.alfabeto = {}
		self.alfabeto = []
		for i in s:
			self.alfabeto.append(i)
		edoInicial = Estado()
		edoFinal = Estado()
		edoFinal.enableFinalState()
		edoInicial.addTransicion(s,edoFinal)
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

		alfaux = list(set.union(set(self.alfabeto),set(f2.alfabeto)))

		self.alfabeto = alfaux


	def concatenar(self,f2):
		for e in self.estadosDeAceptacion:
			for t in f2.estadoInicial.transicionesSalientes:
				self.estadosDeAceptacion[e].addTransicion(f2.estadoInicial.transicionesSalientes[t].simbolos,f2.estadoInicial.transicionesSalientes[t].idEstadoDestino)
				self.estadosDeAceptacion[e].disableFinalState()
			#self.estadosDeAceptacion[e].addTransicion(["Ǝ"],f2.estadoInicial)
		f2.estados.pop(f2.estadoInicial.idEstadoGeneral)
		self.estadosDeAceptacion.clear()
		self.estadosDeAceptacion.update(f2.estadosDeAceptacion)
		self.estados.update(f2.estados)
		alfaux = list(set.union(set(self.alfabeto),set(f2.alfabeto)))

		self.alfabeto = alfaux


	def cerradura_kleene(self):
		#Oscar
		nuevoIni = Estado()
		nuevoFin = Estado()
		nuevoIni.addTransicion(["Ǝ"],self.estadoInicial)
		nuevoIni.addTransicion(["Ǝ"],nuevoFin)
		for e in self.estadosDeAceptacion:
			self.estadosDeAceptacion[e].addTransicion(["Ǝ"],nuevoFin)
			self.estadosDeAceptacion[e].addTransicion(["Ǝ"],self.estadoInicial)
			self.estadosDeAceptacion[e].disableFinalState()

		nuevoFin.enableFinalState()
		self.estadosDeAceptacion.clear()
		self.estadosDeAceptacion[nuevoFin.idEstadoGeneral] = nuevoFin
		self.estados[nuevoIni.idEstadoGeneral] = nuevoIni
		self.estados[nuevoFin.idEstadoGeneral] = nuevoFin
		self.estadoInicial = nuevoIni

	def cerradura_positiva(self):
	#Luis
		nuevoIni = Estado()
		nuevoFin = Estado()
		nuevoIni.addTransicion(["Ǝ"],self.estadoInicial)

		for idEstado in self.estadosDeAceptacion:
			self.estadosDeAceptacion[idEstado].addTransicion(["Ǝ"],nuevoFin)
			self.estadosDeAceptacion[idEstado].addTransicion(["Ǝ"],self.estadoInicial)
			self.estadosDeAceptacion[idEstado].disableFinalState()

		nuevoFin.enableFinalState()
		self.estadosDeAceptacion.clear()
		self.estadosDeAceptacion[nuevoFin.idEstadoGeneral] = nuevoFin
		self.estados[nuevoIni.idEstadoGeneral] = nuevoIni
		self.estados[nuevoFin.idEstadoGeneral] = nuevoFin
		self.estadoInicial = nuevoIni

	def cerradura_interrogacion(self):
		#Luis
		nuevoIni = Estado()
		nuevoFin = Estado()
		nuevoIni.addTransicion(["Ǝ"],self.estadoInicial)
		nuevoIni.addTransicion(["Ǝ"],nuevoFin)

		for e in self.estadosDeAceptacion:
			self.estadosDeAceptacion[e].addTransicion(["Ǝ"],nuevoFin)
			self.estadosDeAceptacion[e].disableFinalState()

		nuevoFin.enableFinalState()
		self.estadosDeAceptacion.clear()
		self.estadosDeAceptacion[nuevoFin.idEstadoGeneral] = nuevoFin
		self.estados[nuevoIni.idEstadoGeneral] = nuevoIni
		self.estados[nuevoFin.idEstadoGeneral] = nuevoFin
		self.estadoInicial = nuevoIni

	def ir_a(self,simbolo,estados):
	#Luis
	#Estados es un arreglo de arreglos.
	#Ir_a utiliza a mover para verificar un conjunto de estados y la direcciòn de a donde va con un simbolo del alfabeto.
		R = []
		for e in estados:
			R.append(self.mover(simbolo,e))
		return self.cerradura_epsilon_C(R)

	def mover_C(self,simbolo,estados): #para moverse por todos los estados
	#Oscar
		R = []
		#Estados es un diccionario
		for e in estados:
			R.append(self.mover(simbolo,estados[e]))

		return R #arreglo de arreglos con estados

	def mover(self,simbolo,estado): #Para moverse por un estado
	#Oscar
		R = []
		for t in estado.transicionesSalientes:
			if simbolo in estado.transicionesSalientes[t].simbolos:
				R.append(estado.transicionesSalientes[t].idEstadoDestino)
		return R

	def cerradura_epsilon_C(self,estados):#esta cerradura epsilon es para el conjunto de estados
	#Hugo
		conjSalida = []
		estado_aux = []
		for estado in estados:
			if estado:
				for e in estado:
					estado_aux.append(e)

		for estado in estado_aux:
			conjSalida.extend(self.cerradura_epsilon(estado))

		return conjSalida

	def cerradura_epsilon(self,estado):#esta cerradura epsilon es para solo un estado
	#Hugo

		conjSalida = []
		idConj = []
		pilaEstados = []
		pilaEstados.append(estado)
		entrar = False

		while pilaEstados:
			r = pilaEstados.pop()
			if not r.idEstadoGeneral in idConj:
				conjSalida.append(r)
				idConj.append(r.idEstadoGeneral)
				for t in r.transicionesSalientes:
					if "Ǝ" in r.transicionesSalientes[t].simbolos:
						entrar = True
						pilaEstados.append(r.transicionesSalientes[t].idEstadoDestino)

		return conjSalida

	def analizaCadena(self,cadena):
		r = self.cerradura_epsilon(self.estadoInicial)
		#print(self.estadoInicial.idEstadoGeneral)
		pila = []
		for s in cadena:
			c = self.ir_a(s,r)
			if not c:
				return False
				#return False
			else:
				r = c

		if self.isEstadoAceptacion(c):
			return True
		else:
			return False

	def isEstadoAceptacion(self,c):
		for edo in c:
			if edo.idEstadoGeneral in self.estadosDeAceptacion:
				return True
		return False


	def getToken(self):
		return self.token

	def union_especial(self, automatas): #Une n automatas con n transiciones epsilon a un nuevo estado inicial
		nuevoIni = Estado()

		nuevoIni.addTransicion(["Ǝ"],self.estadoInicial)
		for a in range(len(automatas)):
			nuevoIni.addTransicion(["Ǝ"], automatas[a].estadoInicial)

		self.estados[nuevoIni.idEstadoGeneral] = nuevoIni
		self.estadoInicial = nuevoIni

		for a in range(len(automatas)):
			self.estadosDeAceptacion.update((automatas[a].estadosDeAceptacion))
			self.estados.update(automatas[a].estados)
			alfaux = list(set.union(set(self.alfabeto),set(automatas[a].alfabeto)))

			self.alfabeto = alfaux

#1 a u b
#1 kleene a u b
#3 c +
#1 concatenacion de 1 y 3
#4 d+
#5 e cerradura_kleene
#6 f +
#4 concatenacion 4 y 5
#4 union de 4 y 6
#1 union 1 y 4
