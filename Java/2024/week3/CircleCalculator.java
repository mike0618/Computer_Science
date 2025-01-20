
/*
 Filename: CircleCalculator.java
 Author: Mikhail Zubko
 Created: 09/06/24
 Purpose: Calculate the diameter, area and Circumference of a circle
*/
import java.util.Scanner;
import java.text.DecimalFormat;

public class CircleCalculator {
  public static void main(String[] args) {
    // TODO: Print creative program title
    System.out.println("*****************************");
    System.out.println("* Circe's Circle Calculator *");
    System.out.println("*****************************");
    // TODO: Define scanner and variables
    Scanner keyboard = new Scanner(System.in);
    double radius;
    double diameter;
    double area;
    double circumference;
    DecimalFormat df = new DecimalFormat("#.##");
    while (true) {
      // TODO: Get user input
      System.out.print("Enter a radius (enter 0 to exit): ");
      radius = keyboard.nextDouble();
      if (radius == 0 || radius < 0) {
        System.out.println("Good bye!");
        break;
      }
      // TODO: Calculate diameter
      diameter = radius * 2;
      // TODO: Calculate area
      area = radius * radius * Math.PI;
      // TODO: Calculate circumference
      circumference = diameter * Math.PI;
      // TODO: Print results with formatting
      System.out.println("\n*****************************");
      System.out.println("The radius is: " + df.format(radius));
      System.out.println("     Diameter: " + df.format(diameter));
      System.out.println("         Area: " + df.format(area));
      System.out.println("Circumference: " + df.format(circumference));
      System.out.println("*****************************\n");
    }
    // TODO: Close the scanner object
    keyboard.close();
  }
}
