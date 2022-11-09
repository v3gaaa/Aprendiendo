#include <iostream>
#include <string>
using namespace std;

int main() {
  string food = "Pizza"; //Food variable
  string &meal = food;  //Reference to food variable

  cout << food << "\n"; //printea "Pizza"
  cout << meal << "\n"; //printea "Pizza"


  //Las variables son objetos y podemos accesar a su espacio de memoria con:
  string food = "Pizza";
  cout << &food; // Printea 0x6dfed4


  return 0;
}