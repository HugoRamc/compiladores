class transicion(object):
	
	def __init__(self,minsimbolo,maxSimbolo,idEstadoDestino):
		self.minSimbolo = minsimbolo
		self.maxSimbolo = maxSimbolo
		self.idEstadoDestino = idEstadoDestino

	def __init__(self,simbolo,idEstadoDestino):
		self.minSimbolo = simbolo
		self.maxSimbolo = simbolo
		self.idEstadoDestino = idEstadoDestino
		