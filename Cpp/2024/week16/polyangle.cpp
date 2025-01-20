/**
 * Name: polyangle.cpp
 * Author: Mikhail Zubko
 * Date: 2024-12-08
 * Purpose: C++ Polygone calculation
 */

#include <cmath>
#include <iostream>
#include <string>

class PolyAngle { // this is a class
public:
  int n;
  double len;
  std::string name;
  double perimeter;
  double intAngle;
  double extAngle;
  double inrad;
  double cirad;
  double area;
  std::string names[8] = {
      "Triangle", "Square",  "Pentagon", "Hexagon",
      "Heptagon", "Octagon", "Nonagon",  "Decagon",
  };
  void calculate() {
    if (n > 2 && n < 11) {
      this->name = this->names[n - 3];
    } else if (n > 2) {
      this->name = std::to_string(n) + "-sided polygon.";
    }
    this->perimeter = this->n * this->len;
    this->extAngle = 360.0 / this->n;
    this->intAngle = 180 - this->extAngle;
    this->inrad = std::tan(this->intAngle * M_PI / 360) * this->len / 2;
    this->cirad = this->inrad / cos(M_PI / this->n);
    this->area = this->inrad * this->perimeter / 2;
  }
};

int main() {
  PolyAngle pa; // create an object
  std::string input;
  std::string line = "+---------------------------------+";
  std::cout << line << std::endl;
  std::cout << "|         PolyAngle in C++        |" << std::endl;
  std::cout << line << std::endl;
  std::cout << "Enter the number of sides >> ";
  // get sides input as int
  while (true) {
    getline(std::cin, input);
    try {
      pa.n = std::stoi(input);
      if (pa.n < 3) {
        std::cout << "Enter a whole number > 2!" << std::endl;
        continue;
      }
      break;
    } catch (...) {
      std::cout << "Enter a whole number > 2!" << std::endl;
    }
  }
  std::cout << "Enter the length of the side >> ";
  // get length input as double
  while (true) {
    getline(std::cin, input);
    try {
      pa.len = std::stod(input);
      break;
    } catch (...) {
      std::cout << "Enter a number!" << std::endl;
    }
  }
  pa.calculate(); // run calculate method
  // print the outputs
  std::cout << "Polygon Name: " << pa.name << std::endl;
  std::cout << "Perimeter: " << pa.perimeter << std::endl;
  std::cout << "Interior Angle: " << pa.intAngle << "°" << std::endl;
  std::cout << "Exterior Angle: " << pa.extAngle << "°" << std::endl;
  std::cout << "Inradius: " << pa.inrad << std::endl;
  std::cout << "Circumradius: " << pa.cirad << std::endl;
  std::cout << "Area: " << pa.area << std::endl;
  return 0;
}
