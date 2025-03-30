/*
 Filename: Bicycle.java
 Author: Mikhail Zubko
 Created: 2025/03/27
 Purpose: 
*/

public class Bicycle {
  // Privete fields
  private int gear;
  private int speed;

  // default constructor
  public Bicycle() {
  }

  // constructor with parameters
  public Bicycle(int gear, int speed) {
    this.gear = gear;
    this.speed = speed;
  }

  // methods
  public void shiftGears(int gear) {
    this.gear = gear;
  }

  public void applyBreak(int decrement) {
    this.speed -= decrement;
  }

  public void speedUP(int increment) {
    this.speed += increment;
  }

  // override class toString() method
  @Override
  public String toString() {
    return ("No of gears are " + this.gear + "\n" + "Speed of bicycle is " + this.speed);
  }
}
