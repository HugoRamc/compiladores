from estado import *
from automata import *
class convertirAFD(object):

	def __init__(self,AFN,pilaaux):
		print("Conversión a AFD")
		self.AFD = AFN
		self.edoInicial = AFN.estadoInicial
		self.edosAceptacion = {}
		self.conjuntosSi = []
		self.tablaTransiciones = []
		self.tablaTransiciones2 = []
		if not pilaaux:
			pilaaux.append(self.AFD)
		self.AFNtoAFD(pilaaux)


	def AFNtoAFD(self,pilaaux):

		archivo = open("tablaAFD.txt","w")
		conjuntosSi = []
		S0 = self.AFD.cerradura_epsilon(self.AFD.estadoInicial)
		conjuntosSi.append(S0)
		conj = 0
		aux2 = []
		aux2.append("")
		aux2.extend(self.AFD.alfabeto)
		aux2.append("EdoAcep")
		self.tablaTransiciones2.append(aux2)
		straux = ""
		for item in aux2:
			straux += str(item)+","
		straux = straux[0:len(straux)-1]
		archivo.write(straux + "\n")

		for Si in conjuntosSi:
			aux1 = []
			aux2 = []
			aux2.append("S"+str(conjuntosSi.index(Si)))
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
				aux2.append(x)

			#print("dsds: ",self.AFD.isEstadoAceptacion(Si))

			tokenaux = 0
			if self.AFD.isEstadoAceptacion(Si):
				for edo in Si:
					for automata in pilaaux:
						if edo.idEstadoGeneral in automata.estadosDeAceptacion or edo in automata.estadosDeAceptacion:
							tokenaux = automata.token*10
				aux1.append(tokenaux)
				aux2.append(tokenaux)
			else:
				aux1.append(-1)
				aux2.append(-1)

			straux = ""
			for item in aux2:
				straux += str(item)+","
			straux = straux[0:len(straux)-1]
			archivo.write(straux + "\n")

			self.tablaTransiciones.append(aux1)
			self.tablaTransiciones2.append(aux2)

		archivo.close()



		print("\nTerminado")

	def getTabla(self):
		return self.tablaTransiciones2

	def leeTabla():
		tablaTransiciones = []
		archivo = open("tablaAFD.txt","r")
		for line in archivo:
			line = line.replace("\n","")
			lin = line.split(",")
			tablaTransiciones.append(lin)

		return tablaTransiciones

	def generaAlfabeto():
		pass
