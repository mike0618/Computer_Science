// Written by: Mikhail Zubko
// Date: 2024-10-09
// Description: Calculate Area and Perimeter of Rectangle

#include <iostream>
// Include for printf
#include <cstdio>
// Include for thousands separator
#include <locale.h>
using namespace std;

int main() {
  // TODO: Set the locale for thousands separator
  setlocale(LC_ALL, "");
  // TODO: Declare variables for input and output
  double length;
  double width;
  double area;
  double perimeter;
  // TODO: Print nice program title
  cout << "+------------------------------------------+" << endl;
  cout << "+  ---  Randy's Rectangle Calculator  ---  +" << endl;
  cout << "+------------------------------------------+" << endl;
  // TODO: Get user input for length and width as double
  cout << "Enter Length: ";
  cin >> length;
  cout << " Enter Width: ";
  cin >> width;
  // TODO: Calculate area of rectangle Math formula: a = lw
  area = width * length;
  // TODO: Calculate perimeter of rectangle Math formula: p = 2(l+w)
  perimeter = 2 * (width + length);
  // TODO: Echo user input
  printf(" You entered: length %g - width %g\n", length, width);
  // TODO: Display results
  // Use printf to format float to 2 decimal places
  // Use apostrophe ' to show comma , as a 1,000's separator
  cout << "+------------------------------------------+" << endl;
  printf("        Area: %'.2f\n", area);
  printf("   Perimeter: %'.2f\n", perimeter);
  return 0;
}
