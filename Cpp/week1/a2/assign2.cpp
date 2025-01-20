/**
 * Name: tutorials.cpp
 * Author: Mikhail Zubko
 * Date: 2025-01-16
 * Purpose: Arrays and Vectors
 */

#include <algorithm> // to use remove()
#include <iostream>
#include <vector>

int vectorScores() {
  std::vector<int> scores;
  int choice;
  int score;
  while (true) {
    std::cout << "\nGame Score Tracker" << std::endl;
    std::cout << "1. Add Score" << std::endl;
    std::cout << "2. Remove Score" << std::endl;
    std::cout << "3. Display Number of Scores" << std::endl;
    std::cout << "4. Display All Scores" << std::endl;
    std::cout << "5. Exit" << std::endl;
    std::cout << "Choose and option: ";
    std::cin >> choice;
    switch (choice) {
    case 1:
      std::cout << "Enter score to add: ";
      std::cin >> score;
      if (std::find(scores.begin(), scores.end(), score) == scores.end()) {
        scores.push_back(score);
        std::cout << "Score " << score << " added successfully." << std::endl;
      } else {
        std::cout << "Error: Score " << score << " already exists."
                  << std::endl;
      }
      break;
    case 2:
      std::cout << "Enter score to remove: ";
      std::cin >> score;
      if (std::find(scores.begin(), scores.end(), score) == scores.end()) {
        std::cout << "Error: Score " << score << " not found." << std::endl;
      } else {
        // use erase-remove idiom
        scores.erase(std::remove(scores.begin(), scores.end(), score),
                     scores.end());
        std::cout << "Score " << score << " removed successfully." << std::endl;
      }
      break;
    case 3:
      break;
    case 4:
      std::cout << "Scores: ";
      for (int s : scores) {
        std::cout << s << " ";
      }
      std::cout << std::endl;
      break;
    default:
      return 0;
    }
    std::cout << "Number of Scores: " << scores.size() << std::endl;
  }

  return 0;
}

int main() {
  std::cout << "\nAssignment 2: Vector Game Scores\n" << std::endl;
  vectorScores();
  return 0;
}
