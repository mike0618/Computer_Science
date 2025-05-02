#include <algorithm>
#include <iostream>
#include <string>

int main() {
  const std::string VOWELS = "aeiouAEIOU";
  std::string word;
  std::string pigword;
  while (true) {
    std::cout << "Enter a word\nto be converted to Pig Latin (q to exit): ";
    std::cin >> word;
    if (word == "q") {
      break;
    }
    if (std::find(VOWELS.begin(), VOWELS.end(), word[0]) != VOWELS.end()) {
      pigword = word + "way";
    } else {
      for (int i = 0; i < word.size(); i++) {
        if (std::find(VOWELS.begin(), VOWELS.end(), word[i]) != VOWELS.end()) {
          pigword = word.substr(i) + word.substr(0, i) + "ay";
          break;
        } else if (i == word.size() - 1) {
          pigword = word;
        }
      }
    }
    std::cout << "PigLatin word: " << pigword << std::endl;
  }

  return 0;
}
