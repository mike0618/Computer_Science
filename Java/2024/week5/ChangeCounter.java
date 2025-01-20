/*
 Filename: ChangeCounter.java
 Author: Mikhail Zubko
 Created: 2024/09/20
 Purpose: Convert dollars into change
*/

import java.util.Scanner;

public class ChangeCounter {
  public static void main(String[] args) {
    // TODO: Declare currency value constants needed for counting change
    Scanner input = new Scanner(System.in);

    // TODO: Declare variables needed for conversion
    int dollars = 0;
    int remain = 0;
    int twenties = 0;
    int tens = 0;
    int fives = 0;
    // TODO: Print creative title
    System.out.println("-----------------------------");
    System.out.println("|       Change Counter      |");
    System.out.println("-----------------------------");

    while (true) {

      // TODO: Get dollars input from user
      try {
        System.out.print("Enter dollars, or 0 to exit: ");
        dollars = input.nextInt();
      } catch (Exception e) {
        System.out.println("The number is incorrect.");
        input.nextLine();
        continue;
      }
      if (dollars == 0) {
        break;
      }
      // TODO: Calculate change in 20's, 10's, 5's, and 1's
      twenties = dollars / 20;
      remain = dollars % 20;
      tens = remain / 10;
      remain %= 10;
      fives = remain / 5;
      remain %= 5;
      // TODO: Display result
      System.out.printf("$%d is:\n%d - $20's\n%d - $10's\n%d - $5's\n%d - $1's\n\n", dollars, twenties, tens, fives,
          remain);
    }
    // Close scanner input object
    input.close();
  }
}
