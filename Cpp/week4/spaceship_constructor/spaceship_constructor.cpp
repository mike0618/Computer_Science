#include <iostream>
// create a class
class Spaceship {
private: // members used only in the class
  double m_len;
  double m_wid;
  double m_hgt;

public: // program scope members
  // Default constructor
  Spaceship() {}; // created automatically if not defined
  // Parameterized constructor
  Spaceship(double len, double wid, double hgt) {
    m_len = len;
    m_wid = wid;
    m_hgt = hgt;
  };
  // method without parameters
  double calcArea() { return m_len * m_wid; }
  // overloaded method with parameters
  double calcArea(double len, double wid) { return len * wid; }
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
  // create an object of the class
  Spaceship spaceship1;
  // assign values
  spaceship1.insertData(42.5, 30.8, 19.2);
  // calculations
  area = spaceship1.calcArea();
  vol = spaceship1.calcVol(area);
  // disp results
  std::cout << "  Area of Spaceship: " << area << std::endl;
  std::cout << "  Area of Spaceship with parameters: "
            << spaceship1.calcArea(12, 12) << std::endl;
  std::cout << "Volume of Spaceship: " << vol << std::endl;
  // create an object using Parameterized constructor
  Spaceship spaceship2(98.3, 20.1, 15.7);
  area = spaceship2.calcArea();
  vol = spaceship2.calcVol(area);
  std::cout << "\n  Area of Spaceship2: " << area << std::endl;
  std::cout << "Volume of Spaceship2: " << vol << std::endl;
  return 0;
}
