#include <iostream>
#include <unordered_map>

int main() {
  // declare unordered_map
  std::unordered_map<std::string, int> umap;
  // insert some data
  umap["ten"] = 10;
  umap["twenty"] = 20;
  umap["thirty"] = 30;
  // iterate using auto
  for (auto x : umap) {
    std::cout << x.first << " " << x.second << std::endl;
  }
  // access value with a key
  std::cout << "Value at key ten: " << umap.at("ten") << std::endl;
  // change the value
  umap.at("ten") = 100;
  // iterate using auto after changing the value
  for (auto x : umap) {
    std::cout << x.first << " " << x.second << std::endl;
  }

  return 0;
}
