// Written by: Mikhail Zubko
// Date: 2024-10-24
// Description: decisions practice
#include <cctype>
#include <cstdio>  // for printf
#include <cstdlib> //rand srand functionsa
#include <ctime>
#include <iostream>
using namespace std;
int main() {
  srand(time(0)); // init random number generator with different values
  // TODO: declare constants and variables
  const int CURRENT = 2024;
  int year;
  int random_number;
  char answer;
  // TODO: print nice program title
  cout << "+----------------------------+" << endl;
  cout << "+ --- TARDIS Time Travel --- +" << endl;
  cout << "+----------------------------+" << endl;
  cout << "Welcom to time travel with the Doctor!" << endl;
  printf("You are currently in the year %u.\n", CURRENT);
  while (true) { // game loop
    // TODO: get user input for a year
    cout << "Enter a year to travel to: ";
    cin >> year;
    // TODO: year comparisons
    if (year == CURRENT) {
      printf("You traveled in the same year: %u.\n", year);
    } else if (year < CURRENT) {
      printf("You traveled back in time to %u!\n", year);
    } else {
      printf("You traveled forward in time to %u!\n", year);
    }
    // TODO: generate random number
    random_number = (rand() % 10) + 1;
    // TODO: random number comparisons
    if (random_number == 1) {
      cout << "You are stuck until you are rescued." << endl;
      break;
    } else if (random_number < 5) {
      printf("You found a valuable artifact in %u!\n", year);
    } else {
      printf("You couldnt't find any artifacts in %u\n", year);
    }
    cout << "Try again? (y/N): ";
    cin >> answer;
    if (tolower(answer) != "y"[0]) {
      break;
    }
  }
  return 0;
}
