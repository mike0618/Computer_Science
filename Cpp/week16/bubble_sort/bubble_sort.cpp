#include <algorithm> // to use swap
#include <cstdlib>   // for random
#include <ctime>     // to seed random
#include <iostream>
#include <vector>

int main() {
  srand(time(0)); // seed for rand

  std::vector<int> lst(99);  // create a vector for 99 ints
  for (int &num : lst) {     // stuff lst with rand nums using reference
    num = std::rand() % 100; // gen rand numbers from 0 to 99
  }
  int len = lst.size() - 1;
  std::cout << "C++ Bubble Sort" << std::endl;
  std::cout << std::endl;
  for (int num : lst) { // print lst
    std::cout << num << " ";
  }
  std::cout << std::endl;
  bool swap = true;
  while (swap) {
    swap = false;
    for (size_t i = 0; i < len; i++) {
      if (lst[i] > lst[i + 1]) {
        swap = true;
        std::swap(lst[i], lst[i + 1]);
      }
    }
  }
  std::cout << std::endl;
  for (int num : lst) {
    std::cout << num << " ";
  }
  std::cout << std::endl;
  return 0;
}
