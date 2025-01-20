// Written by: Mikhail Zubko
// Date: 2024-11-09
// Description: loops practice

#include <iostream>
#include <string>
#ifdef _WIN32
#include <Window.h> // Windows header file for sleep
#else
#include <unistd.h> // Linux header file for sleep
#endif

int squares_cubes(std::string DASHES) {
  // define variables
  int square{0};
  int cube{0};
  // print heading
  std::cout << DASHES << std::endl;
  std::cout << "Number\tSquare\tCube" << std::endl;
  std::cout << DASHES << std::endl;
  // loop from 1 to 10
  for (int i{1}; i < 11; i++) {
    // calculate square and cube
    square = i * i;
    cube = i * i * i;
    std::cout << i << "\t" << square << "\t" << cube << std::endl;
  }
  std::cout << DASHES << std::endl;
  return 0;
}

int blast_off() {
  // a loop from 5 to 1
  for (int i{5}; i > 0; --i) {
    std::cout << i << std::endl;
    sleep(1); // pause for 1 second
  }
  std::cout << "Blast off!" << std::endl;
  return 0;
}

int running_total(std::string DASHES) {
  double total = 0;
  double number;
  std::cout << DASHES << std::endl;
  std::cout << "Sum the entered numbers" << std::endl;
  std::cout << DASHES << std::endl;
  while (true) {
    std::cout << "Enter a number (0 to quit): ";
    std::cin >> number;
    if (number == 0) {
      break;
    }
    total += number;
  }
  std::cout << "The total is: " << total << std::endl;
  return 0;
}

int input_validation() {
  std::string age_string;
  int age;
  while (true) {
    try {
      std::cout << "Enter your age: ";
      std::cin >> age_string;
      // cast to str to int, throw exception if non numeric
      age = std::stoi(age_string);
    } catch (...) {
      std::cout << "Please enter a whole number." << std::endl;
      continue;
    }
    if (age < 1) {
      std::cout << "Please enter a positive number." << std::endl;
      continue;
    }
    break;
  }
  std::cout << "Your age is: " << age << std::endl;
  return 0;
}

int nested_loops() {
  for (int i{0}; i < 3; i++) {
    std::cout << "--- Exterior loop " << i << " ---" << std::endl;
    std::cout << "--- Interior loop ---" << std::endl;
    for (int j{0}; j < 5; j++) {
      std::cout << j << "\t";
    }
    std::cout << "\n";
  }
  return 0;
}

int main() {
  const std::string DASHES = "------------------------";
  std::cout << "Tutorial 4.1: Squares and Cubes" << std::endl;
  squares_cubes(DASHES);
  std::cout << "\nTutorial 4.2: Blast off" << std::endl;
  blast_off();
  std::cout << "\nTutorial 4.3: Running total" << std::endl;
  running_total(DASHES);
  std::cout << "\nTutorial 4.4: Input validation. Try-Catch" << std::endl;
  input_validation();
  std::cout << "\nTutorial 4.5: Nested loops" << std::endl;
  nested_loops();
}
