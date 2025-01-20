
// A single line comment
/*
 * 
 * 
 */
// TODO: import Scanner to get keyboard input
import java.util.Scanner;

public class MultiplyNumbers {
  public static void main(String[] args) {

    Scanner keyboard = new Scanner(System.in);

    // TODO: define 2 double variables to save user input
    double firstNum;
    double secondNum;

    // TODO: get user input and save it to the variables
    System.out.print("Enter first number: ");
    firstNum = keyboard.nextDouble();
    System.out.print("Enter second number: ");
    secondNum = keyboard.nextDouble();

    // TODO: Print a result to the console
    System.out.println("Result: " + firstNum * secondNum);

    keyboard.close();
  }
}
