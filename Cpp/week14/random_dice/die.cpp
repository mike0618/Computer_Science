#include "die.h"
#include <stdlib.h>

Die::Die() {}
void Die::rollDie() { value = (rand() % 6) + 1; }
int Die::getValue() { return value; }
