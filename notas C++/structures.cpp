//Structures unlike arrays can store several types of values


#include <iostream>
#include <string>
using namespace std;

int main() {
  struct {
    int myNum; //Miembro de la structura (int)
    string myString; //Miembro de la structura (string)
  } myStructure; //Nombre de la variable de la structura

  myStructure.myNum = 1; //Asignacion de valor al miembro de la structura (myNum)
  myStructure.myString = "Hello World!"; //Assignacion de valor al miembro de la structura (myString)

  cout << myStructure.myNum << "\n"; //Acceso a los miembros de la structura
  cout << myStructure.myString << "\n";
  

  
  //Se pueden crear varias variables apartir de la misma structura para almacenar diferentes datos:
  struct {
    string brand;
    string model;
    int year;
  } myCar1, myCar2; // Añadimos varias variables a la structura

  // Añadimos los datos de la primera structura
  myCar1.brand = "BMW";
  myCar1.model = "X5";
  myCar1.year = 1999;

  // Añadimos los datos de la segunda structura
  myCar2.brand = "Ford";
  myCar2.model = "Mustang";
  myCar2.year = 1969;

  // Accesamos a los datos de las dos structuras
  cout << myCar1.brand << " " << myCar1.model << " " << myCar1.year << "\n";
  cout << myCar2.brand << " " << myCar2.model << " " << myCar2.year << "\n";
  return 0;
}