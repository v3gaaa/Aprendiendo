//Arrays Syntax
/*To declare an array, define the variable type,
specify the name of the array followed by square brackets and
specify the number of elements it should store: int nums[4];*/

//FOR EACH
/*There is also a "for-each loop" ,
which is used exclusively to loop through elements in an array:
SYNTAX
for (type variableName : arrayName) {
  // code block to be executed
}*/


//ARRAYS ONLY CAN STORE 1 TYPE OF VALUE
#include <iostream>
#include <string>
#include <string>
using namespace std;

int main() {
  string cars[4] = {"Volvo", "BMW", "Ford", "Mazda"};
  cars[0] = "Opel"; //Update value of an array
  cout << cars[0]; //Access the value of an array

  string cars[5] = {"Volvo", "BMW", "Ford", "Mazda", "Tesla"}; //Recorrer arrays
  for (int i = 0; i < 5; i++) {
    cout << cars[i] << "\n";
  }

  int myNumbers[5] = {10, 20, 30, 40, 50}; //Recorrer arrays con el FOREACH loop
  for (int i : myNumbers) {
    cout << i << "\n";
  }

  //It is also possible to declare an array without specifying the elements on declaration, and add them later:
  string cars1[5];
  cars1[0] = "Volvo";
  cars1[1] = "BMW";


  /*The result of this shows 20 instead of 5,
  this because the sizeof() operator returns the size of a type in bytes.
  and an int type value contains 4 bytes 4x5 = 20*/
  int myNumbers1[5] = {10, 20, 30, 40, 50};
  cout << sizeof(myNumbers1);

  //To show the real size we divide the size of the array / the size of the data type
  int getArrayLength = sizeof(myNumbers1) / sizeof(int);
  cout << getArrayLength;

  //Loop throug array with size of
  for (int i = 0; i < sizeof(myNumbers1) / sizeof(int); i++) {
    cout << myNumbers[i] << "\n";
  }

  //MATRICES
  string letters[2][4] = {
  { "A", "B", "C", "D" },
  { "E", "F", "G", "H" }
  };

  letters[0][0] = "Z"; //Reassign value in a matrix
  cout << letters[0][2];  //Acces value of a matrix


  //Loop through an array
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 4; j++) {
      cout << letters[i][j] << "\n";
    }
  }
  return 0;
}