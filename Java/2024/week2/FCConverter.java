/*
 Filename: FahrenheitConverter.java
 Author: Mikhail Zubko
 Created: 08/29/24
 Purpose: Get Fahrenheit temperature as a float
 Calculate Celsius and Kelvin
*/

import java.text.DecimalFormat;
import java.util.Scanner;

public class FCConverter {
  public static void main(String[] args) {
    // TODO: Print creative program title
    System.out.println("-----------------------------");
    System.out.println("| Java Fahrenheit Converter |");
    System.out.println("-----------------------------");
    // TODO: Define scanner and variables
    Scanner keyboard = new Scanner(System.in);
    double celsius;
    double fahrenheit;
    double kelvin;
    // TODO: Get user Fahrenheit input
    System.out.print("Enter temperature in Fahrenheit : ");
    fahrenheit = keyboard.nextDouble();
    // TODO: Calculate Celsius C = (F - 32) x 5/9
    celsius = ((fahrenheit - 32) * 5) / 9;
    // TODO: Calculate Kelvin iK = (F - 32) x 5/9 + 273.15
    kelvin = ((fahrenheit - 32) * 5) / 9 + 273.15;
    // TODO: Print formatted results
    DecimalFormat df = new DecimalFormat("#.#");
    System.out.println("Temperature in Celsius: " + df.format(celsius));
    System.out.println("Temperature in Kelvin: " + df.format(kelvin));
    // TODO: Close the scanner object
    keyboard.close();
  }
}
