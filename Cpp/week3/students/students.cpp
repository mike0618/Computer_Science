#include <array>
#include <iostream>
#include <string>

struct Student {
  std::string name;
  int age;
  char grade;
};

int main() {
  // define const and vars
  const int MAX_STUDENTS = 3;
  std::array<Student, MAX_STUDENTS> students{};
  std::cout << "Enter information for 3 students:" << std::endl;
  // get input
  for (int i = 0; i < MAX_STUDENTS; i++) {
    std::cout << "Student " << i + 1 << ":" << std::endl;
    Student student;
    std::cout << "Name: ";
    std::getline(std::cin >> std::ws, student.name);
    std::cout << "Age: ";
    std::cin >> student.age;
    std::cout << "Grade: ";
    std::cin >> student.grade;
    students[i] = student;
  }
  // disp results
  std::cout << "\nStudent details:" << std::endl;
  for (int i = 0; i < MAX_STUDENTS; i++) {
    std::cout << "Student " << i + 1 << ":" << std::endl;
    std::cout << "Name: " << students[i].name << std::endl;
    std::cout << "Age: " << students[i].age << std::endl;
    std::cout << "Grade: " << students[i].grade << std::endl;
    std::cout << std::endl;
  }
  return 0;
}
