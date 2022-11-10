from FiguraGeometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        # super().__init__(lado)
        FiguraGeometrica.__init__(self, lado, lado) #Solo se usa la variable lado para inicializar los valores de la clase padre (se usa lado dos veces por que es el mismo valor)
        Color.__init__(self, color)

    def __str__(self):
        return f"Cuadrado(Lado: {self._alto} Color: {self._color})"

    def calcular_area(self):
        return self.alto * self.ancho #Ya que los valores de la clase padre ya estan inicializados los podemos usar