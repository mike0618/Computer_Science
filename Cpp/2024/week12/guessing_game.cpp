// Written by: Mikhail Zubko
// Date: 2024-11-09
// Description: Guessing game

#include <cctype>  // to compare chars
#include <cstdlib> //rand srand functionsa
#include <ctime>
#include <iostream>
#include <limits>
using namespace std;

int main() {
  srand(time(0));
  int random_number;
  string guess_str;
  int guess;
  int count;
  char answer;
  while (true) {
    count = 1;
    random_number = (rand() % 10) + 1;
    cout << "+---------------------------+" << endl;
    cout << "+ --- C++ Guessing Game --- +" << endl;
    cout << "+---------------------------+" << endl;
    while (true) {
      cout << "Enter your guess between 1 and 10: ";
      cin >> guess;
      if (guess == random_number) {
        cout << "Congratulations!" << endl;
        cout << "You guessed the number in " << count << " guesses!" << endl;
        cout << "Thanks for playing!" << endl;
        break;
      } else if (guess > 0 && guess < random_number) {
        cout << "Your guess is too low!" << endl;
      } else if (guess < 11 && guess > random_number) {
        cout << "Your guess is too high!" << endl;
      } else {
        cin.clear(); // clear the error after wrong input
        // discard remaining input (I googled it.)
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        cout << "That was a wasted guess." << endl;
        cout << "Pick a number between 1 and 10 inclusive!" << endl;
      }
      count++;
    }
    cout << "Do you wish to play again? (y/n): " << endl;
    cin >> answer;
    if (tolower(answer) != "y"[0]) {
      break;
    }
  }
  return 0;
}
