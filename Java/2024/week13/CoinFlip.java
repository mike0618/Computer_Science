/*
 Filename: CoinFlip.java
 Author: Mikhail Zubko
 Created: 2024/11/16
 Purpose: 
*/

public class CoinFlip {
  public static void main(String[] args) {
    String tossResult = "";
    // Create a Coin object
    Coin quarter = new Coin();

    // Flip the coin 10 times
    for (int i = 0; i < 10; i++) {
      // call object Flip method, return a string
      tossResult = quarter.Flip();
      System.out.println(tossResult);
    }
  }
}
