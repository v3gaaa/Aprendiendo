
#La clase FIGURAGEOMETRICA es abstracta y no se pueden crear objetos ni nada apartir de ella y obliga a las clases hijas a instancear los metodos seleccionados.
from abc import ABC, abstractmethod  #Libreria para clases abstractas

class FiguraGeometrica(ABC): #Le ponemos ABC a la clase para indicar que es una clase abstracta
    def __init__(self, ancho, alto):

        #Simple validacion para ver si el valor es mayor a 0
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print("ERORR: Valor de ancho negativo ancho = 0")

        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print("ERORR: Valor de ancho negativo ancho = 0")
            
        

    def __str__(self):
            return f"FiguraGeometrica(Ancho: {self._ancho}, Alto: {self._alto})"

    @property
    def ancho(self):
        #Lamando metodo get ancho
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        #LLamando metodo set alto
        if self._validar_valor(ancho):
            self._ancho = ancho
        else:
            self._ancho = 0
            print("ERORR: Valor de ancho negativo ancho = 0")

    @property
    def alto(self):
        #Lamando metodo get alto
        return self._alto

    @alto.setter
    def alto(self, alto):
        #LLamando metodo set alto
        if self._validar_valor(alto):
            self._alto = alto
        else:
            self._alto = 0
            print("ERORR: Valor de ancho negativo ancho = 0")

    @abstractmethod #Los metodos abstractos no pueden contener implementacion
    def calcular_area(self):
        pass #Por eso ponemos pass para definir nuestro metodo correctamente
            
    #Este tipo de metodos sirven para que obligatoriamente las clases hijas deban contener estos metodos


    def _validar_valor(self,valor): #metodo encapsulado (no significa nada pero es buena practica para avisar que este metodo solo se usa dentro de la clase)
        #ESTA FUNCION ES PARA VALIDAR SI EL ATRIBUTO ES POSITIVO
        #SE CREA ESTA FUNCION PARA QUE FUNCIONE CON LOS VALORES ASIGNADOS DESPUES DE LA INICIALIZACION DEL OBJETO
        return True if valor > 0 else False
    