//PARAMETROS EN FUNCIONES

#include <iostream>
#include <string>
using namespace std;

void myFunction(string fname, int edad) { //Declaras la funcion con sus argumentos
  cout << "Hola" << fname << "Tienes" << edad << "años";
}

void myFunction2(string country = "Norway") { //Declarar funcion con parametro DEFAULT
  cout << country << "\n";
}

//Returner valores de una funcion
//If you want the function to return a value, you can use a data type (such as int, string, etc.)
int myFunction3(int y, int x) {
  return y + x; //Regresa un valor
}

//Pasar Arrays a una funcion
void myFunction4(int myNumbers[5]) {
  for (int i = 0; i < 5; i++) {
    cout << myNumbers[i] << "\n";
  }
}

int main() {
  myFunction("Liam",22); //LLamas a la funcion con el dato que quieres pasar
  myFunction("Jenny",18);
  
  myFunction2();// Printea Norway
  myFunction2("France");//Printea France

  int z = myFunction3(5,3); //Almacena el return de la funcion 8 (5+3)
  cout << z; //Printea 8

  int myNumbers[5] = {10, 20, 30, 40, 50};
  myFunction4(myNumbers); //LLamar a la funcion pasando el array

  return 0;
}