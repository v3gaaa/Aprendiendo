class Persona:
    contador_personas = 0 #Cada vez que creemos un objeto vamos a sumarle 1 a esta variable de clase
    #Recordemos que las variables clase se comparten entre

    def __init__(self,nombre,edad):
        Persona.contador_personas += 1 #Lo ponemos dentro del init para que se inicialice cada que se cree un objeto asi sume +1
        self.id_persona = Persona.contador_personas #Le añadimos el ID del numero de objeto que es a cada objeto que se inicialice
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Persona [{self.id_persona}  {self.nombre}  {self.edad}]"




persona1 = Persona("Juan", 28)
print(persona1)
persona2 = Persona("Carla", 19)
print(persona2)
print(f"Valor del contador de personas: {Persona.contador_personas}")