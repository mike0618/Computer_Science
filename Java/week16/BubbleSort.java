
/*
 Filename: BubbleSort.java
 Author: Mikhail Zubko
 Created: 2025/05/01
 Purpose: 
*/
import java.util.Random;
import java.util.Arrays;

public class BubbleSort {
  public static void main(String[] args) {
    Random rand = new Random();
    int[] lst = new int[99];
    int len = lst.length - 1;
    // add random ints to the array
    for (int i = 0; i < lst.length; i++) {
      lst[i] = rand.nextInt(100); // upper bound is exclusive
    }
    System.out.println("Java Bubble Sort\n");
    System.out.println(Arrays.toString(lst));
    boolean swap = true;
    while (swap) {
      swap = false;
      for (int i = 0; i < len; i++) {
        if (lst[i] > lst[i + 1]) {
          swap = true;
          // Swap using temp var
          int temp = lst[i];
          lst[i] = lst[i + 1];
          lst[i + 1] = temp;
        }
      }
    }
    System.out.println();
    System.out.println(Arrays.toString(lst));
  }
}
