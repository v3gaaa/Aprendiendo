
#Metodo para crear objetos

class Persona:
    def __init__(self, nombre, apellido, edad,):
        self._nombre = nombre
        self.apellido = apellido
        self.edad = edad

    @property
    def nombre(self):
        print("LLamando metodo get nombre")
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        print("LLamando metodo set nombre")
        self._nombre = nombre

    def mostrar_detalle(self):
        print(f"Persona: {self._nombre} {self.apellido} {self.edad}")

persona1 = Persona("Juan", "Lopez", 24)
print(persona1.nombre)
persona1.nombre = "Jose"
print(persona1.nombre)