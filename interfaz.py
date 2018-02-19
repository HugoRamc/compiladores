from tkinter import *
from tkinter import ttk
from automata import *

class Interfaz(object):
    """docstring for interfaz"""
    def __init__(self):
        self.automatas = []
        self.idAutomata = 0
        self.idEstadoAcum = 0
        self.frame()


    def frame(self):
        MsgButtons = ["Crear AFN Básico","Unir AFN","Concatenar AFN´s","Operación +","Operación *","Operación ?","Validar Cadena","Salir"]
        Buttons = []
        f = Tk()
        f.geometry('350x300')
        f.configure(bg = 'LightBlue3')
        f.title('Automatas')
        label = Label( f, text="Automatas", font = ("Helvetica", "18"),background='LightBlue3')
        label.place(x = 130,y = 13)
        for i in range(len(MsgButtons)):
            Buttons.append(Button(f, text = MsgButtons[i],command = lambda: interfaz(E.get(),f),highlightbackground='LightBlue3'))
            Buttons[i].place(x = 30, y = 39 + i*30)
        f.mainloop()

#Automata = automata(va el iterador de los estados,string de alfabeto) para crear nu automata se usa esta notaciòn,
#La clase automata ya cre automaticamente un automata base
obj = interfaz()
