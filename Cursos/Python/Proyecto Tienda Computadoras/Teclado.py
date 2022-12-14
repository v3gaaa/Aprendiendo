from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclado = 0

    def __init__(self,tipo,marca):
        contador_teclado += 1
        DispositivoEntrada.__init__(self,tipo,marca)
        self.idTeclado = contador_teclado
    
    def __str__(self):
        return f"(ID teclado: {self.idTeclado})"+ DispositivoEntrada.__str__()