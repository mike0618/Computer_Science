#ifndef LDIE_H
#define LDIE_H
#include "die.h"
class LoadedDie : public Die {
public:
  // constructor
  LoadedDie();
  // setter method
  void rollDie();
  // getter method
  int getValue();
};

#endif
