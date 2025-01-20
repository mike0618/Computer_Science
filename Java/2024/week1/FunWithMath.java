import java.util.Scanner;

public class FunWithMath {
   public static void main(String[] args) {
    // TODO: Declare variables, constants or objects

    // TODO: Get input from user
    Scanner keyboard = new Scanner(System.in);
    System.out.print("Enter int: ");

    // TODO: Calculations
    int num = keyboard.nextInt();
    if (isEven(num) == 0){
        System.out.print("EVEN");
    }
    else{
        System.out.print("ODD");
    }

    // TODO: Display output
   keyboard.close();
   } 

   static int isEven(int value){

    return (value % 2);
   }
}
