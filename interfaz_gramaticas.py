from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from convertidorGramaticasAFN import *
from lexico import * 

analizadorGramaticas = convertidorGramaticasAFN()


def analize(expresion):

    # Lexico(tabla, cadena)
    lex = Lexico(analizadorGramaticas.tablaAFD,expresion)
    analizadorGramaticas.lex = lex

    valido = analizadorGramaticas.analizar()

    if valido:
        print("Tu expresion pertenece a la gramática")
        messagebox.showinfo("Exito", "Tu cadena pertenece a la gramatica")
    else:
        print("Tu expresion no pertenece a la gramática")
        messagebox.showinfo("Error", "Tu cadena no pertenece a la gramatica")


def frame():
    f = Tk()
    f.geometry('500x320')
    f.configure(bg = 'LightBlue3')
    f.title('Gramáticas')
    #
    label = Label(f, text="Gramática con reglas separadas por ;", font=("Helvetica", "18"), background='LightBlue3')
    label.place(x=40, y=13)
    field = Entry(f, bd=0, width=46)
    field.place(x=40, y=50)

    button = Button(f, text = "Analizar",command = lambda m = field: analize(field.get()),highlightbackground='LightBlue3')
    button.place(x=195, y=130)
    f.mainloop()
frame()
