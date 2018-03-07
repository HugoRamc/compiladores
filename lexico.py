class lexico(object):
	"""docstring for lexico"""
	def __init__(self,tablaAFD):
		self.tablaAFD = tablaAFD

	def lexico(self,cadena):
		cadenatokens = ""
		while len(cadena) > 0:
			

			val,pos = self.validaCadena(cadena)

			if val == -1 or val == "-1":
				cadenatokens +="-1,"
				pos+=1
			else:
				cadenatokens+=str(val)+","
			cadena = cadena[pos:]
			
		cadenatokens = cadenatokens[0:len(cadenatokens)-1]
		return cadenatokens

	def validaCadena(self,cadena):
	    print("Hola cadena "+cadena)
	    caracteres = self.tablaAFD[0]
	    edoActual = 0
	    i=0
	    token = 0
	    for c in cadena:

	        if c not in caracteres:
	            return -1,i
	        else:
	            print(edoActual)
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

	    print(edoActual)
	    x = self.tablaAFD[edoActual+1]
	    if x[len(x)-1] == -1:
	        return -1,i
	    else:
	        return x[len(x)-1],i
		