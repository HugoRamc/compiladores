from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from LR1 import *
from LR0 import *
import copy

class interfazLL1(object):
    """docstring for interfaz_expresiones"""
    def __init__(self):
        self.frame()
        self.reglas = ""
        self.cadena = ""
        #self.TTL1 = None


    def analize(self,reglas,cadena):
        self.reglas = reglas.split("\n")
        self.reglas = self.reglas[:len(self.reglas)-1]
        print(str(type(self.reglas)) + str(len(self.reglas)))
        print(self.reglas)


        
        self.LR01 = LR0(self.reglas)

        self.Tabla = self.LR01.obj.createNodes(self.reglas) #esta tabla contiene todas las reglas pero sin punto
        self.LR01.obj.blank(self.Tabla)
        self.Tabla = self.LR01.gramaticaExtendida(self.Tabla)
        #To this point we have the extended grammar we update all the simbols
        self.LR01.obj.resetsimbolos(self.Tabla)
        NoTerminalesA = self.LR01.obj.NoTerminalesA
        TerminalesA = self.LR01.obj.TerminalesA
        TerminalesA.append("$")
        self.LR01.setValores(self.Tabla,TerminalesA,NoTerminalesA)
        #with the simbols1 now updated, now we proceed to create all the items
        items = self.LR01.createItems(self.Tabla)
        #now having the items we proceed to create the LR1 tables
        self.LR1 = LR1(self.LR01,self.Tabla,items)
        self.TablaLR1 = self.LR1.createLR1()
        copia = copy.deepcopy(self.TablaLR1)
        self.LR1.LR0.imprimirTablaf(copia)
        
        if cadena != "":
            self.analizaCadena(cadena)
        

    def analizaCadena(self,cadena):
        #self.cadena = cadena.split(" ")
        print(cadena)
        cadena = cadena.split(" ")
        mensaje = ""
        if self.LR1.analizarCadena(cadena,self.TablaLR1):
            mensaje += "Cadena Aceptada"
        else:
            mensaje += "Cadena no aceptada"
        
        #self.LR01.imprimirTablaf(self.LR01.tablaImprime)
        messagebox.showinfo("Éxito",mensaje)




    def frame(self):
        f = Tk()
        f.geometry('500x600')
        f.configure(bg = 'LightBlue3')
        f.title('Tabla LR1')
        #
        label = Label( f, text="Introduce tus reglas de gramática", font = ("Helvetica", "18"),background='LightBlue3')
        label.place(x = 55,y = 13)
        field = Text(f, bd = 0,width=50,height = 10)
        field.place(x = 60,y = 50)

        label = Label( f, text="Escribe una cadena para ser analizada por la gramática", font = ("Helvetica", "12"),background='LightBlue3')
        label.place(x = 20,y = 200)
        field1 = Entry(f, bd = 0,width=43)
        field1.place(x = 60,y = 230)


        button = Button(f, text = "Crear Tabla LR1",command = lambda m = field: self.analize(field.get(1.0,END),field1.get()),highlightbackground='LightBlue3')
        button.place(x=80,y =270)

        button2 = Button(f, text = "Analizar Cadena",command = lambda m = field: self.analizaCadena(field1.get()),highlightbackground='LightBlue3')
        button2.place(x=230,y =270)



        f.mainloop()

obj = interfazLL1()