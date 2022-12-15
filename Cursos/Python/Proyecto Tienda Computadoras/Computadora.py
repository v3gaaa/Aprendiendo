from Raton import Raton
from Monitor import Monitor
from Teclado import Teclado

class Computadora:
    contador_computadora = 0

    def __init__(self,nom,moni,rat,tecl):
        Computadora.contador_computadora +=1
        self._nombre = nom
        self._monitor = moni
        self._raton = rat
        self._teclado = tecl
        self._idCompu = Computadora.contador_computadora

    def __str__(self):
        return f"[ID: {self._idCompu}, Nombre: {self._nombre}, \n Monitor: {self._monitor}, \n Raton: {self._raton}, \n Teclado: {self._teclado}]"

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,nom):
        self._nombre=nom

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self,moni):
        self._monitor=moni

    @property
    def raton(self):
        return self._raton

    @raton.setter
    def raton(self,rat):
        self._raton=rat

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self,tecl):
        self._teclado=tecl


if __name__ == "__main__":
    raton1 = Raton("USB","HP")
    teclado1 = Teclado("Inalambrico","Gamer")
    monitor1 = Monitor("27 pulgadas","LG")
    compu1 = Computadora("Computadora Gamer", monitor1, raton1, teclado1)
    print(compu1)