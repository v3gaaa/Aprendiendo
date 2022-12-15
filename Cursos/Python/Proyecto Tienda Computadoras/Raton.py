from DispositivoEntrada import DispositivoEntrada

class Raton(DispositivoEntrada):
    contador_raton = 0

    def __init__(self,tipo,marca):
        Raton.contador_raton += 1
        super().__init__(tipo,marca)
        self.idRaton = Raton.contador_raton
    
    def __str__(self):
        return f"(ID raton: {self.idRaton}) "+ super().__str__()


if __name__ == "__main__":
    raton1 = Raton("USB","HP")
    print(raton1)
    raton2 = Raton("Inalambrico","Gamer")
    print(raton2)
