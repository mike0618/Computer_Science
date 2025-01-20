/**
 * Name: assign1.cpp
 * Author: Mikhail Zubko
 * Date: 2025-01-16
 * Purpose: Arrays and Vectors
 */

#include <array>
#include <iostream>
#include <limits>

int arrayScores() {
  const int ARR_SIZE = 5;
  std::array<int, ARR_SIZE> scores{};
  int current;
  double total = 0.0;
  int highest = 0;
  int lowest = std::numeric_limits<int>::max();
  double average;
  int nAbove = 0;
  int nBelow = 0;
  std::cout << "Enter the scores for each player:" << std::endl;
  // get scores and calc total, highest and lowest
  for (int i = 0; i < ARR_SIZE; i++) {
    std::cout << "Score for player " << i + 1 << ": ";
    std::cin >> current;
    scores.at(i) = current;
    total += current;
    if (current > highest) {
      highest = current;
    }
    if (current < lowest) {
      lowest = current;
    }
  }
  // calc average
  average = total / ARR_SIZE;
  // calc nAbove and nBelow
  for (int s : scores) {
    if (s > average) {
      nAbove++;
    }
    if (s < average) {
      nBelow++;
    }
  }
  // disp results
  std::cout << std::endl;
  std::cout << "Game Statistics:" << std::endl;
  std::cout << "Total Score: " << total << std::endl;
  std::cout << "Highest Score: " << highest << std::endl;
  std::cout << "Lowest Score: " << lowest << std::endl;
  std::cout << "Average Score: " << average << std::endl;
  std::cout << "Above average players: " << nAbove << std::endl;
  std::cout << "Below average players: " << nBelow << std::endl;

  return 0;
}

int main() {
  std::cout << "\nAssignment 1: Array Game Scores\n" << std::endl;
  arrayScores();
  return 0;
}
