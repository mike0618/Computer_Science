#include <stdio.h> // work with input/output functions like printf()

int main() {
  printf("Hello, World!\n");
  int myNum = 42; // variable (type name = value) name - unique identifier
  float myFloat = 8.8;
  char myChar = 'M';     // char is in single quotes
  printf("%d\n", myNum); // %d format specifier to output int
  // %s for string, %c for char, %f for float, %lf for double
  printf("%f\n", 5.5);
  printf("%f\n", myFloat);
  printf("%c\n", myChar);
  printf("My favorite number is: %d\n", myNum);
  printf("My float number is %f, my letter is %c\n", myFloat, myChar);
  // Declare multiple variables
  int x = 8, y = 13, z = 21;
  printf("The answer is: %d\n", x + y + z);

  // Real-life example: Area of a Rectangle
  int len = 7;
  int wid = 6;
  int area;
  area = len * wid; // calculation
  printf("Length is: %d\n", len);
  printf("Width is: %d\n", wid);
  printf("Area is: %d\n", area);

  // int - 2 or 4 bytes;
  // float - 4 bytes, 6-7 digits;
  // double - 8 bytes, 15 digits;
  // char - 1 byte
  //
  // ASCII chars
  char a = 65, b = 66, c = 67;
  printf("%c", a);
  printf("%c", b);
  printf("%c\n", c);
  // do not store multiple characters in a char.
  //
  // scientific float notation
  float f1 = 35e3;
  double d1 = 12E4;
  printf("%f\n", f1);
  printf("%lf\n", d1);
  printf("%.2lf\n", d1); // only show 2 digits
  //
  // sizeof operator
  printf("%lu\n", sizeof(myNum)); // %lu sizeof returns a long unlisted int
  printf("%lu\n", sizeof(myFloat));
  printf("%lu\n", sizeof(d1));
  printf("%lu\n", sizeof(myChar));

  // Real-life example
  int items = 50;
  float item_cost = 9.99;
  float total_cost = items * item_cost;
  char currency = '$';
  printf("Items: %d\n", items);
  printf("Cost per item: %c%.2f\n", currency, item_cost);
  printf("Total cost: %c%.2f\n", currency, total_cost);

  // Type Conversion
  // Implicit
  float f2 = 9;  // int to float
  int i2 = 9.99; // float to int
  printf("int to float: %f\n", f2);
  printf("float to int: %d\n", i2);
  // Manual
  float sum = (float)5 / 2;   // int to float
  float sum2 = (float)f2 / 2; // type in front of a var
  printf("Manual int to float: %f\n", sum);
  printf("Manual int to float: %.1f\n", sum2);

  // Constants, always declare it whan the var is unlikely to change
  const int MYNUM = 15; // will always be 15, must be assigned
//
// Operators
// Arithmetic: +, -, *, /, %, ++, --
// Assignment: =, +=, -=, *=, /=, %=, &=, |=, ^=, >>=, <<=
// Comparison: ==, !=, <, >, <=, >=
// Logical: && - and, || - or, ! - not
//
// Boolean
#include <stdbool.h>
  bool isProgrammingFun = true;
  bool isFishTasty = false;
  printf("Use int format to print bool: %d\n", isProgrammingFun);
  printf("Use int format to print bool: %d\n", isFishTasty);

  // Conditions, else, if, switch
  int time = 22;
  if (time < 10) {
    printf("Good morning.");
  } else if (time < 20) {
    printf("Good day.");
  } else {
    printf("Good evening.");
  }
  // Ternary Operator
  (time < 18) ? printf("Good day.") : printf("Good evening.");
  // Switch
  int day = 4;
  switch (day) {
  case 1:
    printf("Monday");
    break;
  case 2:
    printf("Tuesday");
    break;
  case 3:
    printf("Wednesday");
    break;
  case 4:
    printf("Thursday");
    break;
  case 5:
    printf("Friday");
    break;
  case 6:
    printf("Saturday");
    break;
  case 7:
    printf("Sunday");
    break;
  default:
    printf("Looking forward to the Weekend");
  }
  printf("\n");

  // While Loop
  int i = 0;
  while (i < 5) {
    printf("%d\n", i);
    i++;
  }
  // Do/While Loop - always executes at least once before checking the condition
  do {
    printf("%d\n", i);
    i += 2;
  } while (i < 10);
  // Example
  int numbers = 12345;
  int revNumbers = 0; // to store reversed numbers
  while (numbers) {
    revNumbers = revNumbers * 10 + numbers % 10;
    numbers /= 10;
  }
  printf("Reversed numbers: %d\n", revNumbers);

  // For Loop
  for (int i = 2; i <= 512; i *= 2) {
    printf("%d\n", i);
  }
  // break; to jump out of a loop
  // continue: to break one iteration
  //
  // Array - store multiple values in a single variable. type name[] = {values}
  // Cannot mix different types of values
  // The size of array is not changable
  int myNumbers[] = {2, 3, 5, 8};
  // Declare an array before adding elements
  int myNumbers2[4]; // size must be defined
  myNumbers2[0] = 25;
  myNumbers2[1] = 50;
  myNumbers2[2] = 75;
  myNumbers2[3] = 100;
  // Loop through array
  for (int i = 0; i < 4; i++) {
    myNumbers2[i] /= 5;            // change elements
    printf("%d\n", myNumbers2[i]); // access to elements
  }
  // Better loop using sizeof
  // calc length in elemnts
  int length = sizeof(myNumbers) / sizeof(myNumbers[0]);
  float avg, summ = 0;
  for (int i = 0; i < length; i++) {
    summ += myNumbers[i];
    printf("%d\n", myNumbers[i]);
  }
  // calc average
  avg = summ / length;
  printf("Average = %.2f\n", avg);

  // Multidimentional Array
  int matrix[2][3] = {{1, 4, 2}, {3, 6, 8}};
  for (int i = 0; i < 2; i++) {
    for (int j = 0; j < 3; j++) {
      printf("%d\n", matrix[i][j]);
    }
  }

  // String - an array of characters
  char greetings[] = "Hello, World!";
  printf("%s\n", greetings);
  printf("%c\n", greetings[0]);
  // Modify strings
  greetings[0] = 'J'; // must be a char
  printf("%s\n", greetings);
  // Another method
  char greetings2[] = {'H', 'e', 'l', 'l', 'o', ',', ' ',
                       'W', 'o', 'r', 'l', 'd', '!', '\0'};
  // \0 - null termitationg character, must be included in this way.
  printf("%lu\n", sizeof(greetings));
  printf("%lu\n", sizeof(greetings2));
  // \ - escape character
  char txt[] = "It\'s alright.";
  printf("%s\n", txt);

// String Functions
#include <string.h>
  char letters[] = "abcde";
  printf("Strlen: %lu\n", strlen(letters));
  printf("Sizeof: %lu\n", sizeof(letters)); // 5 chars + 1 null char
  char letters2[50] = "abcde";
  printf("Strlen2: %lu\n", strlen(letters2));
  printf("Sizeof2: %lu\n", sizeof(letters2)); // 50 - memory size
  // Concatenate strings
  printf("%s\n", strcat(letters2, letters));
  printf("%s\n", letters2); // result is stored in letters2 also!!!
  // letters2 should be large enough
  // Copy Strings
  char str2[50];
  // copy letters2 to str2
  strcpy(str2, letters2); // str2 should be large enough
  printf("%s\n", str2);
  // Compare Strings
  printf("%d\n", strcmp(str2, letters2)); // returns 0, the strings are equal
  printf("%d\n", strcmp(str2, letters));

  // User Input
  int userNum;
  printf("Type a number: ");
  scanf("%d", &userNum);
  printf("Your number is: %d\n", userNum);
  // Multiple inputs
  char userChar;
  printf("Type a number and a character and press enter: ");
  scanf("%d %c", &userNum, &userChar);
  printf("Your number is: %d\n", userNum);
  printf("Your character is: %c\n", userChar);
  // Line of text
  char fullName[30];
  printf("Type your full name: ");
  scanf(" %29[^\n]", fullName); // parse any 29 sybols but not \n
  // skip leading^ whitespace
  printf("Hello %s\n", fullName);
  getchar(); // consume the leftover \n after scanf()
  // Line of text input fgets()
  printf("Type your full name: ");
  fgets(fullName, sizeof(fullName), stdin);
  printf("Hello from fgets %s", fullName);

  // Pointers - Memory Address
  int myAge = 39;
  printf("%d\n", myAge);
  printf("%p\n", &myAge); // & - reference operator to access the memory address
  // &myAge is a pointer, %p is a format specifier for pointers
  int *ptr = &myAge; // a pointer variable
  printf("%p\n", ptr);
  printf("%d\n", *ptr); // dereference, output the value
  //
  // Pointers & Arrays.
  // The name of an array is a Pointer to the first element of the array.
  printf("%p\n", myNumbers);        // myNumbers is a array-pointer, no need &
  printf("%p\n", &myNumbers[0]);    // mem address of the first array element
  printf("%d\n", *myNumbers);       // dereference to get the first element
  printf("%d\n", *(myNumbers + 1)); // the second element
  printf("%d\n", *(myNumbers + 2)); // the third element, and so on...
  *(myNumbers + 1) = 13;            // change value using pointer
  printf("Changed: %d\n", *(myNumbers + 1));
  // Loop using Pointers
  int *numptr = myNumbers;
  for (i = 0; i < sizeof(myNumbers) / sizeof(myNumbers[0]); i++) {
    printf("%d\n", *(numptr + i));
  }
  // Pointers are more efficient, and also useful for 2-dimensional arrays,
  // strings and files
  //
  //
  return 0;
}
