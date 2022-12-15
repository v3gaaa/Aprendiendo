from Computadora import Computadora
from Raton import Raton
from Monitor import Monitor
from Teclado import Teclado

class Orden:
    contador_ordenes = 0

    def __init__(self):
        Orden.contador_ordenes +=1
        self.idOrden = Orden.contador_ordenes
        self.listaOrden = []

    def agregar_computadora(self,compu):
        self.listaOrden.append(compu)

    def imprimirOrden(self):
        strOrden = ""
        for i in range(len(self.listaOrden)):
            strOrden += f"\n {self.listaOrden[i]}"
        return strOrden

    #def __str__(self):
        #strOrden = self.imprimirOrden
        #return strOrden
            
            
