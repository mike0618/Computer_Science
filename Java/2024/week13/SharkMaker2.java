/*
 Filename: SharkMaker.java
 Author: Mikhail Zubko
 Created: 2024/11/16
 Purpose: Demonstrate classes and objects
*/

public class SharkMaker2 {
  public static void main(String[] args) {
    // create a Shark object
    // use the default constructor
    System.out.println("Sammy the shark uses the default constructor.");
    Shark2 sammy = new Shark2();

    // Set the name and age
    sammy.setName("Sammy");
    sammy.setAge(3);
    // Call and object method
    sammy.swim();
    // Get the object data attributes
    System.out.println(sammy.getName() + " is " + sammy.getAge() + " years old.");

    // use the parameterized constructor
    System.out.println("Susie the shark uses the parameterized constructor.");
    Shark2 susie = new Shark2("Susie", 2);
    // Call and object method
    susie.swim();
    // Get the object data attributes
    System.out.println(susie.getName() + " is " + susie.getAge() + " years old.");
  }
}
