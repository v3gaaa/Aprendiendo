// La herencia en clases es que una clase "hija" herede los metodos y atributos de una clase "padre"

//To inherit from a class, use the : symbol.

//In the example below, the Car class (child) inherits the attributes and methods
//from the Vehicle class (parent):

#include <iostream>
#include <string>
using namespace std;

// Base class
class Vehicle {
  public:
    string brand = "Ford";
    void honk() {
      cout << "Tuut, tuut! \n" ;
    }
};

// Derived class
class Car: public Vehicle {
  public:
    string model = "Mustang";
};

int main() {
  Car myCar;
  myCar.honk();
  cout << myCar.brand + " " + myCar.model;
  return 0;
}