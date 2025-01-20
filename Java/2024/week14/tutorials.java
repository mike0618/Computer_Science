/*
 Filename: tutorials.java
 Author: Mikhail Zubko
 Created: 2024/11/22
 Purpose: 
*/

import java.math.BigInteger;

public class tutorials {
  static void IntegerOverflow() {
    int maxInt = Integer.MAX_VALUE;
    System.out.println("Increment maxInt 4 times using loop to cause overflow:");
    for (int i = 0; i < 4; i++) {
      System.out.println(maxInt);
      // increment maxInt by 1 after each iteration
      maxInt++;
    }
  }

  static void IntegerOverflowMitigation() {
    int maxInt = Integer.MAX_VALUE;
    // convert maxInt to string for easier BigInteger creation
    String maxIntString = maxInt + "";
    // create a BigInteger object to hold a large value that can't overflow an int
    BigInteger largeInt = new BigInteger(maxIntString);
    System.out.println("Increment largeInt (BigInteger) 4 times using loop:");
    for (int i = 0; i < 4; i++) {
      System.out.println(largeInt);
      // increment largeInt by 1
      largeInt = largeInt.add(BigInteger.ONE);

    }

  }

  public static void main(String[] args) {
    System.out.println("Java: Integer Overflow\n");
    IntegerOverflow();
    System.out.println("\nJava: Integer Overflow Mitigation\n");
    IntegerOverflowMitigation();
  }
}
