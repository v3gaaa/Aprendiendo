/*A pointer, is a variable that stores the memory address as its value.
A pointer variable points to a data type (like int or string)
The address of the variable you're working with is assigned to the pointer:*/

#include <iostream>
#include <string>
using namespace std;

int main() {
  string food = "Pizza";  // A string variable
  string* ptr = &food;  // A pointer variable that stores the address of food

  // Output the value of food
  cout << food << "\n";

  // Output the memory address of food
  cout << &food << "\n";

  // Output the memory address of food with the pointer
  cout << ptr << "\n";

  // Dereference: Output the value of food with the pointer (Pizza)
  cout << *ptr << "\n";


  //MODIFY POINTER VALUES 

  // Change the value of the pointer
  *ptr = "Hamburger";

  // Output the new value of the pointer (Hamburger)
  cout << *ptr << "\n";

  // Output the new value of the food variable (Hamburger) ALTERING THE POINTER ALTERS THE VARIABLE
  cout << food << "\n";

  return 0;
}