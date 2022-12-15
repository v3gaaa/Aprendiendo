class Monitor:
    contador_monitor = 0

    def __init__(self, tam,mar):
        Monitor.contador_monitor +=1
        self._tamano=tam
        self._marca=mar
        self.idMonitor= Monitor.contador_monitor
    
    @property
    def tamano(self):
        return self._tamano

    @tamano.setter
    def tamano(self,tam):
        self._tamano=tam

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,mar):
        self._marca=mar

    def __str__(self):
        return f"(IdMonitor: {self.idMonitor}, Tamaño: {self._tamano}, Marca: {self._marca})"
    
    
if __name__ == "__main__":
    monitor1 = Monitor("27 pulgadas","LG")
    print(monitor1)
    monitor2 = Monitor("30 pulgadas","Samsung")
    print(monitor2)
    monitor2.marca = "HP"
    print(monitor2)
