#include <cstring>
#include <iostream>

void vulnerable() {
  char buffer[5];
  std::cout << "Enter your name: ";
  std::cin >> buffer; // unsafe
  std::cout << "You entered: " << buffer << std::endl;
}

void good() {
  char buffer[5];
  std::cout << "Enter your name: ";
  std::cin.getline(buffer, sizeof(buffer)); // safe
  std::cout << "You entered: " << buffer << std::endl;
}

int main() {
  // vulnerable();
  good();
  return 0;
}
