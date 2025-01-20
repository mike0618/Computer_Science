public class Sandwich {
  // Parameters
  private String mainIngredient;
  private String breadType;
  private Double price;

  // Constructors
  public Sandwich() {
  }

  public Sandwich(String mainIngredient, String breadType, Double price) {
    this.mainIngredient = mainIngredient;
    this.breadType = breadType;
    this.price = price;
  }

  // Setters
  public void setMainIngredient(String mainIngredient) {
    this.mainIngredient = mainIngredient;
  }

  public void setBreadType(String breadType) {
    this.breadType = breadType;
  }

  public void setPrice(Double price) {
    this.price = price;
  }

  // Getters
  public String getMainIngredient() {
    return this.mainIngredient;
  }

  public String getBreadType() {
    return this.breadType;
  }

  public Double getPrice() {
    return this.price;
  }

  @Override
  public String toString() {
    String msg = "You ordered a ";
    msg += this.getMainIngredient();
    msg += " sandwich on ";
    msg += this.getBreadType();
    msg += " bread.\nThe price is: $";
    msg += this.getPrice();
    return msg;
  }
}
