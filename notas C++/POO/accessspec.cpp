#include <iostream>
using namespace std;

/*public - members are accessible from outside the class
private - members cannot be accessed (or viewed) from outside the class
protected - members cannot be accessed from outside the class, however, 
they can be accessed in inherited classes.*/

class MyClass {
  public:    // Public access specifier
    int x;   // Public attribute
    // Setter

    //Metodo set y get definidos en el clase publica para accesar y modificar las variables privadas
    void sety(int s) {
      y = s;
    }
    // Getter
    int gety() {
      return y;
    }


  private:   // Private access specifier
    int y;   // Private attribute
};



int main() {
  MyClass myObj;
  myObj.x = 25;  // Allowed (public)
  //myObj.y = 50;  // Not allowed (private)
  //If you try to access a private member, an error occurs:
  //error: y is private

  //ENCAPSULATION
  //The meaning of Encapsulation, is to make sure that "sensitive" data is hidden from users.
  //To achieve this, you must declare class variables/attributes as private.
  //We can acces private members in classes with get and set METHODS
  
  myObj.sety(50000);
  cout << myObj.gety();


  return 0;
}

