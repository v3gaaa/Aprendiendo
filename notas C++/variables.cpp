
//Syntax==
//type variableName = value;

#include <iostream>
#include <string> //Habilita el uso de variables strings
using namespace std;

int main() {
  int myNum = 15;   // Now myNum is 15
  myNum = 10;       // Now myNum is 10
  cout << myNum;

  int myNum2 = 5;               // Integer (whole number without decimals)
  double myFloatNum = 5.99;    // Floating point number (with decimals)
  char myLetter = 'D';         // Character
  string myText = "Hello";     // String (text)
  bool myBoolean = true;       // Boolean (true or false)
  int x = 5, y = 6, z = 50; // Declarar varias variables de una

  cout << "\nEsto es " << myFloatNum << " un float";
  x = 5;
  y = 6;
  int sum = x + y;
  cout << endl << sum << endl; //Suma de variables y salto de linea con endl
  
  const float PI = 3.14; //Constant value cannot be updated

  string firstName = "John ";
  string lastName = "Doe";
  string fullName = firstName + lastName; //String concatenation
  // string lenght == variablename.lenght()
  string myString = "Hello";
  cout << fullName;
  cout << myString[0];
  

  // && == and
  // || == or
  // ! == not
  return 0;
}