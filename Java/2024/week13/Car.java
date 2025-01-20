/*
 Filename: Car.java
 Author: Mikhail Zubko
 Created: 2024/11/16
 Purpose: 
*/

public class Car {
  // Define attributes
  private String model;
  private String color;
  private int milesPerGallon;
  private int year;
  private boolean isRunning;
  private double gasLevel;

  // Constructor with parameters
  public Car(String model, String color, int mpg, int year) {
    this.model = model;
    this.color = color;
    this.milesPerGallon = mpg;
    this.year = year;
    this.isRunning = false;
    this.gasLevel = 0.0d;
  }

  // Getters and Setters
  public void getInfo() {
    System.out.println("--- Car Details:");
    System.out.println("Model: " + this.model);
    System.out.println("Color: " + this.color);
    System.out.println("MPG: " + this.milesPerGallon + " mi/Gallon");
    System.out.println("Year: " + this.year);
  }

  public boolean isEngineRunning() {
    return this.isRunning;
  }

  public double getGasLevel() {
    return this.gasLevel;
  }

  // Methods
  public void startEngine() {
    if (this.gasLevel > 0) {
      this.isRunning = true;
      System.out.println("--- Engine started.");
    } else {
      System.out.println("--- The gas tank is empty.");
    }
  }

  public void stopEngine() {
    this.isRunning = false;
    System.out.println("--- Engine stopped.");
  }

  public boolean drive(int miles) {
    double needGas;
    if (!this.isRunning) {
      System.out.println("--- Start the engine before driving.");
      return false;
    }
    needGas = (double) miles / this.milesPerGallon;
    if (needGas > this.gasLevel) {
      System.out.println("--- Not enough gas to drive " + miles + " miles.\nAdd more gas.");
      return false;
    }
    System.out.println("--- Driving " + miles + " miles.");
    this.gasLevel -= needGas;
    return true;
  }

  public void addGas(int gallons) {
    this.gasLevel += gallons;
    System.out.println("--- " + gallons + " gallons of gas added.");
  }

}
