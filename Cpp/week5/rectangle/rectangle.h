#ifndef RECTANGLE_H
#define RECTANGLE_H

// define a class
class Rectangle {
private:
  double m_width;
  double m_len;
  double m_area;

public:
  // constructor
  Rectangle(double width, double len);
  double get_perimeter();
  double get_area();
};
#endif
