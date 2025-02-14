#include "rectangle.h"
#include <iostream>
int main() {
  double width{2.5};
  double len{7.0};
  std::cout << "\n -- Rectangle Calculator Multiple Files --\n" << std::endl;
  // create an object
  Rectangle rectangle1(width, len);
  // disp values
  std::cout << "Perimeter: " << rectangle1.get_perimeter() << std::endl;
  std::cout << "Area: " << rectangle1.get_area() << std::endl;
  std::cout << std::endl;
  // pause until a key is pressed
  // system("PAUSE");
  std::cin.get(); // pause compatible with Linux
  return 0;
}
