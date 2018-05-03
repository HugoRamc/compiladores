from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from TablaPointersClass import *

class interfazLL1(object):
    """docstring for interfaz_expresiones"""
    def __init__(self):
        self.frame()
        self.reglas = ""
        self.cadena = ""
        #self.TTL1 = None


    def analize(self,reglas,cadena):
        self.reglas = reglas.split("\n")
        self.cadena = cadena.split(" ")
        self.reglas = self.reglas[:len(self.reglas)-1]
        print(str(type(self.reglas)) + str(len(self.reglas)))
        print(self.reglas)


        self.TLL1 = TablaPointersClass(self.reglas)
        mensaje = "Tabla LL1 creada exitosamente \n"
        
        if self.TLL1.analizarCadena(self.cadena):
            mensaje += "Cadena Aceptada"
        else:
            mensaje += "Cadena no aceptada"
        
        messagebox.showinfo("Éxito",mensaje)
        

    def analizaCadena(self,cadena):
        self.cadena = cadena.split(" ")
        
        mensaje = ""
        if self.TLL1.analizarCadena(self.cadena):
            mensaje += "Cadena Aceptada"
        else:
            mensaje += "Cadena no aceptada"
        
        messagebox.showinfo("Éxito",mensaje)


    def frame(self):
        f = Tk()
        f.geometry('500x600')
        f.configure(bg = 'LightBlue3')
        f.title('Tabla LL1')
        #
        label = Label( f, text="Introduce tus reglas de gramática", font = ("Helvetica", "18"),background='LightBlue3')
        label.place(x = 55,y = 13)
        field = Text(f, bd = 0,width=50,height = 10)
        field.place(x = 60,y = 50)

        label = Label( f, text="Escribe una cadena para ser analizada por la gramática", font = ("Helvetica", "12"),background='LightBlue3')
        label.place(x = 20,y = 200)
        field1 = Entry(f, bd = 0,width=43)
        field1.place(x = 60,y = 230)


        button = Button(f, text = "Crear Tabla LL1",command = lambda m = field: self.analize(field.get(1.0,END),field1.get()),highlightbackground='LightBlue3')
        button.place(x=80,y =270)

        button2 = Button(f, text = "Analizar Cadena",command = lambda m = field: self.analizaCadena(field1.get()),highlightbackground='LightBlue3')
        button2.place(x=230,y =270)



        f.mainloop()

obj = interfazLL1()