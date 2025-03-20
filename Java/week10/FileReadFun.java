/*
 Filename: FileReadFun.java
 Author: Mikhail Zubko
 Created: 2025/03/19
 Purpose: 
*/

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class FileReadFun {
  public static void main(String[] args) {
    try {
      // open file handle
      File infile = new File("example.txt");
      // read the input from file
      Scanner input = new Scanner(infile);
      // read line by line while still lines
      while (input.hasNextLine()) {
        String data = input.nextLine();
        System.out.println(data);
      }
      input.close();
    } catch (FileNotFoundException ex) {
      System.out.println("Can't find file!");
      System.out.println(ex.getMessage());
    }
  }
}
