from TablaPointersClass import *
class LR0(object):
	"""docstring for LR0"""
	def __init__(self,Regla):
		self.LR0punto = "."
		self.pesos = "$"
		self.obj = TablaPointersClass(Regla)
		
	def cerradura(self,item,salida):
		#print(type(item))
		#si el punto está en la ultima posicion
		if item not in salida:
			salida.append(item)
			if self.LR0punto == item[len(item)-1]:
				salida.append(item)
			else:
				print("El item es")
				print(item)
				noterm = item[item.index(self.LR0punto)+1]
				#si es no terminal realizar la cerradura de 
				if noterm in self.NoTerminalesA:
					for regla in self.items:
						#si la regla coincide
						if regla[0] == noterm:
							if regla not in salida:
								salida.append(regla)

						#una vez agregada la regla a la lista se checa si esa regla deriva a otras reglas
						self.cerradura(regla,salida)

					
				else:
					if item not in salida:
						salida.append(item)

			#for elemento in salida:
				#print(elemento)
		return salida



	def mover(self,simbolo,reglas):

		#print(reglas)
		salida = []
		for regla in reglas:
			#print(regla)
			lastsimb = regla[len(regla)-1]
			if self.LR0punto != lastsimb:
				simb = regla[regla.index(self.LR0punto)+1]
				if simb == simbolo:

					newItem = regla[0:regla.index(self.LR0punto)]
					newItem.append(regla[regla.index(self.LR0punto)+1])
					newItem.append(self.LR0punto)
					newItem = newItem + regla[regla.index(self.LR0punto)+2:]

					salida.append(newItem)

		print("Resultado de mover con: " + simbolo)
		print(salida)
		return salida



	def irA(self,simbolo,reglas):
		sal = []
		salida = []

		mov = self.mover(simbolo,reglas)
		if len(mov) > 0:
			#print("tiene algo la lista")
			#print(mov)
			
			for items in mov:
				sal = []
				sal1 = self.cerradura(items,sal)
				salida = salida + sal1
				#salidaux = list(set.union(set(salida),set(sal1)))
				#salida = salidaux
		else:
			salida = []

		return salida

	def gramaticaExtendida(self,TablaNodes):
		salida = []
		reglaInicial = [str(TablaNodes[0][0]) + "'",str(TablaNodes[0][0]),self.pesos]
		salida.append(reglaInicial)

		salida = salida + TablaNodes
		return salida


	def createItems(self,TablaNodes):
		#se crea primero la primera regla para aumentar la gramática
		print("Lista de items")
		salida = []
		#itemInicial = [str(TablaNodes[0][0]) + "'",self.LR0punto,str(TablaNodes[0][0]),self.pesos]
		#print(itemInicial)
		#salida.append(itemInicial)

		for regla in TablaNodes:
			newItem=[]

			for i in range(0,len(regla)):
				if i ==0:
					newItem.append(regla[i])
					newItem.append(self.LR0punto)
				else:
					newItem.append(regla[i])
			print(newItem)
			salida.append(newItem)

		self.items = salida
		return salida

	def createLR0(self,items):
		estadosSi = []
		edos = []
		tablaLR0 = []
		fila0 = list(" ")+self.simbolos
		tablaLR0.append(fila0)
		print("estadoInicial")
		S0 = self.cerradura(items[0],edos)

		estadosSi.append(S0)
		flag = True
		for Si in estadosSi:
			filaTabla = []
			filaTabla.append(estadosSi.index(Si))
			for simbolo in self.simbolos:
				edo = self.irA(simbolo,Si)

				if not edo:#si se encuentra vacio 
					filaTabla.append(-1)
				else:
					if edo not in estadosSi:
						estadosSi.append(edo)

					if simbolo in self.NoTerminalesA:
						filaTabla.append(estadosSi.index(edo))
					else:
						filaTabla.append("d"+str(estadosSi.index(edo)))
			tablaLR0.append(filaTabla)

		#ahora a hacer las reducciones
		self.addReducciones(estadosSi,tablaLR0)

		#una vez añadidas las reducciones 

		#self.imprimirTabla(tablaLR0)
		return tablaLR0
		

	def addReducciones(self,estados,TablaLR0):
		fila = TablaLR0[0]
		for estado in estados:

			for item in estado:
				if self.LR0punto == item[len(item)-1]:
					print("Tenemos un Follow en el edo: "+str(estados.index(estado)))
					print(item)
					simbs = []
					print("Follow de: "+str(item[0]))
					self.obj.Follow(item[0],self.Tabla,simbs)
					print(simbs)
					reglaAux = item.copy()
					reglaAux.remove(".")

					i = estados.index(estado)+1
					
					for sim in simbs:
						j = fila.index(sim)
						#print("Coordenadas: "+str(i) + " , "+str(j))
						
						numRegla = self.Tabla.index(reglaAux)
						
						TablaLR0[i][j] = str("R")+str(numRegla)

	def imprimirTabla(self,tablaLR0):
		print("Imprimir Tabla")
		tablaLR0 = self.obj.TableFormat(tablaLR0)
		self.obj.printTable(tablaLR0)

	def setValores(self,Tabla,TerminalesA,NoTerminalesA):
		self.Tabla = Tabla
		self.TerminalesA = TerminalesA
		self.NoTerminalesA = NoTerminalesA
		self.simbolos = self.NoTerminalesA + self.TerminalesA

	def analizarCadena(self,cadena):
		pila = ["$",0]
		
		
"""
#datos de entrada cadena y reglas
cadena = "( num + num ) * num - num $"
cadena = cadena.split(" ")
Regla = sys.argv[1:]


#utilizamos los metodos definidos en la clase TablaPointersClass para obtener el formato de las reglas
LR0 = LR0(Regla)
Tabla = LR0.obj.createNodes(Regla) #esta tabla contiene todas las reglas pero sin punto
LR0.obj.blank(Tabla)

Tabla = LR0.gramaticaExtendida(Tabla)
LR0.obj.resetsimbolos(Tabla)

NoTerminalesA = LR0.obj.NoTerminalesA
TerminalesA = LR0.obj.TerminalesA
LR0.setValores(Tabla,TerminalesA,NoTerminalesA)
#simbolos = NoTerminalesA + TerminalesA

LR0.obj.printTable(Tabla)

#iniciamos proceso de creacion de tabla LR0

items = LR0.createItems(Tabla)
tablaLR0 = LR0.createLR0(items)"""
