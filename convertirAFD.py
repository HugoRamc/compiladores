from estado import *
from automata import *
class convertirAFD(object):
	
	def __init__(self,AFD):
		self.AFD = AFD
		self.edoInicial = AFD.estadoInicial
		self.edosAceptacion = {}
		self.conjuntosSi = []
		self.tablaTransiciones = []
		self.AFNtoAFD()


	def AFNtoAFD(self):
		S0 = self.AFD.cerraduraEpsilon(self.AFD.estadoInicial)
		conjuntosSi.append(S0)
		conj = 0

		for Si in conjuntosSi:
			aux1 = []
			for c in self.AFD.alfabeto:
				aux = self.AFD.ir_a(c,Si)

				if aux not instanceof() conjuntosSi:
					conjuntosSi.append(aux)
					conj+=1
					x = conj
				elif:
					x=aux.index(conjuntosSi)
				else
					x = -1
				aux1.append(x)
				"""aux.append(estadoAceptacionSi)
					duda de donde sacamos el estadoAceptacionSi
				"""
			tablaTransiciones.append(aux1)

	def estadoAceptacionSi(self,Si):
		for i in range(0,len(Si)):
			if Si[i] is estadoAceptacion:
				self.edosAceptacion.append(Si)
		#return estadoAceptacion.token
		
		
obj = convertirAFD()