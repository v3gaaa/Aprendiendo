from Empleado import Empleado


class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento

    def __str__(self):
        return f'Gerente [Departamento: {self.departamento}] {super().__str__()}'

    # def mostrar_detalles(self): #Aqui hay plymorfismo de este metodo pero ya que tambien existe herencia no se necestia sobreescribir.
    #     return self.__str__()