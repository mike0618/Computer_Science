/**
 * Name: tutorials.cpp
 * Author: Mikhail Zubko
 * Date: 2025-01-16
 * Purpose: Arrays and Vectors
 */

#include <array>
#include <iostream>
#include <string>
#include <vector>

int arrays() {
  // constant for Array size
  const int ARR_SIZE = 10;
  // create an empty int array
  std::array<int, ARR_SIZE> numerArray{};
  // hard coded array of strings
  std::array<std::string, 4> names{"Bob", "Sally", "John", "Ed"};
  std::cout << "Fill array with integers with for loop" << std::endl;
  for (int i = 0; i < ARR_SIZE; i++) {
    numerArray.at(i) = i;
    std::cout << numerArray[i] << " ";
  }
  // Access individual array elements
  numerArray.at(1) = 25;
  numerArray.at(3) = numerArray.at(4) * 2;
  numerArray.at(8)++;
  numerArray.at(2) += 20;
  std::cout << "\numerArray after accessing the array." << std::endl;
  // go through the array and print it's elements
  for (int i = 0; i < numerArray.size(); i++) {
    std::cout << numerArray.at(i) << " ";
  }
  std::cout << "\nFor Each loop with the array." << std::endl;
  for (std::string a : names) {
    std::cout << a << " ";
  }
  std::cout << std::endl;
  return 0;
}
int vectors() {
  const int NUM_PEOPLE = 2;
  // create 2 parallel vectors
  std::vector<std::string> names;
  std::vector<int> hourlyPay;
  // vars to store the users input
  std::string tempName;
  int tempHourlyPay;
  // fill up vectors with info
  for (int i = 0; i < NUM_PEOPLE; i++) {
    std::cout << "Enter a person's name: ";
    std::getline(std::cin, tempName);
    std::cout << "Enter " << tempName << "'s hourly pay: ";
    std::cin >> tempHourlyPay;
    std::cin.get(); // to consume the newline leftover
    // Add vars to the end of the vectors
    names.push_back(tempName);
    hourlyPay.push_back(tempHourlyPay);
  }
  std::cout << std::endl;
  // display the info using a loop
  for (int i = 0; i < NUM_PEOPLE; i++) {
    std::cout << names.at(i) << "'s hourly pay is " << hourlyPay.at(i)
              << std::endl;
  }
  return 0;
}

int average() {
  double sum = 0.0;
  double average = 0.0;
  const int NUM_ENTRIES = 5;
  std::vector<double> numbers(NUM_ENTRIES);
  std::cout << "Enter " << NUM_ENTRIES << " numbers: ";
  // allow the user to enter in the values
  for (int i = 0; i < NUM_ENTRIES; i++) {
    std::cin >> numbers.at(i);
    sum += numbers.at(i);
  }
  // calc the average
  average = sum / NUM_ENTRIES;
  // disp results
  std::cout << "The average of ";
  for (int i = 0; i < NUM_ENTRIES - 1; i++) {
    std::cout << numbers.at(i) << ", ";
  }
  std::cout << numbers.at(NUM_ENTRIES - 1) << " is " << average << std::endl;

  return 0;
}

int main() {
  std::cout << "\nTutorial 2: MoreArrayFun\n" << std::endl;
  arrays();
  std::cout << "\nTutorial 3: MoreVectorFun\n" << std::endl;
  vectors();
  std::cout << "\nTutorial 4: VectorAverage\n" << std::endl;
  average();
  return 0;
}
