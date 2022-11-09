class Cubo:
    def __init__(self, largo, ancho, alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
    def volumen(self):
        return self.ancho * self.largo * self.alto

ancho = int(input("Dame el ancho: "))
largo = int(input("Dame el largo: "))
alto = int(input("Dame el alto: "))

cubo1 = Cubo(largo, ancho, alto)
print(f"El volumen es: {cubo1.volumen()}")