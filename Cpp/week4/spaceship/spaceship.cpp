#include <iostream>
// create a class
class Spaceship {
private: // members used only in the class
  double m_len;
  double m_wid;
  double m_hgt;

public: // program scope members
  double calcArea() { return m_len * m_wid; }
  double calcVol(double area) { return area * m_hgt; }
  void insertData(double len, double wid, double hgt) {
    m_len = len;
    m_wid = wid;
    m_hgt = hgt;
  }
};

int main() {
  double area;
  double vol;
  // creage an object of the class
  Spaceship spaceship1;
  // assign values
  spaceship1.insertData(42.5, 30.8, 19.2);
  // calculations
  area = spaceship1.calcArea();
  vol = spaceship1.calcVol(area);
  // disp results
  std::cout << "  Area of Spaceship: " << area << std::endl;
  std::cout << "Volume of Spaceship: " << vol << std::endl;
  return 0;
}
