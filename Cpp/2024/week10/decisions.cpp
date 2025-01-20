// Written by: Mikhail Zubko
// Date: 2024-10-24
// Description: decisions practice
#include <iostream>
using namespace std;
int main() {
  // TODO: Declare constants and variables for input and output
  const int THOUSAND_GALLONS = 1000;
  const int FIVE_HUNDRED_GALLONS = 500;
  int fuel_level{0}; // init variable with value
  double width;
  double area;
  double perimeter;
  // TODO: Print nice program title
  cout << "+-------------------------------+" << endl;
  cout << "+ --- Space Ship Fuel Level --- +" << endl;
  cout << "+-------------------------------+" << endl;
  // TODO: Get user input for fuel level
  cout << "What is your fuel level: ";
  cin >> fuel_level;
  // TODO: Comparisons
  if (fuel_level > THOUSAND_GALLONS) {

    cout << "We have enough fuel, We're homeward bound!" << endl;
  } else if (fuel_level > FIVE_HUNDRED_GALLONS) {

    cout << "We have to stop for fuel!" << endl;
  } else {

    cout << "We don't have enough fuel, head for the escape pods!" << endl;
  }
  return 0;
}
