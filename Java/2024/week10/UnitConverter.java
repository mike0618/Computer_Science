
/*
 Filename: UnitConverter.java
 Author: Mikhail Zubko
 Created: 2024/10/25
 Purpose: 
*/
import java.util.Scanner;

public class UnitConverter {

  // TODO: create conversion methods
  static double CmToInches(double cm, double COEF) {
    return cm / COEF;
  }

  static double InchesToCm(double in, double COEF) {
    return in * COEF;
  }

  static double KmToMiles(double km, double COEF) {
    return km / COEF;
  }

  static double MilesToKm(double mi, double COEF) {
    return mi * COEF;
  }

  // TODO: create a get choice function
  static int Choice(Scanner keyboard) {
    System.out.println("Choose a conversion");
    System.out.println("(1) Centimeters --> Inches");
    System.out.println("(2) Inches --> Centimeters");
    System.out.println("(3) Kilometers --> Miles");
    System.out.println("(4) Miles --> Kilometers");
    int choice;
    while (true) {
      System.out.print("Enter your choice: ");
      try {
        choice = keyboard.nextInt();
      } catch (Exception e) {
        // TODO: handle exception
        System.out.println("Enter an integer");
        keyboard.nextLine();
        continue;
      }
      if (choice < 1 || choice > 4) {
        System.out.println("This option does not exist, try again");
        continue;
      }
      return choice;
    }
  }

  // TODO: create a get source input function
  static double Source(Scanner keyboard, String units) {
    double src;
    while (true) {
      System.out.print("Enter " + units + ": ");
      try {
        src = keyboard.nextDouble();
      } catch (Exception e) {
        // TODO: handle exception
        System.out.println("Enter a float number");
        keyboard.nextLine();
        continue;
      }
      if (src < 0) {
        System.out.println("The input is invalid, enter a positive number");
        continue;
      }
      return src;
    }
  }

  // TODO: main method with menu and user input
  public static void main(String[] args) {
    // TODO: define constants, scanner and variables
    final double IN_CM = 2.54;
    final double MI_KM = 1.60934;
    Scanner keyboard = new Scanner(System.in);
    int choice;
    int another;
    double source = 0;
    double result = 0;
    String src_units = "";
    String dst_units = "";
    // TODO: print a title
    System.out.println("+--------------------------------------+");
    System.out.println("|   Mickey's Multiple Unit Converter   |");
    System.out.println("+--------------------------------------+");
    while (true) {
      choice = Choice(keyboard);
      // TODO: perform calculation and show result
      switch (choice) {
        case 1:
          src_units = "Centimeters";
          dst_units = "Inches";
          source = Source(keyboard, src_units);
          result = CmToInches(source, IN_CM);
          break;
        case 2:
          src_units = "Inches";
          dst_units = "Centimeters";
          source = Source(keyboard, src_units);
          result = InchesToCm(source, IN_CM);
          break;
        case 3:
          src_units = "Kilometers";
          dst_units = "Miles";
          source = Source(keyboard, src_units);
          result = KmToMiles(source, MI_KM);
          break;
        case 4:
          src_units = "Miles";
          dst_units = "Kilometers";
          source = Source(keyboard, src_units);
          result = MilesToKm(source, MI_KM);
      }
      System.out.printf("%.2f %s is %.2f %s\n", source, src_units, result, dst_units);
      // TODO: ask to continue or quit
      System.out.print("Another conversion?\n(1) Yes (any) quit: ");
      try {
        another = keyboard.nextInt();
        if (another == 1) {
          continue;
        }
      } catch (Exception e) {
        // I don't care about this exception here
      }
      System.out.println("Bye!");
      break;
    }
    keyboard.close();
  }
}
