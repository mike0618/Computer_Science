#include <array>
#include <iostream>
#include <string>

int main() {
  std::string line = "**********************************";
  std::array<std::string, 4> services{
      "1. Oil change",
      "2. Tire rotation",
      "3. Battary check",
      "4. Brake inspection",
  };
  std::array<int, 4> prices{25, 22, 15, 5};
  int total = 0;
  while (true) {
    int choice = 0;
    std::cout << line << std::endl;
    std::cout << "Welcome to Sandhills Car Care" << std::endl;
    std::cout << line << std::endl;
    for (int i = 0; i < 4; i++) {
      std::cout << services.at(i) << ": $" << prices.at(i) << std::endl;
    }
    std::cout << line << std::endl;
    std::cout << "Enter a service: ";
    std::cin >> choice;
    if (choice < 1 or choice > 4) {
      std::cout << "Your total bill is: $" << total << std::endl;
      break;
    }
    std::cout << "You chose: " << services.at(choice - 1) << ", the price is $"
              << prices.at(choice - 1) << std::endl;
    total += prices.at(choice - 1);
  }

  return 0;
}
