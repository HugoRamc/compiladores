class lexico(object):
	"""docstring for lexico"""
	def __init__(self):
		pass

	def validaCadena(self,cadena,tablaAFD):
	    caracteres = tablaAFD[0]
	    edoActual = 0
	    i=0
	    for c in cadena:
	        if c not in caracteres:
	            return -1,i
	        else:
	            print(edoActual)
	            y = caracteres.index(c)
	            x = tablaAFD[int(edoActual)+1]
	            edoActual = int(x[y])
	            if edoActual == -1:
	                return -1,i
	        i+=1
	    print(edoActual)
	    x = tablaAFD[edoActual+1]
	    if x[len(x)-1] == -1:
	        return -1,i
	    else:
	        return x[len(x)-1],i
		