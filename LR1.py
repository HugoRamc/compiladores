from TablaPointersClass import *
from LR0 import *

class LR1(object):
	"""docstring for LR1"""
	def __init__(self,LR0,Tabla,Items):
		self.LR0 = LR0
		self.Tabla = Tabla
		self.items = Items

	#esta funcion recibe el item a calcular la cerradura, un arreglo donde se almacenara el resultado de la cerradura, un arreglo para saber si ya se calculo la cerradura y el simbolo padre
	def cerradura(self,item,salida,cerraduraDone,parentSimbol):
		#General form of an item [A -> . a B w, c]
		if item not in salida:
			salida.append(item)

		pos = item[0].index(".")
		if pos+1 <= len(item[0])-1:#the point is not at the last position
			noterm = item[0][pos+1]

			if noterm in self.LR0.NoTerminalesA: #el simbolo que viene es un no terminal y genera
				#obtener las reglas en las que coinciden el noterminal
				for regla in self.items:
					if regla[0] == noterm:#regla que coincida con el simbolo
						itaux = [regla,parentSimbol]
						if itaux not in salida:
							salida.append(itaux)

						if itaux not in cerraduraDone:
							cerraduraDone.append(itaux)
							posaux = regla.index(".")
							if posaux+2 <= len(regla)-1:#saber si la regla tiene first
								simb = []
								self.FirstLR1(regla[pos+2:],simb,[])
								
								if simb:
									self.cerradura(itaux,salida,cerraduraDone,simb[0])
								#else:
									#self.cerradura(itaux,salida,cerraduraDone,simb)

							else:#calcularle la cerradura a la regla con el simbolo del padre con el que viene
								self.cerradura(itaux,salida,cerraduraDone,parentSimbol)

	def mover(self,simbolo,reglas):
		#print(reglas)
		salida = []
		for regl in reglas:
			#print(regla)
			regla = regl[0]
			lastsimb = regla[len(regla)-1]
			if self.LR0.LR0punto != lastsimb:
				simb = regla[regla.index(self.LR0.LR0punto)+1]
				if simb == simbolo:

					newItem = regla[0:regla.index(self.LR0.LR0punto)]
					newItem.append(regla[regla.index(self.LR0.LR0punto)+1])
					newItem.append(self.LR0.LR0punto)
					newItem = newItem + regla[regla.index(self.LR0.LR0punto)+2:]

					salida.append([newItem,regl[1]])
		return salida

	def irA(self,simbolo,edo):
		#cerradura de mover
		salida = []
		mover = self.mover(simbolo,edo)
		if mover:

			for it in mover:
				aux = []
				self.cerradura(it,aux,[it],it[1])
				salida = salida + aux
		else:
			salida = []
		return salida



	def createLR1(self):
		print("creating LR1")
		TablaLR1 = []
		fila0 = list(" ")+self.LR0.simbolos
		TablaLR1.append(fila0)
		#There is two scenarios, when we have the first rule and the others
		#print(self.items[0][2:])
		#esta funcion recibe el simbolo, las reglas y los conjuntos de simbolos follow
		firstItem = [self.items[0],"$"]
		S0 = [firstItem]
		self.cerradura(firstItem,S0,[firstItem],"$")


		#sal = self.irA('f',S0)
		#print(sal)

		for edo in S0:
			print(edo)
		estadosSi = []
		estadosSi.append(S0)

		for Si in estadosSi:
			filaTabla = []
			filaTabla.append(estadosSi.index(Si))
			for simb in self.LR0.simbolos:
				edo = self.irA(simb,Si)

				if not edo:#si se encuentra vacio 
					filaTabla.append(-1)
				else:
					if edo not in estadosSi:#si el estado no se encuentra dentro del conjunto de estados a analizar
						estadosSi.append(edo)

					if simb in self.LR0.NoTerminalesA:
						filaTabla.append(estadosSi.index(edo))
					else:
						filaTabla.append("d"+str(estadosSi.index(edo)))
			TablaLR1.append(filaTabla)

		#print("estadoS0")
		#nS0 = estadosSi[0]
		#for item in nS0:
			#print("estado: "+str(estadosSi.index(si)))
			#print(si)
			#print(item)
		self.addReducciones(TablaLR1,estadosSi)
		#self.LR0.imprimirTablaf(TablaLR1)

		return TablaLR1
		
	def FirstLR1(self,cadena,simbolos,firstdone):
		if cadena:
			noterm = cadena[0]
			if noterm in self.LR0.TerminalesA:
				if noterm not in simbolos:
					simbolos.append(noterm)
			else:
				#recorrer todas las reglas en las que se encuentre el no term
				for regla in self.Tabla:
					if noterm == regla[0]:
						if regla  not in firstdone:
							firstdone.append(regla)
							self.FirstLR1(regla[1:],simbolos,firstdone)

	def addReducciones(self,TablaLR1,estadosSi):
		print("reglas de reducción")
		for reg in self.Tabla:
			print(reg)
		simbols = TablaLR1[0]
		for Si in estadosSi:

			for item in Si:#recordar que el item es una lista de dos elementos
				#obtener los items en los cuales el punto está hasta el final
				regla = item[0]
				simb = item[1]

				if regla[len(regla)-1] == ".":
					reglaaux = regla.copy()
					#print("Reducción en "+str(estadosSi.index(Si)))
					#print(str(regla) + str(simb))
					reglaaux.remove(".")

					i = estadosSi.index(Si)+1
					j = simbols.index(simb)
					numRegla = self.Tabla.index(reglaaux)

					if TablaLR1[i][j] == -1 or TablaLR1[i][j] == "-1":
						TablaLR1[i][j] = str("R")+str(numRegla)
					else:
						print("superposition")

					
		print("reducciones terminadas")

	def analizarCadena(self,cadena,TablaLR1):
		#cadena.append(self.pesos)
		print("Analisis de Cadena")
		#Las reglas para este paso tienen el formato de  ['E','E','+','T']
		pila = ["$",0]
		fila = TablaLR1[0]
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

				accion = TablaLR1[i][j]
				if accion == -1 or accion == "-1":#si es una casilla con error
					return False
				elif accion[0] == "d" or accion[0] == 'd':#si la casilla tiene un desplazamiento
					pila.append(cadena[0])#agregamos el primer elemento de la cadena
					pila.append(int(accion[1:]))#agregamos el numero del estado que sigue

					cadena = cadena[1:] #eliminamos el elemento de la fila
					
				elif accion[0] == "R" or accion[0] == 'R':#la casilla tiene una reduccion
					#print("Hay reduccion :D")
					numRegla = int(accion[1:])#el segundo caracter de la accion es el numero de la regla de la cual hay que hacer reduccion en la pila
					#print(numRegla)
					if numRegla == 0:#cadena aceptada
						return True
					else:

						reg = self.Tabla[numRegla]
						numReducciones = 2 * (len(reg)-1)#se le resta uno porque se quita el lado izquierdo
						print("Reducciones: "+str(numReducciones))

						pila = pila[0:len(pila)-numReducciones]
						# y se agrega el lado derecho de la recla
						pila.append(reg[0])


			elif pila[len(pila)-1] == self.LR0.pesos: #checar si el ultimo caracter de la pila es pesos 
				return False
			elif len(pila) <=0: #la pila esta vacía y no hay como seguir analizando la cadena
				return False
			else:
				ip = int(pila[len(pila)-2]) + 1
				aux = pila[len(pila)-1]
				jp = fila.index(aux)
				accion = str(TablaLR1[ip][jp])
				pila.append(int(accion))#agregamos el numero del estado que sigue

			print([pila,accion,str(cadena)])
			self.tablaImprime.append([pila,accion,str(cadena)])


				
"""
#datos de entrada cadena y reglas
cadena = "f $"
cadena = cadena.split(" ")
Regla = sys.argv[1:]


#utilizamos los metodos definidos en la clase TablaPointersClass para obtener el formato de las reglas

LR0 = LR0(Regla)

Tabla = LR0.obj.createNodes(Regla) #esta tabla contiene todas las reglas pero sin punto
LR0.obj.blank(Tabla)
Tabla = LR0.gramaticaExtendida(Tabla)
#To this point we have the extended grammar we update all the simbols
LR0.obj.resetsimbolos(Tabla)
NoTerminalesA = LR0.obj.NoTerminalesA
TerminalesA = LR0.obj.TerminalesA
TerminalesA.append("$")
LR0.setValores(Tabla,TerminalesA,NoTerminalesA)
#with the simbols now updated, now we proceed to create all the items
items = LR0.createItems(Tabla)
#now having the items we proceed to create the 
LR1 = LR1(LR0,Tabla,items)
TablaLR1 = LR1.createLR1()
#tabAux = TablaLR1.copy()
#LR1.LR0.imprimirTablaf(tabAux)
LR1.analizarCadena(cadena,TablaLR1)"""