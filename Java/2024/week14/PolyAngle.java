/*
 Filename: PolyAngle.java
 Author: Mikhail Zubko
 Created: 2024/11/23
 Purpose: 
*/

public class PolyAngle {
  // Define attributes
  private int sides;
  private double length;
  private String shape;
  private double intAngle;
  private double extAngle;
  private double perimeter;
  private String[] polygons = {
      "Triangle",
      "Square",
      "Pentagon",
      "Hexagon",
      "Heptagon",
      "Octagon",
      "Nonagon",
      "Decagon"
  };

  // Constructor with parameters
  public PolyAngle(int sides, double length) {
    this.sides = sides;
    this.length = length;
    Calculate();
  }

  private void Calculate() {
    int index = this.sides - 3;
    if (index < this.polygons.length) {
      this.shape = this.polygons[index];
    } else {
      this.shape = this.sides + "-sided polygon";
    }
    this.extAngle = 360.0d / this.sides; // explicit double to get double as result
    this.intAngle = 180 - this.extAngle;
    this.perimeter = this.length * this.sides;
  }

  // Override toString method
  @Override
  public String toString() {
    return String.format(
        "Results:\nShape: %s\nNumber of sides: %d\nSide length: %.2f units\nInterior angle: %.2f degrees\nExterior angle: %.2f degrees\nPerimeter: %.2f units",
        this.shape, this.sides, this.length, this.intAngle, this.extAngle, this.perimeter);
  }
}
