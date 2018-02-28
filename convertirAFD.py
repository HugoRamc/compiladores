from estado import *
from automata import *
class convertirAFD(object):
	
	def __init__(self,AFD):
		self.AFD = AFD
		self.edoInicial = AFD.estadoInicial
		self.edosAceptacion = {}
		self.conjuntosSi = []
		self.tablaTransiciones = []
		print("Estamos llamando al objeto :D")
		self.AFNtoAFD()


	def AFNtoAFD(self):
		conjuntosSi = []
		S0 = self.AFD.cerradura_epsilon(self.AFD.estadoInicial)
		conjuntosSi.append(S0)
		conj = 0

		for Si in conjuntosSi:
			aux1 = []
			for c in self.AFD.alfabeto:
				aux = self.AFD.ir_a(c,Si)

				if len(aux) >= 1:
					if aux not in conjuntosSi:
						conjuntosSi.append(aux)
						conj+=1
						x = conj
					else:
						x=aux.index(conjuntosSi)
				else:
					x = -1
				aux1.append(x)
				if self.AFD.isEstadoAceptacion(Si):
					aux1.append(int(self.AFD.token))
				else:
					aux1.append(int("-1"))

				#if conjuntoSi is edoAceptacion append(Token) else append -1
				#aux.append(estadoAceptacionSi)
					
			self.tablaTransiciones.append(aux1)

			for fila in self.tablaTransiciones:
				print(fila)

		print(self.tablaTransiciones)

	def getTabla(self):
		return self.tablaTransiciones

	def estadoAceptacionSi(self,Si):
		for i in range(0,len(Si)):
			if Si[i] is estadoAceptacion:
				self.edosAceptacion.append(Si)
		#return estadoAceptacion.token
		
		