class ScentedCandle extends Candle {
  private double height;
  private int price_per_inch = 3;

  public void set_height(double height) {
    this.height = height;
    this.price = height * this.price_per_inch;
  }

  public double get_height() {
    return this.height;
  }

  @Override
  public String toString() {
    return ("The " + this.get_height() + " inch scented " + this.get_color() + " candle costs $" + this.get_price());
  }
}
