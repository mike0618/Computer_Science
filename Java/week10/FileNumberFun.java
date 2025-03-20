
/*
 Filename: FileNumberFun.java
 Author: Mikhail Zubko
 Created: 2025/03/19
 Purpose: 
*/
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.NoSuchElementException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class FileNumberFun {
  public static void main(String[] args) {
    String numbers = "numbers.txt";
    String twoTimes = "twotimes.txt";
    try {
      File inFile = new File(numbers);
      // filewriter object set to owerwrite
      FileWriter fw = new FileWriter(twoTimes, false);
      // printwriter writes text to file
      PrintWriter pw = new PrintWriter(fw);
      Scanner input = new Scanner(inFile);
      int inNum;
      int outNum;
      while (input.hasNextInt()) {
        inNum = input.nextInt();
        outNum = inNum * 2;
        // write to file
        pw.println("Input: " + inNum + " * 2 = " + outNum + " written to file.");
      }
      input.close();
      pw.close();
    } catch (FileNotFoundException ex) {
      System.out.println(ex.getMessage() + "File doesn't exist.'");
    } catch (IOException ex) {
      System.out.println(ex.getMessage() + "Couldn't write to the file!");
    }
  }
}
