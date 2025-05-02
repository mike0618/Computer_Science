public class Candle {
  // Private fields
  private String color;
  private double height;
  protected double price;
  private int price_per_inch = 2;

  public String get_color() {
    return this.color;
  }

  public double get_height() {
    return this.height;
  }

  public double get_price() {
    return this.price;
  }

  public void set_color(String color) {
    this.color = color;
  }

  public void set_height(double height) {
    this.height = height;
    this.price = height * this.price_per_inch;
  }

  @Override
  public String toString() {
    return ("The " + this.get_height() + " inch " + this.get_color() + " candle costs $" + this.get_price());
  }
}
