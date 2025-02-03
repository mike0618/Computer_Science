#include <iostream>
#include <string>
class Cat {
private:
  std::string m_name;
  int m_age;
  double m_weight;

public:
  Cat(std::string name, int age, double weight) {
    m_name = name;
    m_age = age;
    m_weight = weight;
  };
  // getters
  std::string get_name() { return m_name; }
  int get_age() { return m_age; }
  double get_weight() { return m_weight; }
  // setters
  void set_age(int age) {
    if (age > m_age) {
      m_age = age;
    } else {
      std::cout << m_name << " cannot get younger." << std::endl;
    }
  }
  void set_weight(double weight) { m_weight = weight; }
  // methods
  void play() { std::cout << m_name << " is playing." << std::endl; }
  void eat() { std::cout << m_name << " is eating." << std::endl; }
  void meow() { std::cout << m_name << " says \"Meow!\"." << std::endl; }
};

int main() {
  Cat my_cat("Tom", 4, 6.2);
  std::cout << "My cat's name is: " << my_cat.get_name() << std::endl;
  std::cout << "My cat's age is: " << my_cat.get_age() << " years."
            << std::endl;
  std::cout << "My cat's weight is: " << my_cat.get_weight() << " pounds."
            << std::endl;
  my_cat.play();
  std::cout << "Trying to set younger age: " << std::endl;
  my_cat.set_age(3);
  my_cat.eat();
  std::cout << "Setting a new weight:" << std::endl;
  my_cat.set_weight(6.5);
  std::cout << "My cat's new weight is: " << my_cat.get_weight() << " pounds."
            << std::endl;
  my_cat.meow();

  return 0;
}
