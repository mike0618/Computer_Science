/*
 Filename: SandwichShop.java
 Author: Mikhail Zubko
 Created: 2024/12/01
 Purpose: 
*/

public class SandwichShop {
  public static void main(String[] args) {
    System.out.println("*** Welcome to Scout's Sandwich Shap ***");

    Sandwich sandwich1 = new Sandwich();
    Sandwich sandwich2 = new Sandwich("Roast Beef", "Croissant", 5.55);

    sandwich1.setMainIngredient("Tuna");
    sandwich1.setBreadType("Wheat");
    sandwich1.setPrice(4.99);

    System.out.println(sandwich1.toString());
    System.out.println(sandwich2.toString());
  }
}
