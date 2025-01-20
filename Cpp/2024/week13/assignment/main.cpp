/**
 * Name: main.cpp
 * Author: Mikhail Zubko
 * Date: 2024-11-16
 * Purpose: Converter
 */

// Imports
#include "converter.h" // to parse int from string
#include <iomanip>     // for set precision
#include <iostream>
#include <string>

int main() {
  std::string input;
  double fahrenheit;
  double celsius;
  while (true) {
    std::cout << "Enter Fahrenheit temperature: ";
    getline(std::cin, input);
    try {
      fahrenheit = std::stof(input);
      break;
    } catch (...) {
      std::cout << "Enter a float number" << std::endl;
    }
  }
  celsius = converter(fahrenheit);
  std::cout << fahrenheit << "°F = " << std::setprecision(4) << celsius << "°C"
            << std::endl;
}
