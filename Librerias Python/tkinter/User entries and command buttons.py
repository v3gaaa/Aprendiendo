import tkinter
from random import randint

ventana = tkinter.Tk()
ventana.geometry("700x400")

""" Explicacion
    The function textentry() is called when the button "CLICK" is pressed. 
    
    The function textentrylabel() is called when the button "CLICK TO SHOW" is pressed. 
    
    The function textentry() prints the text entered in the text box. 
    
    The function textentrylabel() shows the text entered in the text box in the label. 
    
    The text box is called cajaTexto. 
    
    The label is called etiqueta. 
    
    The buttons are called boton1 and boton2. 
    
    The window is called ventana. 
    
    The font is called Helvetica 12. 
    
    The window is mainloop. 
    
    The window is called ventana. 
    """

def textentry():
    text_entry = cajaTexto.get()
    print(text_entry)

def textentrylabel():
    text_entry_show = cajaTexto.get()
    etiqueta = tkinter.Label(ventana, text= "Hola " + text_entry_show)
    etiqueta.pack()

def insulto():
    text_entry_show = cajaTexto.get()
    insulto = tkinter.Label(ventana, text= "Me la pelas " + text_entry_show)
    if randint(0,2) == 0:
        insulto = tkinter.Label(ventana, text= text_entry_show + " Chupala")
    elif randint(0,2) == 1:
        insulto = tkinter.Label(ventana, text= "Pudrete " + text_entry_show)
    elif randint(0,2) == 2:
        insulto = tkinter.Label(ventana, text= "No seas idiota " + text_entry_show)
        
    insulto.pack()

Instruccion = tkinter.Label(ventana, text= "Hola, dame tu nombre", bg = "blue")
cajaTexto = tkinter.Entry(ventana, font = "Helvetica 12")
cajaTexto.pack(fill = tkinter.X)

boton1 = tkinter.Button(ventana, text = "Imprimo tu nombre", command = textentry)
boton1.pack(fill = tkinter.X)

boton2 = tkinter.Button(ventana, text = "Te saludo", command = textentrylabel)
boton2.pack(fill = tkinter.X)

boton3 = tkinter.Button(ventana, text = "Sorpresa", command = insulto)
boton3.pack(fill = tkinter.X)

ventana.mainloop()