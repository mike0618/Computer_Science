
/*
 Filename: PizzaPlanet.java
 Author: Mikhail Zubko
 Created: 2024/10/03
 Purpose: Calculate the final bill
*/
import java.util.Scanner;

public class PizzaPlanet {
  static char GetInput(String prompt, Scanner keyboard, char[] opts) {
    char result = 'n';
    while (true) {
      System.out.print(prompt);
      try {
        result = Character.toLowerCase(keyboard.next().charAt(0));
      } catch (Exception e) {
        // TODO: handle exception
        System.out.println("Wrong input. Try again.");
        continue;
      }
      // TODO: check if the option exists
      for (char c : opts) {
        if (c == result) {
          return result;
        }
      }
      System.out.println("Wrong option. Try again.");
    }
  }

  public static void main(String[] args) {
    // define constants
    final int SmallP = 15;
    final int MediumP = 20;
    final int LargeP = 25;
    // TODO: define scanner
    Scanner keyboard = new Scanner(System.in);
    // TODO: define vars
    char size;
    char pepperoni;
    char cheese;
    char[] sizes = { 's', 'm', 'l' };
    char[] opts = { 'y', 'n' };
    // TODO: print headers
    System.out.println("+-------------------------------------------+");
    System.out.println("|     ---     Java Pizza Planet     ---     |");
    System.out.println("+-------------------------------------------+");
    // TODO: game loop
    while (true) {
      int total = 0;
      System.out.println("\nWelcome to Java Pizza Planet!");
      // TODO: print sizes ans ask size
      System.out.println("\nSmall Pizza: $" + SmallP);
      System.out.println("Medium Pizza: $" + MediumP);
      System.out.println("Large Pizza: $" + LargeP);
      size = GetInput("Size of Pizza? (S, M, or L): ", keyboard, sizes);
      // TODO: ask about pepperoni
      System.out.println("\nPepperoni for Small Pizza: +$2");
      System.out.println("Pepperoni for Medium or Large Pizza: +$3");
      pepperoni = GetInput("Do you want pepperoni? (Y/N): ", keyboard, opts);
      // TODO: ask about extra cheese
      System.out.println("\nExtra cheese for any pizza: +$1");
      cheese = GetInput("Do you want extra cheese? (Y/N): ", keyboard, opts);
      // TODO: logic and calculations
      if (size == 's') {
        total += SmallP;
        if (pepperoni == 'y') {
          total += 2;
        }
      } else if (size == 'm') {
        total += MediumP;
        if (pepperoni == 'y') {
          total += 3;
        }
      } else if (size == 'l') {
        total += LargeP;
        if (pepperoni == 'y') {
          total += 3;
        }
      }
      if (cheese == 'y') {
        total += 1;
      }
      // TODO: print result
      System.out.println("\nYour final bill is: $" + total);
      // TODO: exit condition
      System.out.println("\nThanks for ordering from Java Pizza Planet!");
      if (GetInput("Order another pizza? (Y/N): ", keyboard, opts) == 'n') {
        break;
      }
    }

    keyboard.close();
  }
}
