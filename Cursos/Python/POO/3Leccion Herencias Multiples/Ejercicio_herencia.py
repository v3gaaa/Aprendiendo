from Rectangulo_ClaseHija import Rectangulo
from Cuadrado_ClaseHija import Cuadrado
from FiguraGeometrica import FiguraGeometrica
from Color import Color

#No se puede instanciar una clase abstracta (crear un objeto)
# figura1 = FiguraGeometrica()


print("Creacion objeto cuadrado".center(50,"-"))
cuadrado1 = Cuadrado(5,"Rojo") 
print(cuadrado1) #Se llama al metodo STR ya que print intenta convertir automaticamente el objeto a string
print(f"Calculo area: {cuadrado1.calcular_area()}") #Se llama como FUNCION a la funcio calcular area



print("Creacion objeto rectangulo".center(50,"-"))
rectangulo1 = Rectangulo(ancho=5,alto=2,color="Azul") #Esto es una forma de documentar el codigo ya que el nombre de las variables es claro
rectangulo1.ancho = -2
print(rectangulo1)
print(f"Calculo area: {rectangulo1.calcular_area()}")