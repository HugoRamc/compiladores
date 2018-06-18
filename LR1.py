from TablaPointersClass import *
from LR0 import *

class LR1(object):
	"""docstring for LR1"""
	def __init__(self,LR0,Tabla,Items):
		self.LR0 = LR0
		self.Tabla = Tabla
		self.items = Items


	def createLR0(self):
		#There is two scenarios, when we have the first rule and the others
		#print(self.items[0][2:])
		#esta funcion recibe el simbolo, las reglas y los conjuntos de simbolos follow
		firstItem = [self.items[0],"$"]
		S0 = [firstItem]
		self.cerradura(firstItem,S0,[firstItem],"$")
		print("elementos de la cerradura")
		for it in S0:
			print(it)


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
							if posaux+2 <= len(regla)-1:
								simb = []
								self.FirstLR1(regla[pos+2:],simb,[])

								for sim in simb:
									self.cerradura(itaux,salida,cerraduraDone,sim)
							else:
								self.cerradura(itaux,salida,cerraduraDone,parentSimbol)

			else: #el simbolo es un terminal y no genera por lo que termina
				pass



	def FirstLR1(self,cadena,simbolos,firstdone):
		noterm = cadena[0]
		if noterm in LR0.TerminalesA:
			if noterm not in simbolos:
				simbolos.append(noterm)
		else:
			#recorrer todas las reglas en las que se encuentre el no term
			for regla in self.Tabla:
				if noterm == regla[0]:
					if regla  not in firstdone:
						firstdone.append(regla)
						self.FirstLR1(regla[1:],simbolos,firstdone)
			
		






	

#datos de entrada cadena y reglas
cadena = "num + num * ( num + num ) $"
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
LR1.createLR0()