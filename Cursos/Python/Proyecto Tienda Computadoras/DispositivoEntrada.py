class DispositivoEntrada:
    def __init__(self, tipo,mar):
        self.tipoEntrada=tipo
        self.marca=mar
    
    @property
    def tipoEntrada(self):
        return self.tipoEntrada

    @tipoEntrada.setter
    def tipoEntradas(self,tipo):
        self.tipoEntrada=tipo

    @property
    def marca(self):
        return self.tipoEntrada

    @marca.setter
    def marca(self,tipo):
        self.tipoEntrada=tipo

    def __str__(self):
        return f"(Tipo de entrada: {self.tipoEntrada}, Marca: {self.marca})"