from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from automata import *

pila_automatas = []

def update_AFN(f,laut,m,accion,cadena):
    if m == "Crear AFN Básico":
        aux = []
        if accion.find(",") != -1:
            aux = accion.split(",")
        elif ord(accion[0])>64:
            if len(accion) == 1:
                aux.append(accion[0])
            elif len(accion) == 0:
                aux.append("Ǝ")
            else:
                for i in range(ord(accion[0]),ord(accion[2])+1):
                    aux.append(chr(i))
        elif accion.find("-") != -1:
            separador = accion.index("-")
            for i in range (int(accion[:separador]),int(accion[separador-len(accion)+1:])+1):
                aux.append(str(i))

        else:
            aux.append(accion)
        pila_automatas.append(Automata(aux))


    if m == "Unir AFN's":
        automata1 = accion[0].get()
        automata2 = accion[1].get()
        pila_automatas[int(automata1)-1].unir(pila_automatas[int(automata2)-1])
        ##implementacion
    if m == "Concatenar AFN´s":
        automata1 = accion[0].get()
        automata2 = accion[1].get()
        pila_automatas[int(automata1)-1].concatenar(pila_automatas[int(automata2)-1])
        ##implementacion

    if m == "Operación +":
        automata = accion.get()
        pila_automatas[int(automata)-1].cerradura_positiva()
        ##implementacion
    if m == "Operación *":
        automata = accion.get()
        pila_automatas[int(automata)-1].cerradura_kleene()
        ##implementacion
    if m == "Operación ?":
        automata = accion.get()
        pila_automatas[int(automata)-1].cerradura_interrogacion()
        ##implementacion

    if m == "Validar Cadena":
        automata = accion[0].get()
        if cadena == "":
            cadena = "Ǝ"
        print(cadena)
        pertenece = pila_automatas[int(automata)-1].analizaCadena(cadena)
        if pertenece is True:
            messagebox.showinfo("Exito", "Tu cadena pertenece al automata")
        else:
            messagebox.showinfo("Error", "Tu cadena no pertenece al automata")
        ##implementacion

    laut.configure(text=str(len(pila_automatas)))
    f.update()

def create_AFN(m,main,laut):
        f = Tk()
        f.geometry('390x250')
        f.configure(bg = 'LightBlue3')
        f.title(m)
        label = Label(f, text=m, font = ("Helvetica", "18"),background='LightBlue3')
        label.place(x = 40,y = 13)
        label = Label(f, text="Para ingresar un rango usa el separador guión. En caso",background='LightBlue3')
        label.place(x = 20,y = 40)
        label = Label(f, text="de querer ingresar varios simbolos, usa el separador coma.",background='LightBlue3')
        label.place(x = 20,y = 60)
        label = Label(f, text="Entrada:",background='LightBlue3')
        label.place(x = 20,y = 90)
        E = Entry(f, bd = 0,width=6)
        E.place(x = 90,y = 90)
        B = Button(f, text = "Finalizar",command = lambda: update_AFN(main,laut,m,E.get(),None),highlightbackground='LightBlue3')
        B.place(x = 20, y =160)
        f.mainloop()


def unir_conca_AFN(m,main,laut):
        f = Tk()
        f.geometry('270x150')
        f.configure(bg = 'LightBlue3')
        f.title(m)
        label = Label(f, text=m, font = ("Helvetica", "18"),background='LightBlue3')
        label.place(x = 60,y = 13)
        aux = []
        for i in range(int(laut.cget("text"))):
            aux.append(str(i+1))
        Combo = []
        Combo.append(ttk.Combobox(f, state="readonly",width=4))
        Combo[0]["values"] = aux
        Combo[0].current(0)
        Combo[0].place(x=10,y=50)
        Combo.append(ttk.Combobox(f, state="readonly",width=4))
        Combo[1]["values"] = aux
        Combo[1].current(0)
        Combo[1].place(x=130,y=50)
        B = Button(f, text = m,command = lambda: update_AFN(main,laut,m,Combo,None),highlightbackground='LightBlue3')
        B.place(x = 60, y =90)
        f.mainloop()

def operation_aso(m,main,laut):
    f = Tk()
    f.geometry('250x150')
    f.configure(bg = 'LightBlue3')
    f.title(m)
    label = Label(f, text=m, font = ("Helvetica", "18"),background='LightBlue3')
    label.place(x = 60,y = 13)
    aux = []
    for i in range(len(pila_automatas)):
        aux.append(str(i+1))
    Combo1 = ttk.Combobox(f, state="readonly",width=4)
    Combo1["values"] = aux
    Combo1.current(0)
    Combo1.place(x=70,y=50)
    B = Button(f, text = "Finalizar",command = lambda: update_AFN(main,laut,m,Combo1,None),highlightbackground='LightBlue3')
    B.place(x = 60, y =90)

    ##if m == "Operación +":
    ##if m == "Operación *":
    ##if m == "Operación ?":
    f.mainloop()

def validar(m,main,laut):
        f = Tk()
        f.geometry('390x250')
        f.configure(bg = 'LightBlue3')
        f.title(m)
        label = Label(f, text=m, font = ("Helvetica", "18"),background='LightBlue3')
        label.place(x = 60,y = 13)
        aux = []
        for i in range(int(laut.cget("text"))):
            aux.append(str(i+1))
        Combo = []
        Combo.append(ttk.Combobox(f, state="readonly",width=4))
        Combo[0]["values"] = aux
        Combo[0].current(0)
        Combo[0].place(x=10,y=50)
        Combo.append(ttk.Combobox(f, state="readonly",width=4))
        label = Label(f, text="Entrada:",background='LightBlue3')
        label.place(x = 20,y = 90)
        E = Entry(f, bd = 0,width=6)
        E.place(x = 90,y = 90)
        B = Button(f, text = m,command = lambda: update_AFN(main,laut,m,Combo,E.get()),highlightbackground='LightBlue3')
        B.place(x = 90, y =130)
        f.mainloop()

def salir(f):
        f.destroy()

def popmessage(m,aut,f,laut):
    if m == "Crear AFN Básico":
        create_AFN(m,f,laut)
    if m == "Unir AFN's":
        unir_conca_AFN(m,f,laut)
    if m == "Concatenar AFN´s":
        unir_conca_AFN(m,f,laut)
    if m == "Operación +":
        operation_aso(m,f,laut)
    if m == "Operación *":
        operation_aso(m,f,laut)
    if m == "Operación ?":
        operation_aso(m,f,laut)

    if m == "Validar Cadena":
        validar(m,f,laut)

    if m == "Salir":
        salir(f)

def frame():
    aut = 1;
    aut +=1;
    MsgButtons = ["Crear AFN Básico","Unir AFN's","Concatenar AFN´s","Operación +","Operación *","Operación ?","Validar Cadena","Salir"]
    Buttons = []
    f = Tk()
    f.geometry('350x300')
    f.configure(bg = 'LightBlue3')
    f.title('Automatas')
    label = Label( f, text="Automatas", font = ("Helvetica", "18"),background='LightBlue3')
    label.place(x = 50,y = 13)
    label = Label( f, text="Numero de Automatas",background='LightBlue3')
    label.place(x =160,y = 13)
    automatas = Label( f, text="0",background='LightBlue3')
    automatas.place(x = 320,y = 13)
    for i in range(len(MsgButtons)):
        Buttons.append(Button(f, text = MsgButtons[i],command = lambda m = MsgButtons[i]: popmessage(m,aut,f,automatas),highlightbackground='LightBlue3'))
        Buttons[i].place(x = 30, y = 39 + i*30)
    f.mainloop()

frame()
