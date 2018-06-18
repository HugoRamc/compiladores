import sys
import copy

class TablaPointersClass(object):
	"""docstring for TablaPointersClass"""
	def __init__(self,Regla):
		self.Tabla = self.createNodes(Regla)
		self.blank(self.Tabla)
		
		self.resetsimbolos(self.Tabla)
	
	def resetsimbolos(self,Tabla):
		self.NoTerminalesA = self.NoTerminales(Tabla)
		self.TerminalesA = self.Terminales(Tabla)
		self.NoTerminalesA = list(set(self.NoTerminalesA))
		self.TerminalesA = list(set(self.TerminalesA))
		

	def generateLL1(self):
		self.LL1 = self.GenerateLL1(self.Tabla,self.NoTerminalesA,self.TerminalesA)
		self.printTable(self.LL1)

	def analizarCadena(self,cadena):
		aux = self.analizar(cadena,self.NoTerminalesA,self.TerminalesA)
		if self.validate(cadena,self.Tabla,self.LL1):
			return True
		else:
			return False

	def getTabla(self):
		return self.LL1

	def printTable(self,Tabla):
	    for i in Tabla:
	        print(i)

	def TableFormat(self,Tabla):
		for i in range(len(Tabla)):
			for j in range(len(Tabla[i])):
				Tabla[i][j] = '{:^7}'.format(str(Tabla[i][j]))
		return Tabla

	def createNodes(self,Regla):
	    Tabla = []
	    for i in Regla:
	        aux = []
	        for j in i:

	            if j == "→" or j == ";":
	                pass
	            elif j == "|":
	                Tabla.append(aux)
	                aux = aux[:1]

	            elif j != " ":
	                if len(aux)==0:
	                    aux.append(j)
	                else:
	                    aux[len(aux)-1] = aux[len(aux)-1] + j

	            else:
	                aux.append(j)

	        Tabla.append(aux)
	    return Tabla

	def blank(self,Tabla):
	    for i in range(len(Tabla)):
	        for j in range(len(Tabla[i])):
	            Tabla[i][j] = Tabla[i][j].replace(" ","")

	def NoTerminales(self,Tabla):
	    NoTerminalesA = []
	    for i in range(len(Tabla)):
	        NoTerminalesA.append(Tabla[i][0])
	    return NoTerminalesA

	def Terminales(self,Tabla):
	    TerminalesA = []
	    for i in range(len(Tabla)):
	        for j in range(len(Tabla[i])):
	            if Tabla[i][j] not in self.NoTerminalesA and Tabla[i][j]!="ep":
	                TerminalesA.append(Tabla[i][j])
	    return TerminalesA

	#esta funcion recibe el simbolo, las reglas y los conjuntos de simbolos follow
	def First(self,NodeTable,NodeTables,Simbs):
		
	    if NodeTable[0][1] == "ep":
	        self.Follow(NodeTable[0][0],NodeTables,Simbs)
	    else:
	        for i in range(len(NodeTable)):
	            faux = NodeTable[i][1]
	            if faux not in(self.TerminalesA):
	                aux_nodes = []
	                for j in range(len(NodeTables)):
	                    if NodeTables[j][0] == faux:
	                        aux_nodes.append(NodeTables[j])
	                Simbs.append(self.First(aux_nodes,NodeTables,Simbs))
	            else:
	                Simbs.append(faux)

	def createAux(self,Simbolo,NodeTables):
	    aux = []
	    for i in range(len(NodeTables)):
	        if NodeTables[i][0] == Simbolo:
	            aux.append(NodeTables[i])
	    return aux

	#esta funcion recibe el simbolo, las reglas y los conjuntos de simbolos follow
	def Follow(self,NodeTable,NodeTables,Simbs):
	    aux = []
	    if NodeTable == NodeTables[0][0]:
	        if "$" not in Simbs:
	        	Simbs.append("$")
	    for i in range(len(NodeTables)):
	        for j in range(1,len(NodeTables[i])):
	            if NodeTables[i][j] == NodeTable:
	                if len(NodeTables[i]) == j+1:
	                    aux.append(NodeTables[i])
	                else:
	                    if NodeTables[i][j+1] not in self.TerminalesA:
	                        self.Follow(NodeTables[i][j+1],NodeTables,Simbs)
	                        x = self.createAux(NodeTables[i][j+1],NodeTables)
	                        for a in range(len(x)):
	                            self.First([x[a]],NodeTables,Simbs)
	                    else:
	                        Simbs.append(NodeTables[i][j+1])

	    q = copy.deepcopy(aux)
	    for i in range(len(aux)):
	        if q[i][0] == NodeTable:
	            q[i][0] = " "
	    self.blank(q)
	    for i in range(len(q)):
	        self.Follow(q[i][0],NodeTables,Simbs)


	def GenerateLL1(self,NodeTables,NoTerminalesA,TerminalesA):
	    re = []
	    LL1 = [["_"]]*(len(NoTerminalesA)+len(TerminalesA)+2)
	    for i in range(len(LL1)):
	        LL1[i] = ["_"]*(len(TerminalesA)+2)
	    for i in range(len(NoTerminalesA)):
	        LL1[i+1][0] = NoTerminalesA[i]
	    for i in range(len(TerminalesA)):
	        LL1[0][i+1] = TerminalesA[i]
	        LL1[i+1+len(NoTerminalesA)][0] = TerminalesA[i]
	    LL1[0][0] = "  "

	    for i in range(len(LL1)):
	        if LL1[i][0] in TerminalesA:
	            LL1[i][LL1[0].index(LL1[i][0])] = "pop"

	    LL1[0][len(LL1[0])-1] = "$"
	    LL1[len(LL1)-1][0] = "$"
	    LL1[len(LL1)-1][len(LL1[0])-1] = "ACEPTAR"
	    for i in range(len(LL1)):
	        re.append(LL1[i][0])
	    for i in range(len(NodeTables)):
	        Simbs = []
	        self.First([NodeTables[i]],NodeTables,Simbs)
	        Simbs = list(set(Simbs))
	        for j in range(len(Simbs)):
	            if Simbs[j] != None:
	                LL1[re.index(NodeTables[i][0])][LL1[0].index(Simbs[j])] =i+1

	    print("\n")
	    for i in range(len(LL1)):
	        for j in range(len(LL1[i])):
	            LL1[i][j] = '{:^7}'.format(str(LL1[i][j]))
	    return LL1


	def analizar(self,cadena,NoTerminalesA,TerminalesA):
	    aux = []
	    for i in cadena:
	        if i not in NoTerminalesA and i not in TerminalesA:
	            aux.append("num|sim")
	        else:
	            aux.append(i)
	    return aux

	def lookforindex(self,LL1Aux,sim1,sim2):
	    coord = []
	    for i in range(len(LL1Aux)):
	        if LL1Aux[i][0] == sim1:
	            coord.append(i)
	            break

	    for i in range(len(LL1Aux[0])):
	        if LL1Aux[0][i] == sim2:
	            coord.append(i)
	            break
	    return coord

	def addtoPila(self,pila,regla):
	    for i in regla:
	        pila.append(i)

	def validate(self,cadenaaux,NodeTables,LL1):
	    LL1Aux = copy.deepcopy(LL1)
	    self.blank(LL1Aux)
	    header = [["Pila","Cadena","Accion"]]
	    auxpila = ["$",NodeTables[0][0]]
	    i = 0
	    while True:
	        print(auxpila)
	        if auxpila[len(auxpila)-1] == "ep":
	            auxpila = auxpila[:-1]
	        else:
	            i+=1
	            coord = self.lookforindex(LL1Aux,auxpila[len(auxpila)-1],cadenaaux[0])
	            square = LL1Aux[coord[0]][coord[1]]
	            if square == "_":
	                break
	                return False
	            elif square == "pop":
	                auxpila = auxpila[:-1]
	                cadenaaux = cadenaaux[1:]
	            elif square == "ACEPTAR":
	                print("Ya estuvo")
	                return True
	            else:
	                regla = NodeTables[int(square)-1]
	                header.append([auxpila,cadenaaux,regla])
	                regla = list(reversed(regla[1:]))
	                auxpila = auxpila[:-1]
	                self.addtoPila(auxpila,regla)



		#self.printTable(header)

"""
Regla = sys.argv[1:]
print(str(type(Regla))+str(len(Regla)))
print(Regla)

obj = TablaPointersClass(Regla)
cadena = "( num + num ) * num - $"
cadena = cadena.split(" ")
obj.analizarCadena(cadena)"""