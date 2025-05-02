/*
 Filename: DemoCandles.java
 Author: Mikhail Zubko
 Created: 2025/04/11
 Purpose: 
*/

public class DemoCandles {
  public static void main(String[] args) {
    System.out.println("+---------------------------------+");
    System.out.println("|  Welcome to Maya's Candle Shop  |");
    System.out.println("+---------------------------------+");
    Candle candle1 = new Candle();
    ScentedCandle candle2 = new ScentedCandle();
    candle1.set_height(6);
    candle1.set_color("pink");
    candle2.set_height(6);
    candle2.set_color("white");
    System.out.println(candle1);
    System.out.println(candle2);
  }
}
