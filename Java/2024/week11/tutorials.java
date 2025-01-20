/*
 Filename: tutorials.java
 Author: Mikhail Zubko
 Created: 2024/11/01
 Purpose: 
*/

import java.util.Arrays;
import java.util.Random;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class tutorials {
  static void ArrayAccessLoops() {
    // declare constatnt for array size
    final int SIZE = 4;
    int[] counts = new int[SIZE];
    // traversal with a for loop
    System.out.println("\nFor loop with original empty array");
    for (int i = 0; i < SIZE; i++) {
      System.out.print(counts[i] + " ");
    }
    // access individual array elements
    counts[0] = 7;
    counts[1] = counts[0] * 2;
    counts[2]++;
    counts[3] -= 60;
    // traversal with a while loop
    System.out.println("\nWhile loop");
    // counter for while loop
    int j = 0;
    while (j < SIZE) {
      System.out.print(counts[j] + " ");
      j++;
    }
    // traversal with a for each loop
    System.out.println("\nFor each loop");
    // for each element in the array
    for (int count : counts) {
      System.out.print(count + " ");
    }
    // multiply each element by 2
    System.out.println("\nFor loop multiply each element by 2");
    for (int i = 0; i < SIZE; i++) {
      int countsTwo = counts[i] * 2;
      System.out.print(countsTwo + " ");
    }
  }

  // print the elements of an array
  public static void printArray(int[] a) {
    System.out.print("{" + a[0]);
    for (int i = 1; i < a.length; i++) {
      System.out.print(", " + a[i]);
    }
    System.out.println("}");
  }

  // return the index of the target in the array, or -1 if not found.
  public static int search(double[] array, double target) {
    for (int i = 0; i < array.length; i++) {
      if (array[i] == target) {
        return i;
      }
    }
    return -1; // not found
  }

  // return the total of the elements in an array
  public static double sum(double[] array) {
    double total = 0.0;
    for (int i = 0; i < array.length; i++) {
      total += array[i];
    }
    return total;
  }

  static void ArrayFunctions() {
    int[] array = { 1, 2, 3, 4 };
    System.out.println("Print Array using function with array argument");
    printArray(array);
    System.out.println("Print Array's memory address");
    System.out.println(array);// print array as an object
    System.out.println("Print Array using Arrays class method");
    System.out.println(Arrays.toString(array));
    // copying an array is done by copying the elements from one array to another
    double[] a = { 1.0, 2.0, 3.0 };
    double[] b = new double[a.length];
    System.out.println("Print copy b of Array a");
    for (int i = 0; i < a.length; i++) {
      b[i] = a[i];
      System.out.print(b[i] + " ");
    }
    System.out.println("\nPrint copy c of Array a");
    // copying with Arrays class method
    double[] c = Arrays.copyOf(a, a.length);
    for (double i : c) {
      System.out.print(i + " ");
    }
    // search an array using a method with parameters
    int index = search(a, 2.0);
    System.out.println("\nindex = " + index);
    // reduce
    double total = sum(a);
    System.out.println("total = " + total);
  }

  // fill and return an array of random integers
  public static int[] randomArray(int size) {
    // create random object
    Random random = new Random();
    int[] randomNumbersArray = new int[size];
    for (int i = 0; i < randomNumbersArray.length; i++) {
      // get random int from 1 to 99
      randomNumbersArray[i] = random.nextInt(1, 100);
    }
    return randomNumbersArray;
  }

  // print the elements of an array
  public static void printArray2(int[] a) {
    for (int i = 0; i < a.length - 1; i++) {
      System.out.print(a[i] + ", ");
    }
    System.out.println(a[a.length - 1]);// print the last element
  }

  static void RandomArray() {
    final int SIZE = 10;
    int[] array = randomArray(SIZE);
    printArray2(array);
  }

  // display ArrayList
  static void displayArrayList(ArrayList<String> names) {
    int size = names.size(); // get size of ArrayList
    System.out.println("List size is: " + size);
    for (int x = 0; x < size; x++) {
      System.out.print("- " + names.get(x) + " -");
    }
    System.out.println();
  }

  static void ArrayListFun() {
    // create array list
    ArrayList<String> namesList = new ArrayList<>();
    // add elements to the ArrayList
    namesList.add("John");
    namesList.add("Kyle");
    namesList.add("Zorro");
    namesList.add("Amanda");
    namesList.add("Wendy");
    System.out.println("Original ArrayList");
    displayArrayList(namesList);
    // get first element in ArrayList
    String nameZero = namesList.get(0);
    System.out.println("First name in list: " + nameZero);
    // remove Amanda
    namesList.remove("Amanda");
    // add Floyd at the 2nd position
    namesList.add(2, "Floyd");
    // change the furst item to Lucy
    namesList.set(0, "Lucy");
    System.out.println("Modified ArrayList");
    displayArrayList(namesList);
    // use Collections library to sort the ArrayList
    Collections.sort(namesList);
    System.out.println("Sorted ArrayList");
    for (String name : namesList) {
      System.out.print("- " + name + " -");
    }
    System.out.println();
  }

  static void TwoDArray() {
    int[][] values = {
        { 10, 20, 30 },
        { 40, 50, 60 },
        { 70, 80, 90 },
        { 11, 21, 31 },
    };
    // iterate through row one element at a time
    for (int row = 0; row < values.length; row++) {
      // iterate through array one row at a time
      for (int col = 0; col < values[row].length; col++) {
        System.out.print(values[row][col] + " ");
      }
      System.out.println();
    }
  }

  static int sumArray(int[] elements) {
    int sum = 0;
    for (int element : elements) {
      sum += element;
    }
    return sum;
  }

  static int getInt(Scanner input, boolean checkPositive) {
    int num;
    while (true) {
      try {
        num = input.nextInt();
        if (checkPositive) {
          if (num > 0) {
            return num;
          }
          System.out.println("Enter a positive number");
          continue;
        }
        return num;
      } catch (Exception e) {
        System.out.println("Enter a whole number");
        input.nextLine();

      }
    }
  }

  public static void main(String[] args) {
    System.out.println("Tutorial 6.1: Accessing and looping Arrays");
    ArrayAccessLoops();
    System.out.println("\n\nTutorial 6.2: Arrays with Methods\n");
    ArrayFunctions();
    System.out.println("\nTutorial 6.3: Random numbers method\n");
    RandomArray();
    System.out.println("\nTutorial 6.4: ArrayList Fun\n");
    ArrayListFun();
    System.out.println("\nTutorial 6.5: 2D Arrays\n");
    TwoDArray();
    System.out.println("\nAssignment 1: Sum of Array Elements\n");
    Scanner input = new Scanner(System.in);
    int size;
    int sum;
    System.out.print("Enter the number of elements in the array: ");
    size = getInt(input, true);
    int[] elements = new int[size];
    System.out.println("Enter the elements of the array: ");
    for (int i = 0; i < size; i++) {
      elements[i] = getInt(input, false);
    }
    sum = sumArray(elements);
    System.out.println("The sum of the array elements is: " + sum);

  }
}
