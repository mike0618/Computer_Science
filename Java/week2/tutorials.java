/*
 Filename: tutorials.java
 Author: Mikhail Zubko
 Created: 2025/01/22
 Purpose: 
*/

import java.util.Scanner;

public class tutorials {
  static void charMethods(Scanner kb) {
    char userChar;
    System.out.print("Enter a single character: ");
    userChar = kb.next().charAt(0);
    // use the result directly
    if (Character.isLetter(userChar)) {
      System.out.println(userChar + " is a letter.");
    } else {
      System.out.println(userChar + " is not a letter.");
    }
    // store in a var and then use
    boolean isDigitRes = Character.isDigit(userChar);
    if (isDigitRes) {
      System.out.println(userChar + " is a digit.");
    } else {
      System.out.println(userChar + " is not a digit.");
    }
    boolean isLetterOrDigitRes = Character.isLetterOrDigit(userChar);
    System.out.println(userChar + " is a letter or a digit: " + isLetterOrDigitRes);
    if (Character.isUpperCase(userChar)) {
      System.out.println(userChar + " is uppercase.");
    } else {
      System.out.println(userChar + " is not uppercase.");
    }
    System.out.println(userChar + " converted to upper case is: " + Character.toUpperCase(userChar));
    System.out.println(userChar + " converted to lower case is: " + Character.toLowerCase(userChar));
  }

  static void stringMethods() {
    String name = "John Snow";
    String name2 = "John Snow";
    String name3 = "Johnny Depp";
    // Loop through the string
    for (int i = 0; i < name.length(); i++) {
      System.out.print(name.charAt(i) + " ");
    }
    System.out.println();
    // Check for equality
    if (name.equals(name2)) {
      System.out.println("Names are equal.");
    } else {
      System.out.println("Names are not equal.");
    }

    if (name.compareTo(name3) > 0) {
      System.out.println("name > name3");
    } else {
      System.out.println("name <= name3");
    }
    // Unicode
    char heartSybmol = '\u2764';
    char smileyFace = '\u263A';
    char coffeeCup = '\u2615';
    System.out.println("Java Unicode Tutorial");
    System.out.println("Feel " + heartSybmol + " and " + smileyFace);
    System.out.println("Grab a cup of " + coffeeCup + " and enjoy coding!");

    String myName = "Kermit the Frog";
    String upper = myName.toUpperCase();
    String lower = myName.toLowerCase();
    int whereIsF = myName.indexOf("F");
    // Slice starting at 11
    String lastName = myName.substring(11);
    // Slice using indexOf
    String lastNameFromIndex = myName.substring(whereIsF);
    System.out.println(myName);
    System.out.println("UPPER case: " + upper);
    System.out.println("lower case: " + lower);
    System.out.println("F is at index: " + whereIsF);
    System.out.println("Last name: " + lastName);
    System.out.println("Last name using index: " + lastNameFromIndex);
  }

  static void stringBuilderFun() {
    // Create a new StringBuilder object
    StringBuilder sb = new StringBuilder("John Snow");
    sb.append(" is awesome");
    System.out.println(sb);
    sb.insert(5, "Phillip ");// insert at index 5
    System.out.println(sb);
    sb.replace(21, 28, "amazing");// replace from 21 to 28
    System.out.println(sb);
    sb.delete(5, 13);
    System.out.println(sb);
    sb.replace(0, 4, "Dr.");// replace from 21 to 28
    System.out.println(sb);
  }

  public static void main(String[] args) {
    Scanner kb = new Scanner(System.in);
    charMethods(kb);
    kb.close();
    stringMethods();
    stringBuilderFun();
  }
}
