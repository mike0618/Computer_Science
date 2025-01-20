// Written by: Mikhail Zubko
// Date: 2024-11-02
// Description: Generate a series of random numbers

#include <cstdlib> //rand srand functionsa
#include <ctime>
#include <iostream>
using namespace std;

int main() {
  // the rand() function generates the same sequence
  // each time the program runs
  // srand() initializes the random number generator with different values
  // time(0) is the time since January 1st, 1970 at 00:00:00 AM
  srand(time(0));
  int rand_num;
  int random_number;
  for (int count = 1; count <= 10; ++count) {
    // rand() returns a pseudorandom int in range 0 to RAND_MAX
    rand_num = rand();
    // rand() % 10 generates a random number between 0 and 9
    // + 1 brings it to 1 through 10 inclusive
    random_number = (rand() % 10) + 1;
    // cout << rand_num << " ";
    cout << random_number << endl;
  }
  return 0;
}
