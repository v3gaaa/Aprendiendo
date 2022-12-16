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
else:
    print('No se arrojó ninguna excepción') #Unicamente se ejecuta si no se arrojo ninguna excepcion
finally:
    print('Ejecución del bloque finally') #Se ejecuta SIEMPRE una vez se haya acabado el procesamiento de excepciones

print(f'Resultado: {resultado}')
print('Continuamos...')