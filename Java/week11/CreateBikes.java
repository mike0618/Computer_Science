/*
 Filename: CreateBikes.java
 Author: Mikhail Zubko
 Created: 2025/03/27
 Purpose: 
*/

public class CreateBikes {
  public static void main(String[] args) {
    // using default constructor
    Bicycle bike1 = new Bicycle();
    System.out.println(bike1);
    bike1.shiftGears(20);
    bike1.speedUP(10);
    System.out.println(bike1.toString());
    // using parameter based constructor
    Bicycle b2 = new Bicycle(24, 30);
    System.out.println(bike1);
    System.out.println(b2);
    // mtb child class
    MountainBike mtb = new MountainBike(30, 10, 25);
    System.out.println(mtb);

  }
}
