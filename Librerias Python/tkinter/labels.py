import tkinter

# Creating a window with the dimensions of 400x300.
ventana = tkinter.Tk()
ventana.geometry("400x300")

# Creating a label with the text "Hola Mundo" and a background color of blue.
etiqueta = tkinter.Label(ventana, text = "Hola Mundo", bg = "blue")

# Creating a label with the text "Como estan ?" and a background color of green.
etiqueta2 = tkinter.Label(ventana, text = "Como estan ?", bg = "green")

# Placing the label at the bottom of the window.
etiqueta.pack(side = tkinter.BOTTOM)

# Filling the label with the X axis.
etiqueta.pack(fill = tkinter.X)

# Filling the label with the Y axis and expanding it.
etiqueta2.pack(fill = tkinter.Y, expand = True)

# A function that keeps the window open until the user closes it.
ventana.mainloop()
