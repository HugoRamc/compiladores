from tokens import *
import math
#from precedencia import Precedencia

class Calculadora:

	def __init__(self):
		self.crear_tokens()
		self.lex = None

	def crear_tokens(self):
		self.clase_lexema = Tokens()
		self.tablaAFD = self.clase_lexema.tablaAFD

	#Todos los primos regresan el token y regresan verdadero
	def analizar(self):
		v = 0.0
		self.postfija = ""
		self.prefija = ""
		valido,v = self.E(v)
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
					self.postfija += "+"
					self.prefija = "+" + self.prefija
					v = v + v1
				else:
					self.postfija += "-"
					self.prefija = "-" + self.prefija
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
		v1 = 0.0
		if tok == self.clase_lexema.mul or tok == self.clase_lexema.div:
			valido,v1 = self.F(v1)
			if valido:
				if tok == self.clase_lexema.mul:
					self.postfija += "*"
					self.prefija = "*" + self.prefija
					v = v * v1
				else:
					self.postfija += "/"
					self.prefija = "/" + self.prefija
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
				self.postfija += "^"
				self.prefija = "^" + self.prefija
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

		if tok == self.clase_lexema.num:
			v = float(lexema)
			self.postfija += lexema
			self.prefija = lexema + self.prefija
			return True,v

		elif tok == self.clase_lexema.especial:
			if lexema == "e":
				v = math.e
			else:
				v = math.pi
			self.prefija = lexema + self.prefija
			self.postfija += lexema
			return True,v

		elif tok == self.clase_lexema.parI:
			valido,v = self.E(v)
			if valido:
				tok,_ = self.lex.getToken()
				if tok == self.clase_lexema.parD:
					return True,v
			return False,v

		elif tok == self.clase_lexema.cos:
			self.postfija += "cos"
			self.prefija = "cos" + self.prefija
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
			self.postfija += "sin"
			self.prefija = "sin" + self.prefija
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
			self.postfija += "tan"
			self.prefija = "tan" + self.prefija
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
			self.postfija += "log"
			self.prefija = "log" + self.prefija
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
			self.postfija += "ln"
			self.prefija = "ln" + self.prefija
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
			self.postfija += "√"
			self.prefija = "√" + self.prefija
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
