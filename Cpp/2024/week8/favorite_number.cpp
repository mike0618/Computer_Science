// Written by: Mikhail Zubko
// Date: 2024-10-09
// Description: Get name and a favorite number from user

#include <iostream>
using namespace std;

int main() {
  // declare var
  int fav_num;
  string name;
  // prompt the user for input
  cout << "\nHello, what is your name?: ";
  // get input from the kb
  cin >> name;
  // prompt the user for number
  cout << "\nEnter your favorite number between 1 and 100: ";
  // get input from the kb
  cin >> fav_num;
  // output to console, split long line of code
  cout << "Amazing " << name << "! " << fav_num
       << " is my favorite number too.\n";
  return 0;
}
