from automata import *
from tokensGramatica import *

class convertidorGramaticasAFN:

	def __init__(self):
		self.crear_tokens()
		self.lex = None

	def crear_tokens(self):
		print("\nOperacion crear_tokens")
		self.clase_lexema = tokensGramatica()
		self.tablaAFD = self.clase_lexema.tablaAFD

	#Todos los primos regresan el token y regresan verdadero
	def analizar(self):
		print("\nOperacion analizar")
		valido = self.G()
		if valido:
			return True

	# G→ListaReglas
	def G(self):
		print("\nOperacion G")
		valido = self.listaReglas()
		if valido:
			return True
		return False;

	# ListReglas→Reglas ; ListaReglas′
	def listaReglas(self):
		print("\nOperacion listaReglas")
		valido = self.reglas()
		if valido:
			tok, lexema = self.lex.getToken()
			print("--Token recibido por LR: ") 
			print(tok)
			if tok == self.clase_lexema.PC:
				valido = self.listaReglasP()
				if valido:
					return True
				return False
			#self.lex.regresarToken(lexema)
			return False	
		return False


	# ListaReglas′→ Reglas ; ListaReglas′ | ϵ
	def listaReglasP(self):
		print("\nOperacion listaReglasP")
		self.lex.getEstado()
		valido = self.reglas()
		if valido:
			tok, lexema = self.lex.getToken()
			print("--Token recibido por LRP: ") 
			print(tok)
			if tok == self.clase_lexema.PC:
				valido = self.listaReglasP()
				if valido:
					return True
				return False	
			#self.lex.regresarToken(lexema)
			return False	
		self.lex.setEstado()
		return True	

	# Reglas→LadoIzquierdo  Flecha  ListaLadosDerechos
	def reglas(self):
		print("\nOperacion reglas")
		valido = self.ladoIzquierdo()
		if valido:
			tok, lexema = self.lex.getToken()
			print("--Token recibido por R: ") 
			print(tok)
			if tok == self.clase_lexema.FLECHA:
				valido = self.listaLadosDerechos()
				if valido:
					return True
				return False	
			#self.lex.regresarToken(lexema)
			return False	
		return False	

	# LadoIzquierdo→SIMBOLO
	def ladoIzquierdo(self):
		print("\nOperacion ladoIzquierdo")
		tok, lexema = self.lex.getToken()
		print("--Token recibido por LI: ") 
		print(tok)
		if tok == self.clase_lexema.SIMB:
			return True
		return False
		#self.lex.regresarToken(lexema)

	# ListaLadosDerechos→ LadoDerecho ListaLadosDerechos′
	def listaLadosDerechos(self):
		print("\nOperacion listaLadosDerechos")
		valido = self.ladoDerecho()
		if valido:
			valido = self.listaLadosDerechosP()
			if valido:
				return True
			return False	
		return False

	# ListaLadosDerechos′→OR  LadoDerecho ListaLadosDerechos′ | ϵ	
	def listaLadosDerechosP(self):
		print("\nOperacion listaLadosDerechosP")
		tok, lexema = self.lex.getToken()
		print("--Token recibido por LLDP: ") 
		print(tok)
		if tok == self.clase_lexema.OR:
			valido = self.ladoDerecho()
			if valido:
				valido = self.listaLadosDerechosP()
				if valido:
					return True
				return False	
			return False	
		self.lex.regresarToken(lexema)	
		return True

	# LadoDerecho→SIMBOLO LadoDerecho′
	def ladoDerecho(self):
		print("\nOperacion ladoDerecho")
		tok, lexema = self.lex.getToken()
		print("--Token recibido por LD: ") 
		print(tok)
		if tok == self.clase_lexema.SIMB:
			valido = self.ladoDerechoP()
			if valido:
				return True
			return False	
		#self.lex.regresarToken(lexema)
		return False

	# LadoDerecho′→SIMBOLO LadoDerecho′ | ϵ
	def ladoDerechoP(self):
		print("\nOperacion ladoDerechoP")
		tok, lexema = self.lex.getToken()
		print("--Token recibido por LDP: ") 
		print(tok)
		if tok == self.clase_lexema.SIMB:
			valido = self.ladoDerechoP()
			if valido:
				return True
			return False
		self.lex.regresarToken(lexema)
		return True





























