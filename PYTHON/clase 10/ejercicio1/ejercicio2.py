# En este segundo ejercicio, tendréis que crear una interfaz sencilla
# la cual debe de contener una lista de elementos seleccionables,
# también debe de tener un label con el texto que queráis.

import tkinter
from tkinter import ttk

ventana = tkinter.Tk()
ventana.title("EJERCICIO 2")
ventana.geometry("300x300+0+0")

lblmensaje = tkinter.Label(text="Bienvenidos a la lista")
lblmensaje.place(x=110,y=20)


# CREANDO UNA LISTA
lst1 = tkinter.Listbox(ventana,width=30)
lst1.insert(0,"BELGRANO DE CORDOBA")
lst1.insert(1,"BARCELONA")
lst1.insert(2,"REAL MADRID")
lst1.insert(4,"PSG")
lst1.place(x=50,y=100)

ventana.mainloop()