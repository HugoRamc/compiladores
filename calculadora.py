from tkinter import *
from tkinter import messagebox
from tkinter import ttk

def popmessage(m,L):
    if m == "DEL":
        L.configure(text = "")

    else:
        L.configure(text = L.cget("text")+ m)



    L.configure(anchor="se")
    print(m)
def frame():
    Numeros = ["7","8","9","DEL","AC","4","5","6","x","÷","1","2","3","+","-","0",".","(",")","="]
    Cientifica = ["SEN","COS","TAN","LN","^","√","","","",""]
    eq = "="
    Buttons = []
    f = Tk()
    f.geometry('500x500')
    f.configure(bg = 'LightBlue3')
    f.title('Calculadora')
    x = 0;
    y = 100;
    L = Label(f, bd = 0,width=38)
    L.place(x=72, y = y-30)
    Mode = Button(f, text = "MODE" , width = 5,command = lambda : popmessage("MODE",L),highlightbackground='LightBlue3')
    Mode.place(x=70,y = y)
    for i in range(len(Numeros)):
        if i%5 == 0:
            y = y + 30
            x = 0
        x = x + 70
        Buttons.append(Button(f, text = Numeros[i], width = 5,command = lambda m = Numeros[i]: popmessage(m,L),highlightbackground='LightBlue3'))
        Buttons[i].place(x = x, y = y)

    f.mainloop()
frame()
