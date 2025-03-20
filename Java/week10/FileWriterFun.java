/*
 Filename: FileWriterFun.java
 Author: Mikhail Zubko
 Created: 2025/03/19
 Purpose: 
*/

import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public class FileWriterFun {
  public static void main(String[] args) {
    String fileName = "rockstart.txt";
    writeFile(fileName);
  }

  private static void writeFile(String fileName) {
    try {
      // create Filewriter object to open OS file handle
      // false overwrites the file, true appends
      FileWriter fileWriter = new FileWriter(fileName, false);
      // print text to file
      PrintWriter pw = new PrintWriter(fileWriter);
      // print to file
      pw.println("Dave Grusin");
      pw.println("Journey");
      pw.println("Toto");

      pw.close();
      System.out.println("File written successfully.");
    } catch (FileNotFoundException ex) {
      System.out.println(ex.getMessage() + "File doesn't exist.'");
    } catch (IOException ex) {
      System.out.println(ex.getMessage() + "Couldn't write to the file!");
    }
  }
}
