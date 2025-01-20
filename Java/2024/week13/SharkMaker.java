/*
 Filename: SharkMaker.java
 Author: Mikhail Zubko
 Created: 2024/11/16
 Purpose: Demonstrate classes and objects
*/

public class SharkMaker {
  public static void main(String[] args) {
    // create a Shark object
    System.out.println("Sammy the shark is created.");
    Shark sammy = new Shark();

    // Set the name and age
    sammy.setName("Sammy");
    sammy.setAge(3);
    // Call and object method
    sammy.swim();
    // Get the object data attributes
    System.out.println(sammy.getName() + " is " + sammy.getAge() + " years old.");
  }
}
