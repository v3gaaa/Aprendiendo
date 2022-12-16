try: #Muchas veces manejando archivos se van a dar excepciones entonces es recomendado ponerlos dentro de un bolque try-catch
    
    archivo = open('prueba.txt', 'w', encoding="utf8") #Abre un archivo ya existente o crea uno con ese nombre, se usa encoding para especificar el juego de caracteres que se usara
    #Despues de abrir el archivo se pone el modo con el que este se abre en este caso w de write, para escribir desde 0 o borrar la informacion previa del archivo y empezar de 0
    archivo.write('Agregamos información al archivo\n') #con write escribimos dentro del archivo
    archivo.write('Adios')
    
except Exception as e:
    print(e)
finally:
    archivo.close() #.close() cierra el archivo. Se pone en un bloque finally para que se cierre el archivo independientemente de que exista un error