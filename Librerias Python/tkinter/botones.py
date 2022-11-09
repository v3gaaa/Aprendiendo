import tkinter

ventana = tkinter.Tk()
ventana.geometry("400x300")

nombre = input("Cual es tu Nombre")

def saludo():
    print("Hola " + nombre)


# Creating a button that will print out a greeting when pressed.
boton1 = tkinter.Button(ventana, text = "Presiona para saludo", padx = 30, pady = 30, command = saludo)
boton1.pack()


