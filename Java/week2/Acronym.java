/*
 Filename: Acronym.java
 Author: Mikhail Zubko
 Created: 2025/01/22
 Purpose: 
*/

import java.util.Scanner;

public class Acronym {
  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);
    StringBuilder Acronym = new StringBuilder("");
    StringBuilder userInput = new StringBuilder("");
    int index;
    System.out.println("If you give me three words, I will turn in into an Acronym.");
    System.out.print("Please enter three words: ");
    userInput.append(kb.nextLine().trim()); // remove trailing whitespaces
    kb.close();
    System.out.println("Original phrase was: " + userInput);
    Acronym.append(userInput.charAt(0));
    for (int i = 0; i < 2; i++) {
      index = userInput.indexOf(" ");
      if (index == -1) { // if no more whitespaces
        break;
      }
      userInput.delete(0, index + 1); // delete the previous word with the whitespace
      Acronym.append(userInput.charAt(0));
    }
    System.out.println("Three letter acronym is: " + Acronym.toString().toUpperCase());

  }
}
