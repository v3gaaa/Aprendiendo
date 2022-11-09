//Los metodos son funciones dentro de las clases que los objetos pueden llamar con sus valores individuales


#include <iostream>
using namespace std;

class Car { //CLASE
  public:
    void myMethod() {  // Method/function defined inside the class
        cout << "Hello World!";
    }
    int speed(int maxSpeed); //Declaracion del metodo con sus parametros
};


int Car::speed(int maxSpeed) { //Definicion del metodo, se pasan todos sus parametros (Este es el bloque de codigo)
  return maxSpeed; //Return del metodo
}

int main() {
  Car myObj; // Create an object of Car
  cout << myObj.speed(200); // Call the method with an argument
  return 0;
}