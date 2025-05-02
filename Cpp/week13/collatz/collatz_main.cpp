#include "collatz.h"
#include <iostream>
#include <limits>
#include <vector>

int get_input() {
  int num{0};
  std::cout << "Enter a whole number: ";
  std::cin >> num;
  // handle wrong input
  if (std::cin.fail()) {
    std::cin.clear(); // clear the error flag
    // discard invalid input
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cout << " Wrong input." << std::endl;
  }
  return num;
}

int main() {
  std::cout << "\n -- The Collatz chain for the entered number --\n"
            << std::endl;
  Collatz collatz;
  int num;
  int steps;
  char ans;
  std::vector<int> chain;
  while (true) {
    num = get_input();
    chain = collatz.get_lst(num);
    steps = chain.size();
    // print the chain
    for (int element : chain) {
      std::cout << element << " ";
    }
    std::cout << std::endl;
    std::cout << "Steps: " << steps << std::endl;
    std::cout << "Do you want to get another chain? y/n: ";
    std::cin >> ans;
    if (ans != 'y') {
      break;
    }
  }
  std::cout << "Let's try challenge!" << std::endl;
  std::cout << "Find the number below the entered producing the longest "
               "Collatz chain."
            << std::endl;
  num = get_input();
  int maxL{0};
  int maxN{0};
  for (int i = 1; i < num; i += 2) {
    int len = collatz.get_len(i);
    if (len > maxL) {
      maxL = len;
      maxN = i;
    }
  }
  std::cout << "The number " << maxN << " produces the longest chain of "
            << maxL << " steps." << std::endl;
}
