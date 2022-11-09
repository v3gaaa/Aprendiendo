//Syntax funciones
/*void myFunction() {
  // code to be executed
}*/


//1LAS FUNCIONES NO SE PUEDEN DECLARAR DESPUES DE MAIN
//2SIN EMBARGO SE PUEDEN DECLARAR ANTES Y CODIFICAR SU FUNCIONAMIENTO DESPUES
#include <iostream>
using namespace std;


//1Creas la funcion y la defines antes de main
void myFunction() {
  cout << "Hola mundo";
}

//2SOLO DECLARAS LA FUNCION
void myFunction2();


int main() {
  myFunction();//Llama la funcion
  myFunction2();//Llamas la segunda funcion
  return 0;
}


//2Defines la funcion despues de main
void myFunction2() {
  cout << "Adios mundo";
}