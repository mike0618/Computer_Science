
/*
 Filename: DatingDilemma.java
 Author: Mikhail Zubko
 Created: 09/06/24
 Purpose: Get a proger dating age
*/
import java.util.Scanner;

public class DatingDilemma {
  public static void main(String[] args) {
    // TODO: Print creative program title
    System.out.println("--------------------------");
    System.out.println("| The Dating Dilemma App |");
    System.out.println("--------------------------");
    // TODO: Define scanner and variables
    Scanner keyboard = new Scanner(System.in);
    int age;
    int youngest;
    int oldest;
    while (true) {
      // TODO: Get user input
      System.out.print("Enter your age (enter 0 to exit): ");
      age = keyboard.nextInt();
      if (age < 1) {
        System.out.println("Good bye!");
        break;
      }
      // TODO: Calculate youngest
      youngest = (age / 2) + 7;
      // TODO: Calculate oldest
      oldest = (age - 7) * 2;
      // TODO: Print can't date if no dating range
      if (youngest > oldest) {
        System.out.println("You can't date\n");
      } else {
        // TODO: Print results
        System.out.println("You can date someone older than: " + youngest);
        System.out.println("You can date someone younger than: " + oldest + "\n");
      }
    }
    // TODO: Close the scanner object
    keyboard.close();
  }
}
