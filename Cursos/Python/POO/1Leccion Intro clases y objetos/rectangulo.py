class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura

base_usuario = int(input("Deme la base del rectangulo: "))
altura_usuario = int(input("Deme la altura del rectangulo: "))

rectangulo1 = Rectangulo(base_usuario, altura_usuario)
print(f"Area del rectangulo: {rectangulo1.area()}")