class Lexico(object):
	"""docstring for lexico"""
	def __init__(self,tablaAFD,cadena):
		self.cadena = cadena
		self.tablaAFD = tablaAFD


	def getToken(self):

		if len(self.cadena) == 0:
			return "0",self.cadena


		edo,pos = self.validaCadena(self.cadena)

		if edo == -1 or edo == "-1":
			pos+=1


		lexema = self.cadena[:pos]
		self.cadena = self.cadena[pos:]

		return edo,lexema

	def regresarToken(self,lex):
		self.cadena = lex+self.cadena

	def validaCadena(self,cadena):
	    #print("Hola cadena "+cadena+"\n")
	    caracteres = self.tablaAFD[0]
	    edoActual = 0
	    i=0
	    token = 0
	    for c in cadena:

	        if c not in caracteres:
	            return -1,i
	        else:
	            #print(edoActual)
	            y = caracteres.index(c)
	            x = self.tablaAFD[int(edoActual)+1]
	            edoActual = int(x[y])
	            token = x[len(x)-1]

	            if edoActual == -1:
	                if token != "-1" or token != -1:
	                	return token,i
	                else:
	                	return -1,i

	        i+=1

	   # print(edoActual)
	    x = self.tablaAFD[edoActual+1]
	    if x[len(x)-1] == -1:
	        return -1,i
	    else:
	        return x[len(x)-1],i
