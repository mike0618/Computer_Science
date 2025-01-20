/*
 Filename: FruitInventory.java
 Author: Mikhail Zubko
 Created: 2025/01/16
 Purpose: 
*/

import java.util.HashMap;
import java.util.Scanner;

public class FruitInventory {
  protected static int getInput(Scanner keyboard, String prompt) {
    int result;
    while (true) {
      try {
        System.out.print(prompt);
        result = keyboard.nextInt();
        if (result < 0) {
          System.out.println("Enter a positive number.");
          continue;
        }
        return result;
      } catch (Exception e) {
        System.out.println("Enter a whole number.");
        keyboard.nextLine();
      }
    }
  }

  static void showMap(HashMap<String, Integer> map) {
    for (String entry : map.keySet()) {
      // use get(entry) to retrive the value
      System.out.println("Key: " + entry + ", Value: " + map.get(entry));
    }
  }

  public static void main(String[] args) {
    Scanner keyboard = new Scanner(System.in);
    HashMap<String, Integer> myMap = new HashMap<String, Integer>();
    char choice;
    String fruit;
    int quantity;

    System.out.println("--- Welcome to my Fruit Inventory System! ---");

    while (true) {
      System.out.print("\nEnter a fruit name to add: ");
      fruit = keyboard.nextLine();
      quantity = getInput(keyboard, "Enter the quantity for " + fruit + ": ");
      myMap.put(fruit, quantity);
      System.out.println("\nUpdated Fruit Inventory: ");
      showMap(myMap);
      System.out.print("\nDo you want to add more fruits? (y/n): ");
      choice = Character.toLowerCase(keyboard.next().charAt(0));
      if (choice != 'y') {
        System.out.println("\nFinal Fruit Inventory: ");
        showMap(myMap);
        break;
      }
      keyboard.nextLine();
    }
  }
}
