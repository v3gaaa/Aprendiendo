#include <iostream>
using namespace std;

int main() {
  int x, y;
  int sum;
  cout << "Type a number: "; //Esto es solo un print
  cin >> x; //Aqui se pedira el input (Solo acepta ints) se imprime al lado del ultimo print y termina la linea
  cout << "Type another number: ";
  cin >> y;
  sum = x + y;
  cout << "Sum is: " << sum << endl;

  string firstName;
  cout << "Type your first name: ";
  cin >> firstName; // get user input from the keyboard
  cout << "Your name is: " << firstName;
  return 0;
}