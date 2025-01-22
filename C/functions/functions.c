#include <stdio.h>

// Create a function: return_type name(input){body;}
void myFunction() { printf("I just got executed!\n"); }

// name, age - parameters
void functionWithParameters(char name[], int age) {
  printf("Hello %s. You are %d years old.\n", name, age);
}

void arrayInput(int arr[5]) {
  for (int i = 0; i < 5; i++) {
    printf("%d\n", arr[i]);
  }
}

// Function with return float
float toCelsius(float f) { return (f - 32.0) / 1.8; }

float x = 7.11; // global variable
void funcScope() {
  float x = 33.3;                      // local variable
  printf("Local variable: %.2f\n", x); // refers to local var
}

// Function Declaration - recommended
// return_type name(parameters);
void decFunction(int x, int y);
int sumRec(int k);

// Math Functions
#include <math.h>

int main() {
  printf("Hello, World!\n");
  myFunction();                       // call a function
  functionWithParameters("Mike", 39); // Mike, 39 - arguments
  int myNumbers[] = {3, 5, 8, 13, 21};
  arrayInput(myNumbers);
  float f_temp = 26.0;
  printf("Fahrenheit: %.2f\n", f_temp);
  printf("Celsius: %.2f\n", toCelsius(26.0));
  funcScope();
  printf("Global variable: %.2f\n", x); // referes to global var
  ++x;                                  // global variable CAN be modified!!!
  printf("Modified Global variable: %.2f\n", x);
  decFunction(55, 34);
  printf("Sum of numbers = %d\n", sumRec(10));
  printf("%f\n", sqrt(16));
  printf("%f\n", ceil(1.4));
  printf("%f\n", floor(1.4));
  printf("%f\n", pow(4, 3));

  return 0;
}

// Function Definition
void decFunction(int x, int y) { printf("Sum is %d\n", x + y); }
// Recursion
int sumRec(int k) {
  if (k > 0) {
    return k + sumRec(k - 1);
  } else {
    return 0;
  }
}
