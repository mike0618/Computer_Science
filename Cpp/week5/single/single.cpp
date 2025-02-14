#include <cstdlib>
#include <iostream>
// define a class
class Rectangle {
private:
  double m_width;
  double m_len;
  double m_area;

public:
  // constructor
  Rectangle(double width, double len) {
    this->m_width = width;
    this->m_len = len;
  }
  double get_perimeter() { return this->m_width * 2 + this->m_len * 2; }
  double get_area() { return this->m_width * this->m_len; }
};
int main() {
  double width{2.5};
  double len{7.0};
  std::cout << "\n -- Rectangle Calculator Single File --\n" << std::endl;
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
