import tkinter

ventana = tkinter.Tk()



# Creating a button with the text "Boton 1" and the size of 30x30.
boton1 = tkinter.Button(ventana, text = "Boton 1", padx = 30, pady = 30)
boton2 = tkinter.Button(ventana, text = "Boton 2", padx = 30, pady = 30)
boton3 = tkinter.Button(ventana, text = "Boton 3", padx = 30, pady = 30)

# Placing the button in the first row and first column.
boton1.grid(row = 0, column = 0)

# Placing the button in the second row and second column.
boton2.grid(row = 1, column = 1)

boton3.grid(row = 2, column = 2)

ventana.mainloop()