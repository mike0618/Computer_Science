/*
 Filename: MaxOfThree.java
 Author: Mikhail Zubko
 Created: 2024/10/09
 Purpose: 
*/

import java.util.Scanner;

public class MaxOfThree {
  static int findMax(int n1, int n2, int n3) {
    // TODO: find the max int and return it
    int maxn = 0;
    if (n1 > n2) {
      maxn = n1;
    } else {
      maxn = n2;
    }
    if (n3 > maxn) {
      maxn = n3;
    }
    return maxn;
  }

  public static void main(String[] args) {
    // define num vars, and scanner
    Scanner input = new Scanner(System.in);
    int n1, n2, n3;
    // TODO: get the correct input
    while (true) {
      try {
        System.out.print("Enter the first number: ");
        n1 = input.nextInt();
        System.out.print("Enter the second number: ");
        n2 = input.nextInt();
        System.out.print("Enter the third number: ");
        n3 = input.nextInt();
        break;
      } catch (Exception e) {
        // TODO: handle exception
        System.out.println("Something wrong with your input, try again.");
        input.nextLine(); // to clear the input buffer
      }
    } // I'm avoiding recursions
    input.close();
    System.out.println("The maximum of the three numbers is: " + findMax(n1, n2, n3));

  }
}
