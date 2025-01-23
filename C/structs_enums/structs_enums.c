#include <stdio.h>
#include <string.h>

// Struct - a way to group several different but related variables into one
// place declare a struct
struct MyStruct {
  int myNum;
  char myLetter;
  char myString[30];
}; // must end with a semicolon

struct Car {
  char brand[50];
  char model[50];
  int year;
};

// Enum - special type that represents a group of constants
enum Level {
  LOW,    // default = 0
  MEDIUM, // 1
  HIGH,   // 2
};
enum Level2 {
  LOW2 = 2,
  MEDIUM2, // 3
  HIGH2,   // 4
};
enum Level3 {
  LOW3 = 25,
  MEDIUM3 = 50,
  HIGH3 = 75,
};

int main() {
  struct MyStruct s1; // create a struct variable
  struct MyStruct s2; // create a struct variable
  // assign values to members of s1
  s1.myNum = 13;
  s1.myLetter = 'M';
  // assign a value to the string using strcpy()
  strcpy(s1.myString, "Some text");
  // print value
  printf("My number: %d\n", s1.myNum);
  printf("My letter: %c\n", s1.myLetter);
  printf("My string: %s\n", s1.myString);
  // Simplier syntax to assign values at a declaration time
  struct MyStruct s3 = {34, 'B', "Text here"};
  printf("%d %c %s\n", s3.myNum, s3.myLetter, s3.myString);
  // Copy structs
  s2 = s1;
  // change s2 values
  s2.myNum = 0;
  s2.myLetter = 'U';
  strcpy(s2.myString, "Someting else");
  printf("%d %c %s\n", s1.myNum, s1.myLetter, s1.myString); // still the same
  printf("%d %c %s\n", s2.myNum, s2.myLetter, s2.myString);

  // Example
  struct Car car1 = {"BMW", "X5", 1999};
  struct Car car2 = {"Ford", "Mustang", 1969};
  struct Car car3 = {"Toyota", "Corolla", 2011};

  printf("%s %s %d\n", car1.brand, car1.model, car1.year);
  printf("%s %s %d\n", car2.brand, car2.model, car2.year);
  printf("%s %s %d\n", car3.brand, car3.model, car3.year);

  // Create enum variable
  enum Level myVar; // assigned value must be LOW, MEDIUM or HIGH
  // by default the first item (LOW) has the value 0, the secont - 1, etc.
  printf("%d\n", myVar);
  // enum in a switch
  myVar = MEDIUM;
  switch (myVar) {
  case 0:
    printf("Low Level");
    break;
  case 1:
    printf("Medium Level");
    break;
  case 2:
    printf("High Level");
    break;
  }
  printf("\n");

  return 0;
}
