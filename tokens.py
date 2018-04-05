from automata import *
from convertirAFD import *

class Tokens:

    def __init__(self):
        token = self.crear_tokens()
        self.num = token[0]
        self.especial = token[1]
        self.suma = token[2]
        self.res = token[3]
        self.mul = token[4]
        self.div = token[5]
        self.parI = token[6]
        self.parD = token[7]
        self.exp = token[8]
        self.raiz = token[9]
        self.cos = token[10]
        self.sin = token[11]
        self.tan = token[12]
        self.log = token[13]
        self.ln = token[14]

    def crear_tokens(self):
        pila_tokens = []
        pila_automatas = []
        automata = Automata(["0","1","2","3","4","5","6","7","8","9"])
        automata_aux = automata #copia de automata de numeros
        automata.cerradura_positiva()# primer automata con numeros que se repiten
        automata_aux.cerradura_positiva()# segundo automata con numeros que se repiten
        automata_punto = Automata(["."])
        automata_punto.concatenar(automata_aux)
        automata_punto.cerradura_interrogacion()
        automata.concatenar(automata_punto)
        pila_tokens.append(automata.token*10)
        pila_automatas.append(automata)
        automata = Automata(["e","π"])
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
        automata = Automata(["√"]) #token para exponencial
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
        pila_automatas = []
        self.tablaAFD = AFD.getTabla()
        return pila_tokens
