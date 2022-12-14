class DispositivoEntrada:
    def __init__(self, tipo,mar):
        self.tipoEntrada=tipo
        self.marac=mar
    
    @property
    def gettipoEntrada(self):
        return self.tipoEntrada
