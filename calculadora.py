from tkinter import *
from tkinter import messagebox
from tkinter import ttk


def popmessage(m,L,frame,Buttons):
    if m == "MODE":
        act_int(frame,Buttons)
    elif m == "DEL":
        L.configure(text = "")
    elif m == "←":
        L.configure(text = L.cget("text")[:-1])
    elif m == "=":
        print("Aqui se llama a la magia")
    else:
        L.configure(text = L.cget("text")+ m)


    L.configure(anchor="se")
def frame():
    Numeros = ["7","8","9","DEL","←","4","5","6","x","÷","1","2","3","+","-","0",".","(",")","="]
    cientifica = ["SEN","COS","TAN","LN","^","√","","","",""]
    Buttons = []
    ButCient = []
    f = Tk()
    f.geometry('500x500')
    f.configure(bg = 'LightBlue3')
    f.title('Calculadora')
    x = 0;
    y = 60;
    L = Label(f, bd = 0,width=38)
    L.place(x=72, y = y)
    for i in range(len(cientifica)):
        if i%5 == 0:
            y = y + 30
            x = 0
        x = x + 70
        ButCient.append(Button(f, text = cientifica[i], width = 5,command = lambda m = cientifica[i]: popmessage(m,L,f,Buttons),highlightbackground='LightBlue3'))
        ButCient[i].place(x = x, y = y)
    for i in range(len(Numeros)):
        if i%5 == 0:
            y = y + 30
            x = 0
        x = x + 70
        Buttons.append(Button(f, text = Numeros[i], width = 5,command = lambda m = Numeros[i]: popmessage(m,L,f,Buttons),highlightbackground='LightBlue3'))
        Buttons[i].place(x = x, y = y)

    f.mainloop()
frame()
