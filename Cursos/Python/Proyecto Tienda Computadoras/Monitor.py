class Monitor:
    contador_monitor = 0

    def __init__(self, tam,mar):
        contador_monitor +=1
        self.tamano=tam
        self.marca=mar
        self.idMonitor= contador_monitor
    
    @property
    def tamano(self):
        return self.tamano

    @tamano.setter
    def tamano(self,tam):
        self.tamano=tam

    @property
    def marca(self):
        return self.tipoEntrada

    @marca.setter
    def marca(self,tipo):
        self.tipoEntrada=tipo

    def __str__(self):
        return f"(Tamaño: {self.tipoEntrada}, Marca: {self.marca})"