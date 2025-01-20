// Written by: Mikhail Zubko
// Date: 2024-10-09
// Description: Calculate wages per month

#include <iostream>
using namespace std;

int main() {
  // declare vars
  double hourlyWage;
  double hoursWorked;
  double monthlySalary;
  // ask the user to enter their hourly wage
  cout << "Enter your hourly wage: $";
  // store the input in the var
  cin >> hourlyWage;
  // ask the user to enter the number of hours worked
  cout << "Enter the number of hours worked in a month: ";
  // store the input in the var
  cin >> hoursWorked;
  // calculate the monthly salary by multiplying wage and hours
  monthlySalary = hoursWorked * hourlyWage;
  // display the result to the user
  cout << "Your monthly salary is: $" << monthlySalary << endl;
  // return 0 indicate successfull program execution
  return 0;
}
