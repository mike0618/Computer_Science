/*
 Filename: tutorials.java
 Author: Mikhail Zubko
 Created: 2024/10/09
 Purpose: 
*/

import java.util.Scanner;
// import java.lang.Math; // not necessary to import Math lib

public class tutorials {
  // void method
  static void message() {
    System.out.println("It is not necessary to change. Survival is not mandatory.");
    System.out.println("W. Edwards Deming");
  }

  // void method with 1 arg
  static void findSquareRoot(double num) {
    double squareRoot;
    squareRoot = Math.sqrt(num);
    System.out.println("The square root of " + num + " is: " + squareRoot);
  }

  // void method with 2 args
  static void multiply(double num1, double num2, String message) {
    double product;
    product = num1 * num2;
    System.out.println(message);
    System.out.println("The product of " + num1 + "*" + num2 + " is: " + product);
  }

  // method with 1 arg and returns 1 double
  static double getCeil(double num) {
    double numCeil;
    numCeil = Math.ceil(num);
    return numCeil;
  }

  // prompt user for input, return double
  static double getDouble(String prompt, Scanner input) {
    String lineInput;
    double doubleValue = 0;
    System.out.print(prompt);
    lineInput = input.nextLine();
    try {
      doubleValue = Double.parseDouble(lineInput);
      return doubleValue;
    } catch (Exception e) {
      return (getDouble("Enter a number: ", input)); // recursion here!
    }
  }

  static int getResult(int num) {
    return num * 2;
  }

  static int getResult(int num1, int num2) {
    return num1 * num2;
  }

  static int getResult(int num, String value) {
    return num * Integer.parseInt(value);
  }

  static String getResult(String str1, String str2) {
    return str1 + " " + str2;
  }

  static void countDownFrom(int num) {
    if (num >= 0) {
      System.out.print(num + " ");
      countDownFrom(num - 1); // recursion!
    }
  }

  static void countUpTo(int from, int to) {
    if (from <= to) {
      System.out.print(from + " ");
      countUpTo(from + 1, to); // recursion!
    }
  }

  public static void main(String[] args) {
    Scanner input = new Scanner(System.in);
    System.out.println("\ntutorial 5.1");
    System.out.println("First call of message");
    message();
    System.out.println("\nSecond call of message");
    message();
    System.out.println("\nThird call of message");
    message();
    System.out.println("\ntutorial 5.2");
    double num1 = 4;
    double num2 = 8.9;
    double num3 = 112;
    findSquareRoot(num1);
    findSquareRoot(num2);
    findSquareRoot(num3);
    System.out.println("\ntutorial 5.3");
    num1 = 2.45;
    num2 = 3.4;
    num3 = 5.02;
    double num4 = 15.2;
    String message = "\nFirst method call";
    multiply(num1, num2, message);
    message = "\nSecond method call";
    multiply(num3, num4, message);
    System.out.println("\ntutorial 5.4");
    num1 = 4.54;
    num2 = 8.2;
    double ceil2;
    System.out.println("\nPrint method returns value directly");
    System.out.println(getCeil(num1));
    System.out.println("Assign return value to variable");
    ceil2 = getCeil(num2);
    System.out.println(ceil2);
    System.out.println("\ntutorial 5.5");
    double inches;
    inches = getDouble("Enter inches: ", input);
    System.out.println("Inches: " + inches);
    System.out.println("\ntutorial 5.6");
    System.out.println("Method Overloading");
    int result;
    System.out.println("Method with a single int arg");
    result = getResult(5);
    System.out.println(result);
    System.out.println("Method with two int args");
    result = getResult(5, 4);
    System.out.println(result);
    System.out.println("Method with an int and a string args");
    result = getResult(5, "12");
    System.out.println(result);
    System.out.println("Method with two string args");
    System.out.println(getResult("Billy", "Idol"));
    System.out.println("\ntutorial 5.7");
    System.out.println("Countdown");
    countDownFrom(10);
    System.out.println();
    System.out.println("Countup");
    countUpTo(0, 10);
    System.out.println();

    input.close();
  }
}
