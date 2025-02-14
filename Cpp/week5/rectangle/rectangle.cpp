#include "rectangle.h"

// implement the constructor and public methods
Rectangle::Rectangle(double width, double len) {
  this->m_width = width;
  this->m_len = len;
}

double Rectangle::get_perimeter() {
  return this->m_width * 2 + this->m_len * 2;
}

double Rectangle::get_area() { return this->m_width * this->m_len; }
