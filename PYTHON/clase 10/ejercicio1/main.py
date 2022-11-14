
#En este ejercicio tenéis que crear una lista de RadioButton que muestre
# la opción que se ha seleccionado
#y que contenga un botón de reinicio para que deje todo como al principio.
#Al principio no tiene que haber una opción seleccionada.

import tkinter
from tkinter import ttk

ventana = tkinter.Tk()
ventana.geometry("300x300+0+0")

def mostrar():
    if seleccionado.get()==1:
        mensaje="Has seleccionado si"
    if seleccionado.get()==2:
        mensaje="Has selecionado no"
    if seleccionado.get()==3:
        mensaje= "Has selecionado tal vez"

    lblMensaje.config(text=mensaje)

def reiniciar():
    seleccionado.set(None)
    lblMensaje.config(text="")

ventana.columnconfigure(0,weight=1)
ventana.columnconfigure(1,weight=3)

seleccionado = tkinter.IntVar()
seleccionado.set(None)

r1 = ttk.Radiobutton(ventana, text='si', value=1, variable = seleccionado, command=mostrar).place(x=100,y=70)
r2 = ttk.Radiobutton(ventana, text='no', value=2, variable = seleccionado, command=mostrar).place(x=100,y=90)
r3 = ttk.Radiobutton(ventana, text='tal vez', value=3, variable = seleccionado, command=mostrar).place(x=100,y=110)


lblMensaje = tkinter.Label(ventana)
lblMensaje.place(x=100,y=150)

btnReiniciar= tkinter.Button(ventana, text= "reiniciar" , command=reiniciar)
btnReiniciar.pack
btnReiniciar.place(x=100,y=200)

ventana.mainloop()

