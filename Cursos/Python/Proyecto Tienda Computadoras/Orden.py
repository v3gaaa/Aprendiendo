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
            strOrden += f"\n \n {self.listaOrden[i]}"
        return strOrden

           
if __name__ == "__main__":
    raton1 = Raton("USB","HP")
    teclado1 = Teclado("Inalambrico","Gamer")
    monitor1 = Monitor("27 pulgadas","LG")
    compu1 = Computadora("Computadora Gamer", monitor1, raton1, teclado1)
    
    raton2 = Raton("USB","Logitech")
    teclado2 = Teclado("USB","HP")
    monitor2 = Monitor("30 pulgadas","Samsung")
    compu2 = Computadora("Computadora Diseño", monitor2, raton2, teclado2)
    
    orden = Orden()
    orden.agregar_computadora(compu1)
    orden.agregar_computadora(compu2)
    print(orden.imprimirOrden())