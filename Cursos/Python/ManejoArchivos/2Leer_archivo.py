# archivo = open('c:\\Cursos\\Python\\Archivos\\Leccion01\\prueba.txt', 'r', encoding='utf8')
#Se puede leer un archivo mediante la ruta

#O si esta dentro de la misma carpeta tan solo con poner el nombre del archivo basta
archivo = open('prueba.txt', 'r', encoding='utf8') #Se usa r (read) para especificar que el archivo se abre en modo lectura


#print(archivo.read()) #IMPRIME EL ARCHIVO ENTERO

# leer algunos caracteres
#print(archivo.read(5)) #Lee los primeros 5 caracteres
#print(archivo.read(3)) #Lee los siguientes 3

# leer lineas completas
#print(archivo.readline())
#print(archivo.readline())

# iterar el archivo
# for linea in archivo:
#     print(linea)

# leer lineas
# print(archivo.readlines())

# acceder a una linea de la lista
#print(archivo.readlines()[1])

# abrimos un nuevo archivo
# a - anexar informacion
archivo2 = open('copia.txt', 'a', encoding='utf8')
archivo2.write(archivo.read())

archivo.close()
archivo2.close()