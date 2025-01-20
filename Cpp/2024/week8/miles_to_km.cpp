// Written by: Mikhail Zubko
// Date: 2024-10-09
// Description: Calculate wages per month

#include <iostream>
using namespace std;

int main() {
  // TODO: Declare conversion constant
  // 1 mile = 1.609344 kilometers
  const double COEF = 1.609344;
  // declare vars
  double miles;
  double km;
  // TODO: Print a creative title
  cout << "+-----------------------------------------+" << endl;
  cout << "+  ---  Convert Miles to Kilometers  ---  +" << endl;
  cout << "+-----------------------------------------+" << endl;
  // TODO: Get user input and save it to var
  cout << "Enter Miles: ";
  cin >> miles;
  // TODO: Convert Miles to Kilometers
  km = miles * COEF;
  // TODO: Print the result
  cout << miles << " miles: " << km << " km" << endl;
  return 0;
}
