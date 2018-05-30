from TablaPointersClass import *
class LR0(object):
	"""docstring for LR0"""
	def __init__(self,Regla):
		self.LR0punto = "."
		self.pesos = "$"
		self.obj = TablaPointersClass(Regla)
		
	def cerradura(self,item,salida,cerraduraDone):
		#si el item no está en la salida
		
		if item not in salida:
			salida.append(item)
				

		if self.LR0punto != item[len(item)-1]:
			#print("El item es")
			#print(item)
			noterm = item[item.index(self.LR0punto)+1]
			#si es no terminal realizar la cerradura de ese item
			if noterm in self.NoTerminalesA:
				for regla in self.items:
					#si el lado izquierdo coincide con el item
					if regla[0] == noterm:
						if regla not in salida:
							salida.append(regla)
						
						if regla not in cerraduraDone:
							cerraduraDone.append(regla)
							self.cerradura(regla,salida,cerraduraDone)
			else:
				if item not in salida:
					salida.append(item)



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

		if salida:
			print("Resultado de mover con: " + simbolo)
			print(salida)
		return salida



	def irA(self,simbolo,reglas):
		salida = []

		mov = self.mover(simbolo,reglas)
		if len(mov) > 0:
			#print("tiene algo la lista")
			#print(mov)
			for items in mov:
				sal = []
				cerr = [items]
				self.cerradura(items,sal,cerr)
				#salida = salida + sal
				for it in sal:
					if it not in salida:
						salida.append(it)

				#salidaux = list(set.union(set(salida),set(sal1)))
				#salida = salidaux
		else:
			salida = []

		return salida

	def gramaticaExtendida(self,TablaNodes):
		salida = []
		reglaInicial = [str(TablaNodes[0][0]) + "p",str(TablaNodes[0][0])]
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
		#print(items)
		estadosSi = []
		S0 = []
		tablaLR0 = []
		fila0 = list(" ")+self.simbolos
		
		
		tablaLR0.append(fila0)
		print("primer item")
		print(items[0])
		cerr = [items[0]]
		self.cerradura(items[0],S0,cerr)
		print(S0)
		#tablaLR0 = []
		#return tablaLR0

		estadosSi.append(S0)
		flag = True
		for Si in estadosSi:
			filaTabla = []
			filaTabla.append(estadosSi.index(Si))
			for simbolo in self.simbolos:
				
				if simbolo != self.pesos:
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
				else: #si el simbolo es pesos hay que checar que sea el renglon 1
					filaTabla.append(-1)

			tablaLR0.append(filaTabla)

		print("Estados")
		for edo in estadosSi:
			print(edo)


		#ahora a hacer las reducciones
		self.addReducciones(estadosSi,tablaLR0)

		#una vez añadidas las reducciones 

		#self.imprimirTabla(tablaLR0)
		return tablaLR0


	def addReducciones(self,estados,TablaLR0):
		print("Agregar Reducciones\n")
		fila = TablaLR0[0]
		flag = True
		for estado in estados:
			#print(estado)
			for item in estado:
				if self.LR0punto == item[len(item)-1]:
					print("Tenemos un Follow en el edo: "+str(estados.index(estado)))
					print(estados[estados.index(estado)])
					print("El simbolo a sacar follow es: ")
					print(item[0])
					simbs = []
					
					self.obj.Follow(item[0],self.Tabla,simbs)
					simbs = self.limpiarFollow(simbs)
					print(simbs)
					reglaAux = item.copy()
					reglaAux.remove(self.LR0punto)
					


					i = estados.index(estado)+1
					
					for sim in simbs:
						j = fila.index(sim)
						if TablaLR0[i][j] == -1 or TablaLR0[i][j] == "-1":
						#print("Coordenadas: "+str(i) + " , "+str(j))
							numRegla = self.Tabla.index(reglaAux)
							TablaLR0[i][j] = str("R")+str(numRegla)
						else:
							print("Superposition")

	def limpiarFollow(self,simbs):
		salida = []
		for sim in simbs:
			if sim not in salida:
				salida.append(sim)
		return salida
								

	def imprimirTablaf(self,tablaLR0):
		print("Imprimir Tabla")
		tablaLR0 = self.obj.TableFormat(tablaLR0)
		self.obj.printTable(tablaLR0)

	def imprimirTabla(self,tablaLR0):
		for fila in tablaLR0:
			print(fila)

	def setValores(self,Tabla,TerminalesA,NoTerminalesA):
		self.Tabla = Tabla
		self.TerminalesA = TerminalesA
		self.NoTerminalesA = NoTerminalesA
		self.simbolos = self.NoTerminalesA + self.TerminalesA

	def analizarCadena(self,cadena,tablaLR0,reglas):
		#cadena.append(self.pesos)
		print("Analisis de Cadena")
		#Las reglas para este paso tienen el formato de  ['E','E','+','T']
		pila = ["$",0]
		fila = tablaLR0[0]
		self.tablaImprime = []
		it = 0

		while len(cadena)>0:
			#checar si el utlimo simbolo de la pila es un numero
			
			if type(pila[len(pila)-1]) == int:

				if pila[len(pila)-1] == -1 or pila[len(pila)-1] == "-1":
					return False


				#obtenemos la coordenada de la tabla
				i = int(pila[len(pila)-1])+1#se le suma uno a la fila porque la primera fila es de los simbolos
				j = fila.index(cadena[0])

				accion = tablaLR0[i][j]
				if accion == -1 or accion == "-1":#si es una casilla con error
					return False
				elif accion[0] == "d" or accion[0] == 'd':#si la casilla tiene un desplazamiento
					pila.append(cadena[0])#agregamos el primer elemento de la cadena
					pila.append(int(accion[1]))#agregamos el numero del estado que sigue

					cadena = cadena[1:] #eliminamos el elemento de la fila
					
				elif accion[0] == "R" or accion[0] == 'R':#la casilla tiene una reduccion
					#print("Hay reduccion :D")
					numRegla = int(accion[1])#el segundo caracter de la accion es el numero de la regla de la cual hay que hacer reduccion en la pila
					#print(numRegla)
					if numRegla == 0:#cadena aceptada
						return True
					else:

						reg = reglas[numRegla]
						numReducciones = 2 * (len(reg)-1)#se le resta uno porque se quita el lado izquierdo
						#print("Regla con reducciones: "+ str(numReducciones))
						#print(reg)
						#print("pila Antes")
						#print(pila)
						print("Reducciones: "+str(numReducciones))

						pila = pila[0:len(pila)-numReducciones]
						# y se agrega el lado derecho de la recla
						pila.append(reg[0])


						#print("Pila despues")
						#print(pila)

						#la pila no puede terminar con un simbolo tiene que tener un numero
				

					

			elif pila[len(pila)-1] == self.pesos: #checar si el ultimo caracter de la pila es pesos 
				return False
			elif len(pila) <=0: #la pila esta vacía y no hay como seguir analizando la cadena
				return False
			else:
				ip = int(pila[len(pila)-2]) + 1
				aux = pila[len(pila)-1]
				jp = fila.index(aux)
				accion = str(tablaLR0[ip][jp])
				pila.append(int(accion))#agregamos el numero del estado que sigue

			print([pila,accion,str(cadena)])
			self.tablaImprime.append([pila,accion,str(cadena)])

		


"""

#datos de entrada cadena y reglas
cadena = "num + num * ( num + num ) $"
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
TerminalesA.append("$")
LR0.setValores(Tabla,TerminalesA,NoTerminalesA)
#simbolos = NoTerminalesA + TerminalesA


print(LR0.simbolos)

LR0.obj.printTable(Tabla)

#iniciamos proceso de creacion de tabla LR0


items = LR0.createItems(Tabla)

tablaLR0 = LR0.createLR0(items)

LR0.imprimirTablaf(tablaLR0)"""
