class DispositivoEntrada:
    def __init__(self, tipo,mar):
        self._tipoEntrada=tipo
        self._marca=mar
    
    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @tipoEntrada.setter
    def tipoEntrada(self,tipo):
        self._tipoEntrada=tipo

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,mar):
        self._marca=mar
        
    def __str__(self):
        return f"(Tipo de entrada: {self._tipoEntrada}, Marca: {self._marca})"