/*
 Filename: tutorials.java
 Author: Mikhail Zubko
 Created: 2024/09/25
 Purpose: 
*/

import java.util.concurrent.TimeUnit;
import java.util.Scanner;

public class tutorials {
  static void SquaresAndCubes() {
    // constants
    String DASHES = "---------------------------------------";
    int square = 0;
    int cube = 0;
    // print headers
    System.out.println(DASHES);
    System.out.println("Number\tSquare\tCube");
    System.out.println(DASHES);
    // for loop 1 - 10
    for (int i = 1; i < 11; i++) {
      // calculate squarea and cube
      square = i * i;
      cube = i * i * i;
      System.out.println(i + "\t" + square + "\t" + cube);
    }

    System.out.println(DASHES);
    System.out.println("\n");
  }

  static void BlastoffForLoop() {
    // a loop 5 - 1
    for (int i = 5; i > 0; i--) {
      System.out.println(i);
      // sleep 1 sec
      try {
        TimeUnit.SECONDS.sleep(1);
      } catch (InterruptedException e) {
        Thread.currentThread().interrupt();
      }
    }

    System.out.println("Blastoff!");
    System.out.println("\n");
  }

  static void RunningTotal(Scanner keyboard) {
    // declare scanner
    // declare vars
    double runningTotal = 0;
    double number;
    // print headers
    System.out.println("+---------------------------------------+");
    System.out.println("|        Sum the entered numbers        |");
    System.out.println("+---------------------------------------+");

    while (true) {
      System.out.print("Enter a number (0 to quit): ");
      // get double and assign to var
      number = keyboard.nextDouble();
      // if 0 break the loop
      if (number == 0) {
        break;
      }
      // accumulate runningTotal
      runningTotal += number;
    }
    System.out.println("The total is: " + runningTotal);
    System.out.println("\n");
  }

  static void InputValidation(Scanner keyboard) {
    int age = 0;
    String input;
    keyboard.nextLine();
    while (true) {
      // try to get a valid input
      try {
        System.out.print("Enter your age: ");
        input = keyboard.nextLine();
        age = Integer.parseInt(input);
      } catch (Exception e) {
        // if the input is not int
        System.out.println(e);
        System.out.println("Enter a whole number");
        // start over
        continue;
      }
      // is the age is a positive number?
      if (age < 1) {
        System.out.println("Enter a positive number");
        continue;
      }
      // break the loop if input is valid
      break;
    }
    System.out.println("Your age is: " + age);
    System.out.println("\n");
  }

  static void NestedFor() {
    System.out.println("==============Nested For Loop===============");
    // exterior loop
    for (int i = 0; i < 3; i++) {
      System.out.println("Exterior Loop: " + i);
      System.out.println("Interior Loop:");
      for (int j = 0; j < 5; j++) {
        System.out.print(j + "\t");
      }
      System.out.println("\n");
    }
  }

  static void NestedWhile() {
    System.out.println("==============Nested While Loop===============");
    int i = 0;
    // exterior loop
    while (i < 3) {
      System.out.println("Exterior Loop: " + i);
      System.out.println("Interior Loop:");
      i++;
      int j = 0;
      while (j < 5) {
        System.out.print(j + "\t");
        j++;
      }
      System.out.println("\n");
    }
  }

  static void MenuChoice(Scanner keyboard) {
    // Declare character variable
    char menuChoice;
    // Prompt user
    System.out.print("Please enter a menu choice (Y/N): ");
    // Character input
    menuChoice = keyboard.next().charAt(0);
    // Convert char to lowercase for easier comparison
    // You can also use toUpperCase()
    menuChoice = Character.toLowerCase(menuChoice);
    // Print the Menu Choice value
    System.out.println("Menu Choice: " + menuChoice);
  }

  public static void main(String[] args) {
    // init scanner
    Scanner keyboard = new Scanner(System.in);
    SquaresAndCubes();
    BlastoffForLoop();
    RunningTotal(keyboard);
    InputValidation(keyboard);
    NestedFor();
    NestedWhile();
    MenuChoice(keyboard);
    // close scanner
    keyboard.close();

  }
}
