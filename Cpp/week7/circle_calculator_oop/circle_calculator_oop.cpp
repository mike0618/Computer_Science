#include "circle.h"
#include <ios>
#include <iostream>
#include <limits>
int main() {
  std::cout << "\n -- circle Calculator Multiple Files --\n" << std::endl;
  while (true) {
    double raduis;
    char answer;
    // create an object
    Circle circle1;
    std::cout << " Enter radius: ";
    std::cin >> raduis;
    // the best practice that I found to clear the buffer after the wrong input
    if (std::cin.fail()) {
      std::cin.clear(); // clear the error flag
      // discard invalid input
      std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
      std::cout << " Wrong input." << std::endl;
    } else {
      circle1.set_radius(raduis);
      // disp values
      printf("     Diameter: %'.2f\n", circle1.get_diameter());
      printf("         Area: %'.2f\n", circle1.get_area());
      printf("Circumference: %'.2f\n", circle1.get_circ());
    }
    std::cout << std::endl;
    std::cout << "Do you want to calculate another circle? y/n: ";
    std::cin >> answer;
    if (answer != 'y') {
      break;
    }
  }
  return 0;
}
