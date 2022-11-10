from Cuadrado_ClaseHija import Cuadrado


cuadrado1 = Cuadrado(25,"Rojo")
print(cuadrado1.ancho) #Se puede accesar a los atributos de las clases padres aunque no los hayamos mandado ya que fueron inicializados en la clase hija
print(cuadrado1.alto)
print(cuadrado1.color)
print(cuadrado1.calcular_area())


#MRO - METHOD RESOLUTION ORDER
#Nos dice el orden de jerarquia con el que se llaman las clases padres
print(Cuadrado.mro())