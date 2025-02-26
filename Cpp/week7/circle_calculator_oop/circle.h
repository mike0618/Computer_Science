#ifndef CIRCLE_H
#define CIRCLE_H

// define a class
class Circle {
private:
  double m_radius;
  double m_diameter;
  double m_area;
  double m_cird;

public:
  // constructor
  Circle();
  void set_radius(double radius);
  double get_diameter();
  double get_area();
  double get_circ();
};
#endif
