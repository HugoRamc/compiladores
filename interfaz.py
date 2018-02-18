from tkinter import *
from tkinter import ttk
from automata import *

class interfaz(object):
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

    def automataBasico(self,simbolo):
        nautomata = automata(simbolo,self.idEstadoAcum)
        self.automatas.append(nautomata)

    def unir(self):
        pass

    def concatenar(self):
        pass

    def cerradura_kleene(self):
        pass

    def cerradura_positiva(self):
        pass

    def ir_a(self):
        pass

    def mover_C(self):
        pass

    def mover(self):
        pass

    def cerradura_epsilon_C(self):
        pass

    def cerradura_epsilon(self,estado):
        conjEstados = []
        pilaEstados = []
    
        pilaEstados.append(estado)

        while len(pilaEstados)==0:
            pass


obj = interfaz()
