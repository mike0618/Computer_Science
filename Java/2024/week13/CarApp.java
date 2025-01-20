/*
 Filename: CarApp.java
 Author: Mikhail Zubko
 Created: 2024/11/16
 Purpose: 
*/

import java.util.Scanner;

public class CarApp {
  protected static int getInput(Scanner keyboard, String prompt) {
    int result;
    while (true) {
      try {
        System.out.print(prompt);
        result = keyboard.nextInt();
        if (result < 1) {
          System.out.println("Enter a positive number.");
          continue;
        }
        return result;
      } catch (Exception e) {
        System.out.println("Enter a whole number.");
        keyboard.nextLine();
      }
    }
  }

  public static void main(String[] args) {
    Scanner keyboard = new Scanner(System.in);
    String model;
    String color;
    int mpg;
    int year;

    System.out.print("Enter the model of the car: ");
    model = keyboard.nextLine();
    System.out.print("Enter the color of the car: ");
    color = keyboard.nextLine();
    year = getInput(keyboard, "Enter the year of the car: ");
    mpg = getInput(keyboard, "Enter the gas usage (miles per gallon): ");

    Car mycar = new Car(model, color, mpg, year);

    mycar.getInfo();

    System.out.println("Trying to drive 50 miles not starting the engine...");
    mycar.drive(50);

    System.out.println("Trying to start the engine...");
    mycar.startEngine();

    System.out.println("Adding 10 gallons of gas...");
    mycar.addGas(10);

    System.out.println("Starting the engine...");
    mycar.startEngine();

    System.out.println("Trying to drive 50 miles...");
    mycar.drive(50);
    System.out.printf("Still have %.1f gallons of gas.\n", mycar.getGasLevel());

    System.out.println("Trying to drive 200 miles...");
    mycar.drive(200);

    System.out.println("Adding 5 gallons of gas...");
    mycar.addGas(5);

    System.out.println("Trying to drive 200 miles...");
    mycar.drive(200);

    System.out.println("Stopping the engine...");
    mycar.stopEngine();

  }
}
