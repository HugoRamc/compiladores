from automata import *
from convertirAFD import *

class TokensAFN:

    def __init__(self):

        token = self.crear_tokens()
        self.OR =token[0]
        self.conc = token[1]
        self.cerrPos = token[2]
        self.cerrKleene = token[3]
        self.cerrOpc = token[4]
        self.parI = token[5]
        self.parD = token[6]
        self.mas = token[7]
        self.por = token[8]
        self.interrogacion = token[9]
        self.AND = token[10]
        self.barra = token[11]
        self.abecedario =  token[12]


    def crear_tokens(self):
        pila_tokens = []
        pila_automatas = []
        #0
        automata = Automata(["|"])
        pila_tokens.append(automata.token*10)
        pila_automatas.append(automata)
        #1
        automata = Automata(["&"])
        pila_tokens.append(automata.token*10)
        pila_automatas.append(automata)
        #2
        automata = Automata(["+"])
        pila_tokens.append(automata.token*10)
        pila_automatas.append(automata)
        #3
        automata = Automata(["*"])
        pila_tokens.append(automata.token*10)
        pila_automatas.append(automata)
        #4
        automata = Automata(["?"])
        pila_tokens.append(automata.token*10)
        pila_automatas.append(automata)
        #5
        automata = Automata(["("])
        pila_tokens.append(automata.token*10)
        pila_automatas.append(automata)
        #6
        automata = Automata([")"])
        pila_tokens.append(automata.token*10)
        pila_automatas.append(automata)
        #7
        automata = Automata(["+"])
        automata2 = Automata(["\\"])
        automata2.concatenar(automata)
        pila_tokens.append(automata2.token*10)
        pila_automatas.append(automata2)
        #8
        automata = Automata(["*"])
        automata2 = Automata(["\\"])
        automata2.concatenar(automata)
        pila_tokens.append(automata2.token*10)
        pila_automatas.append(automata2)
        #9
        automata = Automata(["?"])
        automata2 = Automata(["\\"])
        automata2.concatenar(automata)
        pila_tokens.append(automata2.token*10)
        pila_automatas.append(automata2)
        #10
        automata = Automata(["&"])
        automata2 = Automata(["\\"])
        automata2.concatenar(automata)
        pila_tokens.append(automata2.token*10)
        pila_automatas.append(automata2)
        #11
        automata = Automata(["|"])
        automata2 = Automata(["\\"])
        automata2.concatenar(automata)
        pila_tokens.append(automata2.token*10)
        pila_automatas.append(automata2)
        #12"2
        automata = Automata(["0","1","2","3","4","5","6","7","8","9","a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","ñ","Ñ","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","y","Y","z","Z"])
        automata.cerradura_positiva()
        pila_tokens.append(automata.token*10)
        pila_automatas.append(automata)

        pila_automatas[0].union_especial(pila_automatas[1:])
        AFD = convertirAFD(pila_automatas[0],pila_automatas)
        pila_automatas = []
        self.tablaAFD = AFD.getTabla()
        return pila_tokens

        

