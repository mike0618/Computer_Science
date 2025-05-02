#ifndef COLLATZ_H
#define COLLATZ_H
#include <vector>

// define a class
class Collatz {
public:
  // constructor
  Collatz();
  std::vector<int> get_lst(int num);
  int get_len(long num);
};
#endif
