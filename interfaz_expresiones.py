from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from convertidorExpresionesAFN import *
from lexico import * 

analizadorExpresiones = convertidorExpresionesAFN()


def analize(expresion,cadena):
    #messagebox.showinfo("Exito", str(cadena))

    lex = Lexico(analizadorExpresiones.tablaAFD,expresion)
    analizadorExpresiones.lex = lex

    valido, AFN = analizadorExpresiones.analizar()



    if valido:
        print("Tu expresion pertenece a la gramática")
        if AFN.analizaCadena(cadena):
            print("Tu cadena pertenece a la expresion Regular")
        else:
            print("Tu candea no pertenece a la expresion regular")


    else:
        print("Tu expresion no pertenece a la gramática")






def frame():
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


    button = Button(f, text = "Analizar",command = lambda m = field: analize(field.get(),field1.get()),highlightbackground='LightBlue3')
    button.place(x=120,y =130)
    f.mainloop()
frame()
