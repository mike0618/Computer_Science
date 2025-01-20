/*
 Filename: CarCare.java
 Author: Mikhail Zubko
 Created: 2024/11/08
 Purpose: 
*/

import java.util.Scanner;

public class CarCare {
  // user input validating method
  static int getInt(Scanner input, boolean checkPositive, int limit) {
    int num;
    while (true) {
      try {
        num = input.nextInt();
        if (checkPositive) {
          if (num >= 0 && num < limit) {
            return num;
          }
          System.out.println("Enter a positive number less than " + limit);
          continue;
        }
        return num;
      } catch (Exception e) {
        System.out.println("Enter a whole number");
        input.nextLine();

      }
    }
  }

  public static void main(String[] args) {
    // TODO: define constants, variables and scanner
    final String line = "***********************************************";
    final String[] services = { "1. Oil change", "2. Tire rotation", "3. Battery check", "4. Brake inspection" };
    final int[] prices = { 25, 22, 15, 5 };
    final int len = services.length;
    int total = 0;
    int choice = 0;
    String service;
    int price;
    Scanner keyboard = new Scanner(System.in);
    // TODO: print title
    System.out.println(line);
    System.out.println("Welcome to Sandhills Car Care");
    // TODO: create a menu loop
    while (true) {
      // TODO: print the menu between two lines
      System.out.println(line);
      for (int x = 0; x < len; x++) {
        System.out.println(services[x] + ": $" + prices[x]);
      }
      System.out.println(line);
      // TODO: ask the user for choice and get a validated input
      System.out.print("Enter a service (0 to quit): ");
      choice = getInt(keyboard, true, len + 1);
      // exit the menu if choice is 0
      if (choice == 0) {
        System.out.println(line);
        break;
      }
      // TODO: show user choice and increment total
      choice--;
      service = services[choice];
      price = prices[choice];
      System.out.println("\nYou chose: " + service + ", price is: $" + price + "\n");
      total += price;
    }
    // TODO: after exit the loop show the total bill
    System.out.println("Your total bill is: $" + total);
  }
}
