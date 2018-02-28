from estado import *
from automata import *
class convertirAFD(object):
	
	def __init__(self,AFD):
		print("Conversión a AFD")
		self.AFD = AFD
		self.edoInicial = AFD.estadoInicial
		self.edosAceptacion = {}
		self.conjuntosSi = []
		self.tablaTransiciones = []
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

				#si la operacion ir a trae un conjunto mayor a 
				if len(aux) > 0:
					if aux not in conjuntosSi:
						conjuntosSi.append(aux)
						conj+=1
						x = conj
					else:
						x=conjuntosSi.index(aux)
				else:
					x = -1
				
				aux1.append(x)

			if self.AFD.isEstadoAceptacion(Si):
				aux1.append(int(self.AFD.token))
			else:
				aux1.append(int("-1"))	

					
			self.tablaTransiciones.append(aux1)

		for fila in self.tablaTransiciones:
			print(fila)

		print("\nTerminado")

	def getTabla(self):
		return self.tablaTransiciones

		
		