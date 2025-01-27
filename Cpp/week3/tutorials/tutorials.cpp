#include <iostream>

// Define a struct
struct Person {
  std::string name;
  int age;
  std::string city;
};

int main() {
  // Create and instance of the struct
  Person person1;

  // assign values
  person1.name = "Mike";
  person1.age = 39;
  person1.name = "Scottsbluff";

  // Create struct and with values
  Person person2{"Bob", 28, "Los Angeles"};

  // Avccess and print the struct's values
  std::cout << "Name: " << person1.name << std::endl;
  std::cout << "Age: " << person1.age << std::endl;
  std::cout << "City: " << person1.city << std::endl;

  std::cout << "Name: " << person2.name << std::endl;
  std::cout << "Age: " << person2.age << std::endl;
  std::cout << "City: " << person2.city << std::endl;

  return 0;
}
