try:
    10/0
    #Exception es una "Clase" la cual es la clase padre de todos los tipos de excepcion que existen en python (ver imagen)
    #En este caso podemos procesar la excepcion zero Division error que es clase hija de la clase arithmetic error y a su vez de la clase Excpetion
    
except Exception as e: #Guardamos el tipo de excepcion que arroja en una variable eh imprimimos el error
    print(f'Ocurrió un error: {e}')
    
    
    
try:
    10/0
    #En este caso si usamos directamente la excepcion ZeroDivisionError sin embargo el resultado es el mismo
    
except ZeroDivisionError as e: #Guardamos el tipo de excepcion que arroja en una variable eh imprimimos el error
    print(f'Ocurrió un error: {e}')
    
    
#Tambien podemos procesar errores con literales. Esto nos ayuda a que si hay un error en nuestro programa se procese el error pero se siga corriendo.
a= 10
b=0
resultado = None

try:
    resultado = a/b
except Exception as e: 
    print(f'Ocurrió un error: {e}')
    
print(f"Resultado: {resultado}") #En este caso como hubo un error no se reasigna el valor de resultado y se imprime None


a= 10
b=5
resultado = None

try:
    resultado = a/b
except Exception as e: 
    print(f'Ocurrió un error: {e}') #En este caso como no hay error no se imprime el error y se reasigna el resultado de None a la Division de a/b
    
print(f"Resultado: {resultado}")


a= "10"
b=5
resultado = None

try:
    resultado = a/b
except Exception as e: 
    print(f'Ocurrió un error: {e}') #En este caso como la variable a es un string nos va a mandar otro tipo de error
    
print(f"Resultado: {resultado}")


#Tambien si queremos procesar varias excepciones especificas a la vez podemos hacerlo

a= "10"
b=5
resultado = None

try:
    resultado = a/b
except ZeroDivisionError as e: 
    print(f'Ocurrió un error: {e}, {type(e)}') #Aqui se procesaria la excepcion si existiera una division entre 0
except TypeError as e:
    print(f'Ocurrió un error: {e}, {type(e)}') #Aqui se procesaria la excepcion si existeria algun error en los tipos de datos
    
print(f"Resultado: {resultado}")

#Tambien se pueden declarar literales dentro del codigo try

resultado = None
try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    resultado = a/b
except ZeroDivisionError as e:
    print(f'ZeroDivisionError - Ocurrió un error: {e} , {type(e)}')
except TypeError as e:
    print(f'TypeError - Ocurrió un error: {e} , {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrió un error: {e} , {type(e)}')

print(f'Resultado: {resultado}')
print('Continuamos...')