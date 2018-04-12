from automata import *
from tokensAFN import *

class convertidorExpresionesAFN:

	def __init__(self):
		self.crear_tokens()
		self.lex = None

	def crear_tokens(self):
		self.clase_lexema = TokensAFN()
		self.tablaAFD = self.clase_lexema.tablaAFD

	#Todos los primos regresan el token y regresan verdadero
	def analizar(self):
		automata = Automata(["Ǝ"])

		valido,automata = self.E(automata)
		if valido:
			return True,automata
		else:
			return False,automata
		




	#
	def E(self,AFN):
		print("E")
		valido,f = self.T(AFN)
		if valido:
			valido,f = self.Ep(f)
			if valido:
				return True,f
		return False,f

	def Ep(self,f):
		print("Ep")
		f1 = Automata(["Ǝ"])
		tok,lexema = self.lex.getToken()
		if tok == self.clase_lexema.OR:
			valido,f1 = self.T(f1)
			if valido:
				f.unir(f1)
				valido,f = self.Ep(f)
				if valido:
					return True,f
			return False,f

		##regrsar el token
		self.lex.regresarToken(lexema)
		return True,f

	def T(self,f):
		print("T")
		valido,f = self.C(f)
		if valido:
			valido,f = self.Tp(f)
			if valido:
				return True,f
		return False,f

	def Tp(self,f):
		print("Tp")
		token,lexema = self.lex.getToken()
		f1 = Automata(["Ǝ"])
		if token == self.clase_lexema.conc:
			valido,f1 = self.C(f1)
			if valido:
				f.concatenar(f1)
				valido,f = self.Tp(f)

				if valido:
					return True,f
			return False,f
		self.lex.regresarToken(lexema)
		return True,f


	def C(self,f):
		print("C")
		valido,f = self.F(f)
		if valido:
			
			valido2,f = self.Cp(f)
			if valido2:
				return True,f
		return False,f


		
	def Cp(self,f):
		print("Cp")

		token,lexema = self.lex.getToken()
		print(str(token))
		if token == self.clase_lexema.cerrPos or token== self.clase_lexema.cerrKleene or token == self.clase_lexema.cerrOpc:

			if token == self.clase_lexema.cerrPos:
				f.cerradura_positiva()
			elif token == self.clase_lexema.cerrKleene:
				f.cerradura_kleene()
			elif token == self.clase_lexema.cerrOpc:
				f.cerradura_interrogacion()

			val,f = self.Cp(f)
			if val:
				return True,f
			else:
				return False,f


		else:
			self.lex.regresarToken(lexema)
			return True,f
			

	def F(self,AFN):
		print("F")
		token,lexema = self.lex.getToken()
		print("Token: "+str(token)+"  "+str(lexema))
		print(str(self.clase_lexema.abecedario))

		if token == self.clase_lexema.abecedario or token== self.clase_lexema.barra or token== self.clase_lexema.AND or token== self.clase_lexema.interrogacion or token== self.clase_lexema.por or token== self.clase_lexema.mas:
			print("creacion automata basico")
			lexema = lexema.replace("\\","")

			AFN = Automata(str(lexema))
			return True,AFN

		elif token == self.clase_lexema.parI:
			print("expresion parentesis")
			valido2,AFN = self.E(AFN)

			if valido2:
				token2,lexema2 = self.lex.getToken()
				if token2 == self.clase_lexema.parD:
					return True,AFN
			else:
				return False,AFN
		
		return False,AFN

