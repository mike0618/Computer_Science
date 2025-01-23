#include <iostream>
#include <unordered_map>

void showMap(std::unordered_map<std::string, int> umap);

int main() {
  std::unordered_map<std::string, int> inventory;
  std::string fruit;
  std::string dummy; // to consume newlines
  int quantity;
  char choice;
  std::cout << "--- Welcome to my Fruit Inventory System! ---" << std::endl;
  while (true) {
    quantity = 0;
    std::cout << "Enter a fruit name to add: ";
    std::getline(std::cin, fruit);
    std::cout << "Enter the quantity for " << fruit << ": ";
    std::cin >> quantity;
    if (quantity < 1) {
      std::cout << "Wrong input." << std::endl;
      std::cin.clear();              // clear the error flag
      std::getline(std::cin, dummy); // clear the input
      continue;
    }
    inventory[fruit] = quantity;
    std::cout << std::endl;
    std::cout << "Updated Fruit Inventory:" << std::endl;
    showMap(inventory);
    std::cout << std::endl;
    std::cout << "Do you want to add more fruits? (y/n): ";
    std::cin >> choice;
    std::getline(std::cin, dummy); // clear the input
    std::cout << std::endl;
    if (choice != 'y') {
      std::cout << "Final Fruit Inventory:" << std::endl;
      showMap(inventory);
      break;
    }
  }

  return 0;
}
void showMap(std::unordered_map<std::string, int> umap) {
  for (auto x : umap) {
    std::cout << "Key: " << x.first << ", Value: " << x.second << std::endl;
  }
}
