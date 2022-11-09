//while Syntax
/*while (condition) {
  // code block to be executed
}*/

//Do while Syntax == It helps to run de code block at least 1 time before checking condition
/*do {
  // code block to be executed
}
while (condition);*/

//For Syntax
/*for (statement 1; statement 2; statement 3) {
  // code block to be executed
}
Statement 1 is executed (one time) before the execution of the code block.

Statement 2 defines the condition for executing the code block.

Statement 3 is executed (every time) after the code block has been executed.*/

#include <iostream>
using namespace std;

int main(void) {
  int i = 0;
  while (i < 5) {
    cout << i << "\n";
    i++; //Increments the variable by 1
  }

  cout << "\n";
  int x = 0;
  do {
    cout << x << "\n";
    x++;
  }
  while (x < 5);

  cout << "\n";
  for (int j = 0; j<10;j++) {
    cout << j << endl;
    if (j==4){
        break;
    }
  }
}