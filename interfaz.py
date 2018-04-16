from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from automata import *
from convertirAFD import *
from lexico import *
#from interfaz_expresiones import *
from convertidorExpresionesAFN import *

pila_automatas = []
pilaaux = []
tablaAFD = []
analizadorExpresiones = convertidorExpresionesAFN() 
pilaAutomatas = []

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
        elif accion.find("_") != -1:
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
    if m == "Union Especial":
         cadena = accion.split(",")
         pilaaux.clear()
         for item in (cadena):
            pilaaux.append(pila_automatas[int(item)-1])

         pila_automatas[int(cadena[0])-1].union_especial(pilaaux[1:])



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

    if m == "Convertir a AFD":
        indexAutomata = accion.get()
        AFD = convertirAFD(pila_automatas[int(indexAutomata)-1],pilaaux)
        tablaAFD = AFD.getTabla()

    if m == "Léxico":
        cadena = accion
        try:
            if len(tablaAFD) == 0:
                tablaAFD = convertirAFD.leeTabla()
        except:
            tablaAFD = convertirAFD.leeTabla()

        lex = Lexico(tablaAFD,cadena)
        #cadenatokens = ""
        token = ""
        while token != "0":

            token,lexema = lex.getToken()
            print(token +"-----"+  lexema)

    if m ==  "Expresiones Regulares":
        pass



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
    f.mainloop()

def union_esp(m,main,laut):
    f = Tk()
    f.geometry('400x150')
    f.configure(bg = 'LightBlue3')
    f.title(m)
    label = Label(f, text=m, font = ("Helvetica", "18"),background='LightBlue3')
    label.place(x = 60,y = 13)
    if m != "Léxico":
        label = Label(f, text="Coloca los automatas a unir, separa por medio de comas",background='LightBlue3')
    else:
        label = Label(f, text="Introduce una cadena para ser analizada léxicamente",background='LightBlue3')
    label.place(x = 10,y = 40)
    E = Entry(f, bd = 0,width=13)
    E.place(x = 10,y = 80)
    B = Button(f, text = "Finalizar",command = lambda: update_AFN(main,laut,m,E.get(),None),highlightbackground='LightBlue3')
    B.place(x = 150, y =80)
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

def analize(m,f,laut,expresion,cadena):
    #messagebox.showinfo("Exito", str(cadena))
    if cadena =="":
        cadena = "Ǝ"

    lex = Lexico(analizadorExpresiones.tablaAFD,expresion)
    analizadorExpresiones.lex = lex

    valido, AFN = analizadorExpresiones.analizar()
    if AFN not in pila_automatas:
        pila_automatas.append(AFN)


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
    laut.configure(text=str(len(pila_automatas)))
    f.update()


def analizarCadena(m,f,laut,cadena):
    mensaje = ""
    if pilaAutomatas[len(pilaAutomatas)-1].analizaCadena(cadena):
        mensaje = "cadena aceptada"
    else:
        mensaje =  "cadena no aceptada"

    messagebox.showinfo("Éxito",mensaje)
    laut.configure(text=str(len(pila_automatas)))
    f.update()

def expresionesRegulares(m,f,laut):    

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


    button = Button(f, text = "Crear Expresion",command = lambda m = field: analize(m,f,laut,field.get(),field1.get()),highlightbackground='LightBlue3')
    button.place(x=80,y =130)

    button = Button(f, text = "Analizar Cadena",command = lambda m = field: analizarCadena(m,f,laut,field1.get()),highlightbackground='LightBlue3')
    button.place(x=230,y =130)
    f.mainloop()

    

def popmessage(m,aut,f,laut):
    if m == "Crear AFN Básico":
        create_AFN(m,f,laut)
    if m == "Unir AFN's":
        unir_conca_AFN(m,f,laut)
    if m == "Union Especial":
        union_esp(m,f,laut)
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
    if m == "Convertir a AFD":
        operation_aso(m,f,laut)
    if m == "Léxico":
        union_esp(m,f,laut)

    if m == "Salir":
        salir(f)

    if m == "Expresiones Regulares":
        expresionesRegulares(m,f,laut)
        



def frame():
    tablaAFD.clear()
    aut = 1;
    aut +=1;
    MsgButtons = ["Crear AFN Básico","Unir AFN's","Union Especial","Concatenar AFN´s","Operación +","Operación *","Operación ?","Validar Cadena","Convertir a AFD","Léxico","Expresiones Regulares","Salir"]
    Buttons = []
    f = Tk()
    f.geometry('400x450')
    f.configure(bg = 'LightBlue3')
    f.title('Automatas')
    label = Label( f, text="Automatas", font = ("Helvetica", "18"),background='LightBlue3')
    label.place(x = 50,y = 13)
    label = Label( f, text="Numero de Automatas",background='LightBlue3')
    label.place(x =200,y = 13)

    label = Label( f, text="Pila Automatas Expr",background='LightBlue3')
    label.place(x =200,y = 80)

    automatas = Label( f, text="0",background='LightBlue3')
    automatas.place(x = 360,y = 13)

    automatas = Label( f, text="0",background='LightBlue3')
    automatas.place(x = 360,y = 80)


    for i in range(len(MsgButtons)):
        Buttons.append(Button(f, text = MsgButtons[i],command = lambda m = MsgButtons[i]: popmessage(m,aut,f,automatas),highlightbackground='LightBlue3'))
        Buttons[i].place(x = 30, y = 39 + i*30)
    f.mainloop()

frame()
