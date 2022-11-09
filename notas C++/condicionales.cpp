//if Syntax
/*if (condition) {
  // block of code to be executed if the condition is true
}*/

//shortif Syntax
/*
int time = 20;
string result = (time < 18) ? "Good day." : "Good evening.";
cout << result;*/

//switch Syntax == switch is an id that evaluates 1 time (saves memory and time)
/*switch(expression) {
  case x:
    // code block
    break;
  case y:
    // code block
    break;
  default:
    // code block
}*/

#include <iostream>
using namespace std;

int main(void) {
  int time;
  cout << "Give me the time in hours (24 hour clock): ";
  cin >> time;
  if (time < 10) {
    cout << "Good morning.\n";
  } else if (time < 20) {
    cout << "Good day.\n";
  } else {
    cout << "Good evening.\n";
  }

  int day = 4;
  switch (day) {
    case 1:
        cout << "Monday";
        break;
    case 2:
        cout << "Tuesday";
        break;
    case 3:
        cout << "Wednesday";
        break;
    case 4:
        cout << "Thursday";
        break;
    case 5:
        cout << "Friday";
        break;
    case 6:
        cout << "Saturday";
        break;
    case 7:
        cout << "Sunday";
        break;
  }


}