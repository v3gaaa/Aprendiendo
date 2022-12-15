import Raton
import Monitor
import Teclado

class Computadora:
    contador_computadora = 0

    def __init__(self,nom,moni,rat,tecl):
        contador_computadora +=1
        self.nombre = nom
        self.monitor = moni
        self.raton = rat
        self.teclado = tecl
        self.idCompu = contador_computadora

    def __str__(self):
        return f"[ID: {self.idCompu}, Nombre: {self.nombre}, Monitor: {self.monitor}, Raton: {self.raton}, Teclado: {self.teclado}]"

    @property
    def nombre(self):
        return self.nombre

    @nombre.setter
    def nombre(self,nom):
        self.nombre=nom

    @property
    def monitor(self):
        return self.monitor

    @monitor.setter
    def monitor(self,moni):
        self.monitor=moni

    @property
    def raton(self):
        return self.raton

    @raton.setter
    def raton(self,rat):
        self.raton=rat

    @property
    def teclado(self):
        return self.teclado

    @teclado.setter
    def teclado(self,tecl):
        self.teclado=tecl
