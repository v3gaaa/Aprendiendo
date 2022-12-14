import Raton
import Monitor
import Teclado

class Computadora:
    contador_computadora = 0

    def __init__(self,nom,moni,rat,tecl):
        self.nombre = nom
        self.monitor = moni
        self.raton = rat
        self.teclado = tecl