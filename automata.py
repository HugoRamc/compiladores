from estado import estado
from transicion import transicion

class Automata(object):

    def __init__(self,alphabeto):
		self.estadosDeAceptacion = {}
		self.estados = {}
        self.estadoInicial = estado
        self.alphabeto = alfabeto
        automataBasico(self)
        
    def automataBasico(self,s,s1):

        pass

    def unir(self):
        pass

    def concatenar(self):
        pass

    def cerraduraKleene(self):

        pass

    def cerraduraPositiva(self):
        pass

    def irA(self):
        pass

    def moverC(self):
        pass

    def mover(self):
        pass

    def cerraduraEpsilonC(self):
        pass

    def cerraduraEpsilon(self):
        pass
