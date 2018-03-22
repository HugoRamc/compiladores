from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import StringVar
from tkinter import *
from calculadora import *
from lexico import *

calculadora = Calculadora()

def clean_string(cadena):
    c = cadena.get()
    aux = ""
    i = 0
    ii = len(c)
    while i < ii:
        if c[i] == "s" or c[i] == "c" or c[i] == "t":
            aux = aux + c[i]
            i = i + 3
            pass
        elif c[i] == "l":
            if c[i + 1] == "n":
                aux = aux + "n"
                i = i + 2
            if c[i + 1] == "o":
                aux = aux + "l"
                i = i + 3
            pass
        elif c[i] == "√":
            aux = aux + "r"
            i+=1
        elif c[i] == "x":
            aux = aux + "*"
            i+=1
        elif c[i] == "÷":
            aux = aux + "/"
            i+=1
        elif c[i] == "π":
            aux = aux + "p"
            i+=1
        else:
            aux = aux + c[i]
            i+=1

    cadena.set(aux)
def popmessage(m,L,frame,Buttons):
    cadena = StringVar()
    if m == "MODE":
        act_int(frame,Buttons)
    elif m == "DEL":
        L.configure(text = "")
    elif m == "←":
        L.configure(text = L.cget("text")[:-1])
    elif m == "=":
        # C es la cadena final ya con todos los simbolos TE AMO :3
        cadena.set(L.cget("text"))
        clean_string(cadena)
        c = cadena.get()
        lex = Lexico(calculadora.tablaAFD,c)
        calculadora.lex = lex
        valido, v = calculadora.analizar()
        if valido:
            #aquí puedes muestrar lo que te regrese v broo en la barrita de la calculadora? :3
            pass
        else:
            #Aquí pon el famoso sintax error o una mamada así amigo jaja
            pass
        #Te amito <3

    else:
        s = m;
        if m == "sen" or m == "cos"or m == "tan"or m == "ln"or m == "log"or m == "^"or m == "√":
            m = m + "("
        L.configure(text = L.cget("text")+ m)



def frame():
    Numeros = ["sen","cos","tan","ln","log","^","√","","π","e","7","8","9","DEL","←","4","5","6","x","÷","1","2","3","+","-","0",".","(",")","="]
    Buttons = []
    f = Tk()
    f.geometry('500x500')
    f.configure(bg = 'LightBlue3')
    f.title('Calculadora')
    x = 0;
    y = 100;
    L = Label(f, bd = 0,width=38)
    L.place(x=72, y = y)
    L.configure(anchor="se")
    for i in range(len(Numeros)):
        if i%5 == 0:
            y = y + 30
            x = 0
        x = x + 70
        Buttons.append(Button(f, text = Numeros[i], width = 5,command = lambda m = Numeros[i]: popmessage(m,L,f,Buttons),highlightbackground='LightBlue3'))
        Buttons[i].place(x = x, y = y)

    f.mainloop()
frame()
