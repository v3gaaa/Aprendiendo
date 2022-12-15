from DispositivoEntrada import DispositivoEntrada

class Teclado(DispositivoEntrada):
    contador_teclado = 0

    def __init__(self,tipo,marca):
        Teclado.contador_teclado += 1
        super().__init__(tipo,marca)
        self.idTeclado = Teclado.contador_teclado
    
    def __str__(self):
        return f"(ID teclado: {self.idTeclado}) {super().__str__()}"
    
    
    
if __name__ == "__main__":
    teclado1 = Teclado("USB","HP")
    print(teclado1)
    teclado2 = Teclado("Inalambrico","Gamer")
    print(teclado2)