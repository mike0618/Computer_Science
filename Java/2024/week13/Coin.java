/*
 Filename: Coin.java
 Author: Mikhail Zubko
 Created: 2024/11/16
 Purpose: class that wlips a coin
*/

// Import library for random numbers
import java.util.concurrent.ThreadLocalRandom;

public class Coin {
  private final int MIN = 0;
  private final int MAX = 1;
  private int randomNumber;
  private String sideUp;

  public String Flip() {
    // generate a random number
    this.randomNumber = ThreadLocalRandom.current().nextInt(MIN, MAX + 1);
    // determine which side was up
    if (randomNumber == 0) {
      this.sideUp = "Heads";
    } else {
      this.sideUp = "Tails";
    }
    return this.sideUp;
  }

}
