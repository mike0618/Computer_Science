// A single line comment
/*
 * 
 * 
 */

import java.util.Scanner;

public class MPKInput {
    public static void main(String[] args) {

        Scanner keyboard = new Scanner(System.in);

        final double KM_PER_MILE = 1.609;

        double miles;
        double kilometers;

        System.out.print("Enter miles: ");
        miles = keyboard.nextDouble();

        kilometers = miles * KM_PER_MILE;

        // Print a string literal to the console
        System.out.println(miles + " miles = " + kilometers + " kilometers.");

        keyboard.close();
    }
}
