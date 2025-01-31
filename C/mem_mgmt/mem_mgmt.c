#include <stdio.h>
#include <stdlib.h> // for dynamic memory allocation, malloc, calloc

int main() {
  int myInt;
  float myFloat;
  double myDouble;
  char myChar;

  printf("Integer: %lu\n", sizeof(myInt));   // 4 bytes
  printf("Float: %lu\n", sizeof(myFloat));   // 4 bytes
  printf("Double: %lu\n", sizeof(myDouble)); // 8 bytes
  printf("Char: %lu\n", sizeof(myChar));     // 1 bytes
  //
  // Allocation
  //
  // Static memory (compile time memory)
  // reserved for vars before the program runs.
  int students[20];
  printf("Students 20 ints: %lu bytes\n", sizeof(students)); // 80 bytes
  // if this array used only for 12 students, 8 unused elements wasted.
  //
  // Dynamic Memory (runtime memory)
  // allocated after the program starts running.
  int *ptr1 = malloc(10);    // size, may be unexpectable, write before reading!
  int *ptr2 = calloc(4, 12); // writes 0's into memory, slightly less efficient
  // The best way to allocate the right amount of memory:
  int *ptr3, *ptr4;
  ptr3 = malloc(sizeof(*ptr3));
  ptr4 = calloc(1, sizeof(*ptr4));
  // improve the students example above
  int *students2;
  int numStudents = 12;
  students2 = calloc(numStudents, sizeof(*students2));
  printf("12 int Students: %lu bytes\n", numStudents * sizeof(*students)); // 48
  //
  // Check for errors and free memoty at the end of the program!
  // Stack memory - Dynamic mem for vars inside functions.
  // Recursion can couse stack overflow!

  return 0;
}
