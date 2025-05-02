#include "die.h"
#include "ldie.h"
#include "time.h"
#include <cstdlib>
#include <iostream>

int main() {
  srand(time(0));
  int cnt{0};
  int lcnt{0};
  Die die1;
  Die die2;
  LoadedDie ldie;
  for (int i = 0; i < 1000; i++) {
    die1.rollDie();
    die2.rollDie();
    ldie.rollDie();
    if (die1.getValue() > die2.getValue()) {
      cnt++;
    }
    if (ldie.getValue() > die2.getValue()) {
      lcnt++;
    }
  }
  std::cout << "With two regular die, the first die won: " << cnt
            << " out of 1000" << std::endl;
  std::cout << "With one loaded die, the loaded die won: " << lcnt
            << " out of 1000" << std::endl;

  return 0;
}
