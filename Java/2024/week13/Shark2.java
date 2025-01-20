/*
 Filename: Shark.java
 Author: Mikhail Zubko
 Created: 2024/11/16
 Purpose: Class to create a shark
*/

public class Shark2 {
  // Define class data attributes
  private String name;
  private int age;

  // Define constructor
  public Shark2() {
  };

  // Constructor with two parameters
  public Shark2(String name, int age) {
    this.name = name;
    this.age = age;
  };

  // Define class getters and setters
  public String getName() {
    return name;
  }

  public void setName(String name) {
    this.name = name;
  }

  public int getAge() {
    return age;
  }

  public void setAge(int age) {
    this.age = age;
  }

  // Define class method
  public void swim() {
    System.out.println(this.name + " is swimming.");
  }
}
