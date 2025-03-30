
/*
 Filename: FredsFileChallenge.java
 Author: Mikhail Zubko
 Created: 2025/03/27
 Purpose: 
*/
//imports
import java.io.FileWriter;
import java.io.IOException;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;
import java.io.File;

public class FredsFileChallenge {
  public static void main(String[] args) {
    try {
      // define input file, fileWriter, PrintWriter, Scanner and input string
      String fileName = "input.txt";
      FileWriter fileWriter = new FileWriter(fileName, false);
      PrintWriter pw = new PrintWriter(fileWriter);
      Scanner kb = new Scanner(System.in);
      String input;
      // print title
      System.out.println("----------- Fred's File Challenge ------------");
      System.out.println("Enter lines of text or numbers ('done' to finish):");
      // game loop
      while (true) {
        input = kb.nextLine();
        // loop exit condition
        if (input.equals("done")) {
          pw.close();
          kb.close();
          break;
        }
        pw.println(input);
      }
      // print results
      File infile = new File(fileName);
      Scanner f = new Scanner(infile);
      System.out.println("\nContents of " + fileName + ":");
      while (f.hasNextLine()) {
        System.out.println(f.nextLine());
      }
      f.close();
    } catch (FileNotFoundException ex) {
      System.out.println(ex.getMessage() + "File doesn't exist.'");
    } catch (IOException ex) {
      System.out.println(ex.getMessage() + "Couldn't write to the file!");
    }
  }
}
