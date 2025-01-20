/**
 * Name: tutorials.cpp
 * Author: Mikhail Zubko
 * Date: 2024-11-16
 * Purpose: C++ functions practice
 */

// Imports
#include <climits>
#include <cstdio>
#include <iomanip>
#include <iostream>

// Prototypes
void int_overflow();
void int_overflow_mitigation();
void buffer_overflow();
void buffer_overflow_mitigation();

int main() {
  std::cout << "C++ Integer Overflow\n" << std::endl;
  int_overflow();
  std::cout << std::endl;
  std::cout << "C++ Integer Overflow Mitigation\n" << std::endl;
  int_overflow_mitigation();
  std::cout << std::endl;
  std::cout << "C++ Buffer Overflow\n" << std::endl;
  // buffer_overflow();
  std::cout << "Don't run, it is unsafe!" << std::endl;
  std::cout << std::endl;
  std::cout << "C++ Buffer Overflow Mitigation\n" << std::endl;
  buffer_overflow_mitigation();

  return 0;
}

// Definitions
void int_overflow() {
  // maximum value for C++ int: 2147483647
  // maximum value for C++ int: -2147483648
  int maxInt = INT_MAX;
  int minInt = INT_MIN;

  std::cout << "Maximum value for C++ int: " << maxInt << std::endl;
  std::cout << "Minimum value for C++ int: " << minInt << std::endl;

  // Overflow maximum integer value
  std::cout << "Overflow by 1: " << ++maxInt << std::endl;
}
void int_overflow_mitigation() {
  int a = INT_MAX;
  std::cout << "Initial value: " << a << std::endl;
  // Check for potential overflow
  if (a < INT_MAX) {
    // Perform operation only if overflow won't accur
    std::cout << "Value after operation: " << ++a << std::endl;
  } else {
    std::cout << "Overflow avoided!" << std::endl;
  }
}
void buffer_overflow() {
  // Character buffer to store name
  char buffer[5];
  std::cout << "What is your name?: ";
  std::cin >> buffer;
  std::cout << buffer << std::endl;
}
void buffer_overflow_mitigation() {
  // Increased buffer size
  char buffer[20];
  std::cout << "What is your name?: ";
  // Limit input length
  std::cin >> std::setw(20) >> buffer;
  std::cout << "Hello, " << buffer << "!" << std::endl;
}
