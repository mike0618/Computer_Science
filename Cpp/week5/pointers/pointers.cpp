#include <iostream>

void increment(int *pNum) {
  // increment the value pointed to by ptr
  (*pNum)++;
}

int main() {
  int num = 42;
  int *pNum;   // declare a pointer for int
  pNum = &num; // assign the memory address of var to the pointer
  // int *pNum = & num; // short way to declare and assign
  std::cout << "pNum memory address: " << pNum << std::endl;
  std::cout << "Value of num: " << num << std::endl;
  // dereference the pointer
  std::cout << "Value of *pNum: " << *pNum << std::endl;
  // update the value if num through the pointer
  *pNum = 20;
  std::cout << "Value of num after update: " << num << std::endl;
  // dynamically allocate memory
  int *ptr = new int;
  // store a value in dynamically allocated memory
  *ptr = 21;
  std::cout << "Value stored in dynamically allocated memory: " << *ptr
            << std::endl;
  // always free the dynamically allocated memory to avoid memory leaks
  delete ptr;
  // pass a pointer to num to the function
  increment(pNum);
  std::cout << "Value of num after increment: " << num << std::endl;
  // Declare an array of ints
  int arr[] = {2, 4, 6, 8};
  // create a pointer to the first element of the array
  int *pArr = arr;
  std::cout << *pArr << std::endl;
  std::cout << *(pArr + 1) << std::endl;
  std::cout << *(pArr + 2) << std::endl;
  std::cout << "Loop through the array" << std::endl;
  for (int i = 0; i < sizeof(arr) / sizeof(*pArr); i++) {
    std::cout << *pArr << std::endl;
    pArr++;
  }
  return 0;
}
