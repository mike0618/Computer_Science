#include "collatz.h"
#include <vector>

// implement the constructor and public methods
Collatz::Collatz() {}

std::vector<int> Collatz::get_lst(int num) {
  std::vector<int> collatz;
  while (num > 1) {
    if (num % 2 == 0) {
      num /= 2;
    } else {
      num = num * 3 + 1;
    }
    collatz.push_back(num);
  }
  return collatz;
}
int Collatz::get_len(long num) {
  int cnt{0};
  while (num > 1) {
    if (num % 2 == 0) {
      num /= 2;
    } else {
      num = num * 3 + 1;
    }
    cnt++;
  }
  return cnt;
}
