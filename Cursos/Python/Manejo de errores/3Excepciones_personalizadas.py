class NumerosIdenticosException(Exception): #La clase de excepcion personalizada tiene que heredar de Exception

    def __init__(self, mensaje):
        self.message = mensaje
        
        
resultado = None
try:
    a = int(input('Primer número: '))
    b = int(input('Segundo número: '))
    if a == b:
        raise NumerosIdenticosException('números identicos')
    resultado = a/b
except Exception as e:
    print(f'Exception - Ocurrió un error: {e} , {type(e)}')

print(f'Resultado: {resultado}')