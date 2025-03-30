
/*
 Filename: collatz.java
 Author: Mikhail Zubko
 Created: 2025/03/27
 Purpose: 
*/
import java.util.ArrayList;

public class Collatz {
  // Get the Collatz sequence as an array
  public ArrayList<Integer> getLst(int num) {
    ArrayList<Integer> lst = new ArrayList<>();
    while (num > 1) {
      if (num % 2 == 0) {
        num /= 2;
      } else {
        num = num * 3 + 1;
      }
      lst.add(num);
    }
    return lst;
  }

  // Get the length of the Collatz sequence
  public int getLen(long num) {
    int len = 0;
    while (num > 1) {
      if (num % 2 == 1) {
        num = num * 3 + 1;
      } else {
        num /= 2;
      }
      len++;
    }
    return len;
  }
}
