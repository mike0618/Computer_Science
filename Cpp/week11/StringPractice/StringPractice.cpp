/**
 * Name: tutorials.cpp
 * Author: Mikhail Zubko
 * Date: 2025-01-16
 * Purpose: Arrays and Vectors
 */

#include <cctype>
#include <iostream>
#include <string>

bool isVowel(char ch) {
  ch = std::tolower(ch);
  return ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u';
}

int main() {
  std::string str;
  std::cout << "Enter your string: ";
  getline(std::cin, str);
  int size = str.size();
  std::cout << "Number of characters: " << size << std::endl;
  std::cout << "The last character: " << str[size - 1] << std::endl;
  bool vowel_found = false;
  for (int i = 0; i < size; i++) {
    if (isVowel(str[i])) {
      vowel_found = true;
      std::cout << "The first vowel is at index: " << i << std::endl;
      break;
    }
  }
  if (!vowel_found) {
    std::cout << "No vowels found in the string." << std::endl;
  }

  for (int i = 0; i < size; i++) {
    str[i] = std::toupper(str[i]);
  }
  std::cout << "String to UPPERCASE: " << str << std::endl;
  for (int i = 0; i < size; i++) {
    str[i] = std::tolower(str[i]);
  }
  std::cout << "String to lowercase: " << str << std::endl;
  return 0;
}
