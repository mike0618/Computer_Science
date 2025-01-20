/*
 Filename: FruitHashMap.java
 Author: Mikhail Zubko
 Created: 2025/01/16
 Purpose: 
*/

import java.util.HashMap;

public class FruitHashMap {
  public static void main(String[] args) {
    // Create a HashMap with String key and Integer value
    HashMap<String, Integer> myMap = new HashMap<String, Integer>();
    // Add key-value pairs to myMap
    myMap.put("apple", 10);
    myMap.put("orange", 20);
    myMap.put("banana", 15);
    myMap.putIfAbsent("banana", 99); // will not be changed because already exists
    myMap.putIfAbsent("durian", 55); // will be added
    // Loop through each key in myMap
    // keySet() returns keys
    for (String entry : myMap.keySet()) {
      // use get(entry) to retrive the value
      System.out.println("Key: " + entry + ", Value: " + myMap.get(entry));
    }

  }
}
