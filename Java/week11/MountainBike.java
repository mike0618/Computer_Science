/*
 Filename: MountainBike.java
 Author: Mikhail Zubko
 Created: 2025/03/27
 Purpose: 
*/

// derived/child class
class MountainBike extends Bicycle {
  // add more fields
  private int seatHeight;

  // constructor
  public MountainBike(
      int gear,
      int speed,
      int seatHeight) {
    // base class constructor
    super(gear, speed);
    this.seatHeight = seatHeight;
  }

  // add more methods
  public void setHeight(int newVal) {
    this.seatHeight = newVal;
  }

  // override class toString() method
  @Override
  public String toString() {
    return ("MountainBike " + super.toString() + "\nSeat height is " + this.seatHeight);
  }
}
