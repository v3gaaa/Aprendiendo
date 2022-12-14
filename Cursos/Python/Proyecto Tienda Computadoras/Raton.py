from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_raton = 0

    def __init__(self,tipo,marca):
        contador_raton += 1
        DispositivoEntrada.__init__(self,tipo,marca)
        self.idRaton = contador_raton
    
    def __str__(self):
        return f"(ID raton: {self.idRaton})"+ DispositivoEntrada.__str__()




raton1 = Raton("inalambrico","Razer")

print(raton1)