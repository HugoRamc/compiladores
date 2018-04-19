from automata import *
from convertirAFD import *

class tokensGramatica:

    def __init__(self):

        token = self.crear_tokens()
        self.PC = token[0]
        self.FLECHA = token[1]
        self.OR = token[2]
        self.SIMB = token[3]
        


    def crear_tokens(self):
        pila_tokens = []
        pila_automatas = []
        #0 ;
        automata = Automata([";"])
        automata2 = Automata([" "])
        automata2.cerradura_interrogacion()
        automata.concatenar(automata2)
        pila_tokens.append(automata.token*10)
        pila_automatas.append(automata)
        #1 ->
        automata = Automata(["-"])
        automata2 = Automata([">"])
        automata.concatenar(automata2)
        pila_tokens.append(automata.token*10)
        pila_automatas.append(automata)
        #2 OR
        automata = Automata(["|"])
        pila_tokens.append((automata.token*10))
        pila_automatas.append(automata)
        #3 SIMB
        #automata = Automata(["'"])
        #automata.cerradura_interrogacion()
        automata = Automata(["a","A","b","B","c","C","d","D","e","E","f","F","g","G","h","H","i","I","j","J","k","K","l","L","m","M","n","N","ñ","Ñ","o","O","p","P","q","Q","r","R","s","S","t","T","u","U","v","V","w","W","x","y","Y","z","Z"])
        automata.cerradura_positiva()
        #automata2.concatenar(automata)
        #automata.unir(automata2)
        pila_tokens.append(automata.token*10)
        pila_automatas.append(automata)


        pila_automatas[0].union_especial(pila_automatas[1:])
        AFD = convertirAFD(pila_automatas[0],pila_automatas)
        pila_automatas = []
        self.tablaAFD = AFD.getTabla()
        return pila_tokens

