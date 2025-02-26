#include "circle.h"
#include "math.h"
#include <cmath>

// implement the constructor and public methods
// Circle::Circle(double radius) { this->m_radius = radius; }
Circle::Circle() {}

void Circle::set_radius(double radius) { this->m_radius = radius; }

double Circle::get_diameter() { return this->m_radius * 2; }

double Circle::get_area() { return M_PI * this->m_radius * this->m_radius; }

double Circle::get_circ() { return 2 * M_PI * this->m_radius; }
