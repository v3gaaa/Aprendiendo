from Color import Color
from FiguraGeometrica import FiguraGeometrica

class Rectangulo(FiguraGeometrica,Color):
    def __init__(self, ancho, alto,color):
        FiguraGeometrica.__init__(self,ancho, alto)
        Color.__init__(self,color)

    def __str__(self):
        return f"Rectangulo(Ancho: {self.ancho}, Alto: {self.alto} Color: {self.color})"

    def calcular_area(self):
        return self.ancho * self.alto