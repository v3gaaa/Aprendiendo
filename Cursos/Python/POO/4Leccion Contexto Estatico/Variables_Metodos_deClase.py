
#VARIABLES DE CLASE y METODOS DE CLASE

class MiClase:

    variable_clase = "Valor variable clase" #Las variables de clase se asocian con la clase en si y no con los objetos
    #NO HAY NECESIDAD DE CREAR UN OBJETO PARA LLAMAR A LA VARIABLE DE CLASE

    def __init__(self,variable_instancia):
        self.variable_instancia = variable_instancia #Variable de instancia; se accesa apartir de un opbjeto.


    #METODOS STATICOS: Los metodos staticos son metodos que se asocian con la clase en si al igual que las variables de clase
    @staticmethod #Esto es un decorador que afecta al metodo siguiente; Este en particular define al metodo siguiente como estatico.

    def metodo_estatico(): #UN METODO ESTATICO NO PUEDE ACCEDER A LAS VARIABLES DE INSTANCIA (NO USA SELF)
        #No pueden acceder a variables de instancia ya que estas se definen cuando se crea un objeto y estos metodos se inicializan antes de eso
        #Esto viene siendo el contexto estatico que es la definicion de la clase
        #Y el contexto dinamico es cuando la clase ya fue creada y se inicializan objetos e instancias
        print(MiClase.variable_clase) #Si se puede acceder a las variables de clase (Indirectamente con el nombre de la clase)

    #Los metodos estaticos no recibe informacion de la clase en si misma, no tienen relacion con la clase


    #METODO DE CLASE: Si recibe un contexto de clase. Recibe algo parecido al parametro self (cls)
    @classmethod #Decorador que indica que es un metodo de clase
    def metodo_clase(cls): #Parametro de la clase en si misma
        print(cls.variable_clase) #Se puede acceder directamente a todas las variables o metodos de clase sin necesidad de ponerlas como parametro (parecido a self)


    def metodo_instancia(self):
        self.metodo_clase() #Desde los metodos de instancia tambien se pueden llamar a los metodos de clase y estaticos



print(MiClase.variable_clase) #No se necesita crear un objeto para llamar una variable de clase

objeto1 = MiClase("Valor variable instancia") #Para las variables de instancia se necesita crear un objeto
print(objeto1.variable_instancia) 


#Sin embargo un objeto tambien puede llamar una variable de clase
print(objeto1.variable_clase)


#Como en python las clases en si tambien son objetos se pueden crear variables de clase al "Vuelo" o sea a medio codigo.
MiClase.variable_clase2 = "Valor variable clase 2"
print(MiClase.variable_clase2)

MiClase.metodo_estatico #No se necesita crear un objeto para llamar un metodo estatico al igual que una variable de clase.
MiClase.metodo_clase #Tampoco se necesita crear un objeto para llamarlo aunque los objetos tambien pueden llamarlo