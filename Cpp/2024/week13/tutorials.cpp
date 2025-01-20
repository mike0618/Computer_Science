/**
 * Name: tutorials.cpp
 * Author: Mikhail Zubko
 * Date: 2024-11-16
 * Purpose: C++ functions practice
 */

// Imports
#include "my_function.h" // to parse int from string
#include <cmath>
#include <cstdio>
#include <iomanip>  // for set precision
#include <iostream> // for sqrt math method
#include <string>   // to parse int from string

///// Function prototypes
void message();
void findSquareRoot(double num);
void multiply(double num1, double num2, std::string message);
double getCeil(double num);
int getResult(int num = 24);
int getResult(int num1, int num2);
int getResult(int num, std::string value);
std::string getResult(std::string str1, std::string str2);
double getDouble(std::string prompt);
void countDownFrom(int num);
void countUpTo(int from, int to);
void aFunction(int &num1, int &num2); // take two int references
void greeting(std::string greet, int repeats = 1);

int main() {
  std::cout << "Tutorial 5.1: Void Function" << std::endl;
  std::cout << "\nFirst function call" << std::endl;
  // Function call
  message();
  std::cout << "\nSecond function call" << std::endl;
  // Function call
  message();
  std::cout << "\nThird function call" << std::endl;
  // Function call
  message();

  std::cout << "\nTutorial 5.2: Function with a Single Parameter\n"
            << std::endl;
  // Initialize variables
  double num1{4};
  double num2{8.9};
  double num3{112};
  double num4{313.2};
  // Function calls with 1 double argument
  findSquareRoot(num1);
  findSquareRoot(num2);
  findSquareRoot(num3);

  std::cout << "\nTutorial 5.3: Function with Multiple Parameters\n"
            << std::endl;
  std::string message = "\nFirst function call";
  multiply(num1, num2, message);
  message = "\nSecond function call";
  multiply(num3, num4, message);

  std::cout << "\nTutorial 5.4: Function with Return Value\n" << std::endl;
  double numCeil;
  std::cout << "Print the function directly" << std::endl;
  std::cout << num2 << " -> " << getCeil(num2) << std::endl;
  std::cout << "Assign return value to variable" << std::endl;
  numCeil = getCeil(num4);
  std::cout << num4 << " -> " << numCeil << std::endl;

  std::cout << "\nTutorial 5.5: Function Overloading\n" << std::endl;
  // Call a method with a single int argument
  int result = getResult(5);
  std::cout << result << std::endl;
  // Call a method with no arguments, use the default parameter
  result = getResult();
  std::cout << result << std::endl;
  // Call a method with two int args
  result = getResult(5, 4);
  std::cout << result << std::endl;
  // Call a method with an int and a string argument
  result = getResult(5, "13");
  std::cout << result << std::endl;
  // Call a method with two string args
  std::cout << getResult("Billy", "Idol") << std::endl;

  std::cout << "\nTutorial 5.6: Input Function Try-Catch\n" << std::endl;
  double number;
  number = getDouble("Enter number: ");
  std::cout << "Number: " << number << std::endl;

  std::cout << "\nTutorial 5.7: Recursion\n" << std::endl;
  std::cout << "Countdown" << std::endl;
  countDownFrom(10);
  std::cout << std::endl;
  std::cout << "Countup" << std::endl;
  countUpTo(0, 10);
  std::cout << std::endl;

  std::cout << "\nTutorial 5.8: Pass by Reference\n" << std::endl;
  int num5{5};
  int num6{8};
  // call the aFunction, pass num5 and num6 by reference
  aFunction(num5, num6);
  std::cout << num5 << ", " << num6 << std::endl;

  std::cout << "\nTutorial 5.9: Default Arguments\n" << std::endl;
  greeting("Hello", 3);
  greeting("Good morning"); // use the default argument
  greeting("Hola, amigo!", 5);
  std::cout << "\nTutorial 5.10: Headers and Multiple files\n" << std::endl;
  myFunction(); // defined in my_function.cpp

  return 0;
}

///// Function definitions
void message() {
  // Split a long string across multiple lines for readability
  std::cout << "I love deadlines.\n"
            << "I like the whooshing sound they make as they fly by."
            << std::endl;
  std::cout << "Douglas Adams" << std::endl;
}
void findSquareRoot(double num) {
  double squareRoot;
  squareRoot = sqrt(num);
  std::cout << std::setprecision(15) << "The square root of " << num
            << " is: " << squareRoot << std::endl;
}
void multiply(double num1, double num2, std::string message) {
  double product;
  product = num1 * num2;
  std::cout << message << std::endl;
  std::cout << "The product of " << num1 << " * " << num2 << " is: " << product
            << std::endl;
}
double getCeil(double num) {
  double numCeil;
  // cmath.ceil() method rounds a floating poing
  // up to the nearest integer value
  numCeil = ceil(num);
  return numCeil;
}
int getResult(int num) { return num * 2; }
int getResult(int num1, int num2) { return num1 * num2; }
int getResult(int num, std::string value) {
  // std::stoi is a string library function
  // that parses an integer from a string
  return num * std::stoi(value);
}
std::string getResult(std::string str1, std::string str2) {
  return str1 + " " + str2;
}
double getDouble(std::string prompt) {
  std::string line_input;
  double double_value{0};
  std::cout << prompt;
  // get the input line into a string
  getline(std::cin, line_input);
  // try-catch if any exceptions
  try {
    // convert str to double_value
    double_value = std::stod(line_input);
    return double_value;
  } catch (...) {
    // returse the return method until the user enters a number
    return getDouble("Enter a number: ");
  }
}
void countDownFrom(int num) {
  if (num >= 0) {
    std::cout << num << " ";
    // recursive call to itself
    countDownFrom(num - 1);
  }
}
void countUpTo(int from, int to) {
  if (from <= to) {
    std::cout << from << " ";
    // recursive call to itself
    countUpTo(from + 1, to);
  }
}
void aFunction(int &num1, int &num2) {
  // parameters are passed by references,
  // the original variables will be modified
  num1 = 2;
  num2 = 2;
}
void greeting(std::string greet, int repeats) {
  for (int i = 0; i < repeats; i++) {
    std::cout << greet << std::endl;
  }
}
