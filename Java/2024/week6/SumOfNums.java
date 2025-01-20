
/*
 Filename: SumOfNums.java
 Author: Mikhail Zubko
 Created: 2024/09/25
 Purpose: Calculate the sum of all natural numbers from 1 to n
*/
import java.util.Scanner;

public class SumOfNums {
  public static void main(String[] args) {
    Scanner keyboard = new Scanner(System.in);
    String input;
    int num;
    while (true) {
      try {
        System.out.print("Enter a positive number: ");
        input = keyboard.nextLine();
        num = Integer.parseInt(input);
      } catch (Exception e) {
        System.out.println(e);
        System.out.println("This is not a number");
        continue;
      }
      if (num < 1) {
        System.out.println("Enter a POSITIVE number");
        continue;
      }
      // break the loop if input is valid
      break;
    }
    // calculate the sum
    int sum = 0;
    for (int i = 1; i <= num; i++) {
      sum += i;
    }
    System.out.println("The sum of the first " + num + " natural numbers is: " + sum);
    keyboard.close();
  }
}
