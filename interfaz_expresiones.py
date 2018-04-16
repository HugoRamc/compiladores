from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from convertidorExpresionesAFN import *
from lexico import * 

class interfaz_expresiones(object):
    """docstring for interfaz_expresiones"""
    def __init__(self,m,f,laut):
        self.pilaAutomatas = []
        self.analizadorExpresiones = convertidorExpresionesAFN()
        self.frame(m,f,laut)
        


    def getPilaAutomatas(self):
        return self.pilaAutomatas


    def analize(self,expresion,cadena):
    #messagebox.showinfo("Exito", str(cadena))
        if cadena =="":
            cadena = "Ǝ"

        lex = Lexico(self.analizadorExpresiones.tablaAFD,expresion)
        self.analizadorExpresiones.lex = lex

        valido, AFN = self.analizadorExpresiones.analizar()
        if AFN not in self.pilaAutomatas:
            self.pilaAutomatas.append(AFN)


        mensaje = ""
        if valido:
            mensaje = "Tu expresion pertenece a la gramática"
            if AFN.analizaCadena(cadena):
                mensaje += ("\nTu cadena pertenece a la expresion Regular")
            else:
                mensaje+= ("\nTu cadena no pertenece a la expresion regular")
        else:
            mensaje = ("Tu expresion no pertenece a la gramática + \nCadena no analizada")

        messagebox.showinfo("Éxito",mensaje)


    def analizarCadena(self,cadena):
        mensaje = ""
        if self.pilaAutomatas[len(self.pilaAutomatas)-1].analizaCadena(cadena):
            mensaje = "cadena aceptada"
        else:
            mensaje =  "cadena no aceptada"

        messagebox.showinfo("Éxito",mensaje)
        



    def frame(self,f,m,laut):
        f = Tk()
        f.geometry('500x320')
        f.configure(bg = 'LightBlue3')
        f.title('Expresiones Regulares')
        #
        label = Label( f, text="Expresiones Regulares", font = ("Helvetica", "18"),background='LightBlue3')
        label.place(x = 55,y = 13)
        field = Entry(f, bd = 0,width=20)
        field.place(x = 60,y = 50)

        label = Label( f, text="Escribe una cadena para ser analizada por la expresion regular", font = ("Helvetica", "12"),background='LightBlue3')
        label.place(x = 20,y = 80)
        field1 = Entry(f, bd = 0,width=20)
        field1.place(x = 60,y = 100)


        button = Button(f, text = "Crear Expresion",command = lambda m = field: self.analize(field.get(),field1.get()),highlightbackground='LightBlue3')
        button.place(x=80,y =130)

        button = Button(f, text = "Analizar Cadena",command = lambda m = field: self.analizarCadena(field1.get()),highlightbackground='LightBlue3')
        button.place(x=230,y =130)



        f.mainloop()

