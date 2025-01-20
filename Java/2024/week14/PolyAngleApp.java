/*
 Filename: PolyAngleApp.java
 Author: Mikhail Zubko
 Created: 2024/11/23
 Purpose: 
*/

import java.util.Scanner;

public class PolyAngleApp {
  static int getInt(Scanner input, String prompt) {
    int num;
    while (true) {
      System.out.print(prompt);
      try {
        num = input.nextInt();
        if (num > 2) {
          return num;
        }
        System.out.println("Enter number 3 or greater");
      } catch (Exception e) {
        System.out.println("Enter a whole number");
        input.nextLine();
      }
    }
  }

  static double getFloat(Scanner input, String prompt) {
    double num;
    while (true) {
      System.out.print(prompt);
      try {
        num = input.nextDouble();
        if (num > 0) {
          return num;
        }
        System.out.println("Enter a positive number");
      } catch (Exception e) {
        System.out.println("Enter a number");
        input.nextLine();
      }
    }
  }

  public static void main(String[] args) {
    // variables
    Scanner kb = new Scanner(System.in);
    int sides;
    double length;
    // title
    System.out.println("PolyAngle in Java");
    System.out.println("---------------------------------");
    System.out.println("Calculate angles and perimeter of a regular polygon");
    // get and validate user input
    sides = getInt(kb, "Enter number of sides  >> ");
    length = getFloat(kb, "Enter length of a side >> ");
    System.out.println("---------------------------------");
    // create the object
    PolyAngle polyangle = new PolyAngle(sides, length);
    // print the polygon info using toString method
    System.out.println(polyangle);
  }
}
