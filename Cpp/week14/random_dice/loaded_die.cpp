#include "ldie.h"
#include <stdlib.h>
LoadedDie::LoadedDie() : Die() {}
void LoadedDie::rollDie() { value = (rand() % 5) + 2; }
int LoadedDie::getValue() { return value; }
