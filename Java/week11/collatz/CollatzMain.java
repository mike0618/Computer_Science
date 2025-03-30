/*
 Filename: CollatzMain.java
 Author: Mikhail Zubko
 Created: 2025/03/27
 Purpose: 
*/

import java.util.ArrayList;
import java.util.Scanner;

public class CollatzMain {
  // Get correct input
  private static int getIntInput(Scanner scanner) {
    while (true) {
      System.out.print("Enter a whole number: ");
      String input = scanner.nextLine().trim().replace(",", "");
      try {
        return Integer.parseInt(input);
      } catch (NumberFormatException e) {
        System.out.println("Wrong input.");
      }
    }
  }

  // Find the number below the given input that produces the longest Collatz chain
  private static void challenge(Collatz collatz, int num) {
    long start = System.nanoTime();

    int maxL = 0;
    int maxN = 0;

    for (int i = 1; i < num; i += 2) {
      int len = collatz.getLen(i);
      if (len > maxL) {
        maxL = len;
        maxN = i;
      }
    }

    System.out.printf("The number %d produces the longest chain of %d steps.%n", maxN, maxL);
    System.out.printf("The function executed in: %.3f seconds%n", (System.nanoTime() - start) / 1e9);
  }

  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);
    Collatz collatz = new Collatz();
    int num;

    System.out.println("The Collatz chain for the entered number.");
    while (true) {
      num = getIntInput(scanner);
      ArrayList<Integer> chain = collatz.getLst(num);

      for (int n : chain) {
        System.out.print(n + " ");
      }
      System.out.println("\nSteps: " + chain.size());
      System.out.print("\nWould you like to try another number? y/n: ");
      String inputstr = scanner.nextLine();
      char ans = inputstr.charAt(0);
      if (ans != 'y') {
        break;
      }
    }

    System.out.println("\nChallenge!\nFind the number below the entered producing the longest Collatz chain.");
    num = getIntInput(scanner);
    challenge(collatz, num);

    scanner.close();
  }
}
