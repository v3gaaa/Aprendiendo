import Computadora

class Orden:
    contador_ordenes = 0

    def __init__(self):
        contador_ordenes +=1
        self.idOrden = contador_ordenes
        self.listaOrden = []

    def agregar_computadora(self,compu):
        self.listaOrden.append(compu)

    def __str__(self):
        for i in range(len(self.listaOrden)):
            print(self.listaOrden[i].__str__())