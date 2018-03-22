from automata import *
from tokens import *
from convertirAFD import *
#from lexico import *
import math

class Calculadora:

	def __init__(self):
		self.crear_tokens()
		self.lex = None

	def crear_tokens(self):
		pila_tokens = []
		pila_automatas = []
		automata = Automata(["0","1","2","3","4","5","6","7","8","9","e","p"])
		automata_aux = automata #copia de automata de numeros
		automata.cerradura_positiva()# primer automata con numeros que se repiten
		automata_aux.cerradura_positiva()# segundo automata con numeros que se repiten
		automata_punto = Automata(["."])
		automata_punto.concatenar(automata_aux)
		automata_punto.cerradura_interrogacion()
		automata.concatenar(automata_punto)
		pila_tokens.append(automata.token*10)
		pila_automatas.append(automata)
		automata = Automata(["+"])
		pila_tokens.append(automata.token*10)
		pila_automatas.append(automata)
		automata = Automata(["-"])
		pila_tokens.append(automata.token*10)
		pila_automatas.append(automata)
		automata = Automata(["*"])
		pila_tokens.append(automata.token*10)
		pila_automatas.append(automata)
		automata = Automata(["/"])
		pila_tokens.append(automata.token*10)
		pila_automatas.append(automata)
		automata = Automata(["("])
		pila_tokens.append(automata.token*10)
		pila_automatas.append(automata)
		automata = Automata([")"])
		pila_tokens.append(automata.token*10)
		pila_automatas.append(automata)
		automata = Automata(["^"]) #token para exponencial
		pila_tokens.append(automata.token*10)
		pila_automatas.append(automata)
		automata = Automata(["r"]) #token para exponencial
		pila_tokens.append(automata.token*10)
		pila_automatas.append(automata)
		automata = Automata(["c"]) #Token para el coseno
		pila_tokens.append(automata.token*10)
		pila_automatas.append(automata)
		automata = Automata(["s"]) #Token para el seno
		pila_tokens.append(automata.token*10)
		pila_automatas.append(automata)
		automata = Automata(["t"]) #Token para la tangente
		pila_tokens.append(automata.token*10)
		pila_automatas.append(automata)
		automata = Automata(["l"]) #Token para log
		pila_tokens.append(automata.token*10)
		pila_automatas.append(automata)
		automata = Automata(["n"]) #Token para ln
		pila_tokens.append(automata.token*10)
		pila_automatas.append(automata)
		pila_automatas[0].union_especial(pila_automatas[1:])
		AFD = convertirAFD(pila_automatas[0],pila_automatas)
		self.tablaAFD = AFD.getTabla()
		self.clase_lexema = Tokens(pila_tokens)

	#Todos los primos regresan el token y regresan verdadero
	def analizar(self):
		v = 0.0
		valido,v = self.E(v)
		print(valido)
		if valido:
			tok,lexema = self.lex.getToken()
			if tok == "0":
				return True,v
			else:
				return False,v
		else:
			return False,v

	def E(self,v):
		valido,v = self.T(v)
		if valido:
			valido,v = self.Ep(v)
			if valido:
				return True,v
		return False,v

	def T(self,v):
		valido,v = self.P(v)
		if valido:
			valido,v = self.Tp(v)
			if valido:
				return True,v
		return False,v

	def P(self,v):
		valido,v = self.F(v)
		if valido:
			valido,v = self.Pp(v)
			if valido:
				return True,v
		return False,v

	def Ep(self,v):
		tok,lexema = self.lex.getToken()
		v1 = 0.0
		if tok == self.clase_lexema.suma or tok == self.clase_lexema.res:
			valido,v1 = self.T(v1)
			if valido:
				if tok == self.clase_lexema.suma:
					v = v + v1
				else:
					v = v - v1
				valido,v = self.Ep(v)
				if valido:
					return True,v
			return False,v
		else:
			self.lex.regresarToken(lexema)
			return True,v

	def Tp(self,v):
		tok,lexema = self.lex.getToken()
		print(tok)
		v1 = 0.0
		if tok == self.clase_lexema.mul or tok == self.clase_lexema.div:
			valido,v1 = self.F(v1)
			if valido:
				if tok == self.clase_lexema.mul:
					v = v * v1
				else:
					v = v / v1
				valido,v = self.Tp(v)
				if valido:
					return True,v
			return False,v
		else:
			self.lex.regresarToken(lexema)
			return True,v

	def Pp(self,v):
		tok,lexema = self.lex.getToken()
		v1 = 0.0
		if tok == self.clase_lexema.exp:
			valido,v1 = self.F(v1)
			if valido:
				v = math.pow(v,v1)
				valido,v = self.Pp(v)
				if valido:
					return True,v
			return False,v
		else:
			self.lex.regresarToken(lexema)
			return True,v

	def F(self,v):
		tok,lexema = self.lex.getToken()
		print(tok)
		if tok == self.clase_lexema.num:
			if lexema == "e":
				v = math.e
			elif lexema == "p":
				v = math.pi
			else:
				v = float(lexema)
			return True,v

		elif tok == self.clase_lexema.parI:
			valido,v = self.E(v)
			if valido:
				tok,_ = self.lex.getToken()
				if tok == self.clase_lexema.parD:
					return True,v
			return False,v

		elif tok == self.clase_lexema.cos:
			tok,_ = self.lex.getToken()
			if tok == self.clase_lexema.parI:
				valido,v = self.E(v)
				if valido:
					tok,_ = self.lex.getToken()
					if tok == self.clase_lexema.parD:
						v = math.cos(v)
						return True,v
			return False,v

		elif tok == self.clase_lexema.sin:
			tok,_ = self.lex.getToken()
			if tok == self.clase_lexema.parI:
				valido,v = self.E(v)
				if valido:
					tok,_ = self.lex.getToken()
					if tok == self.clase_lexema.parD:
						v = math.sin(v)
						return True,v
			return False,v

		elif tok == self.clase_lexema.tan:
			tok,_ = self.lex.getToken()
			if tok == self.clase_lexema.parI:
				valido,v = self.E(v)
				if valido:
					tok,_ = self.lex.getToken()
					if tok == self.clase_lexema.parD:
						v = math.tan(v)
						return True,v
			return False,v

		elif tok == self.clase_lexema.log:
			tok,_ = self.lex.getToken()
			if tok == self.clase_lexema.parI:
				valido,v = self.E(v)
				if valido:
					tok,_ = self.lex.getToken()
					if tok == self.clase_lexema.parD:
						v = math.log(v,10)
						return True,v
			return False,v

		elif tok == self.clase_lexema.ln:
			tok,_ = self.lex.getToken()
			if tok == self.clase_lexema.parI:
				valido,v = self.E(v)
				if valido:
					tok,_ = self.lex.getToken()
					if tok == self.clase_lexema.parD:
						v = math.log(v)
						return True,v
			return False,v

		elif tok == self.clase_lexema.raiz:
			tok,_ = self.lex.getToken()
			if tok == self.clase_lexema.parI:
				valido,v = self.E(v)
				if valido:
					tok,_ = self.lex.getToken()
					if tok == self.clase_lexema.parD:
						v = math.sqrt(v)
						return True,v
			return False,v

		else:
			return False,v
