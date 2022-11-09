//FUNCTION OVERLOAD
//Funciona para tener varias funciones con el mismo nombre pero diferente tipo de datos y parametros.

#include <iostream>
using namespace std;

int plusFunc(int x, int y) { //Declaras primera funcion con tipo de dato int
  return x + y;
}

double plusFunc(double x, double y) { //Declaras segunda funcion con tipo de dato double
  return x + y;
}

void plusFunc(string x, string y) { //Declaras la tercer funcion sin tipo de dato global pero si en los parametros
    cout << x << y;
}


//RECURSION
//Llamar funciones dentro de funciones
int sum(int k) {
  if (k > 0) {
    return k + sum(k - 1);
  } else {
    return 0;
  }
}


int main() {
  int myNum1 = plusFunc(8, 5); 
  cout << "Int: " << myNum1 << "\n";

  double myNum2 = plusFunc(4.3, 6.26);
  cout << "Double: " << myNum2 << "\n";
  
  plusFunc("String: ", "Hola mundo");

  int result = sum(10);
  cout << result;

  return 0;
}