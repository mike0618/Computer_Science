
/*
 Filename: PigLatin.java
 Author: Mikhail Zubko
 Created: 2025/01/27
 Purpose: 
*/
import javax.swing.JOptionPane;

public class PigLatin {
  public static void main(String[] args) {
    final String VOWELS = "aeiouAEIOU";
    String word = "";
    String pigword = "";
    while (true) {
      word = JOptionPane.showInputDialog(null, "Enter a word\nto be converted to Pig Latin", "Input a Word",
          JOptionPane.QUESTION_MESSAGE);
      if (word == null) {
        break; // cancelled
      }
      if (word.isBlank()) {
        continue; // empty input
      }
      if (VOWELS.indexOf(word.charAt(0)) != -1) {
        pigword = word + "way"; // if the word starts with vowel
      } else { // if the word starts with consonant
        for (int i = 0; i < word.length(); i++) {
          if (VOWELS.indexOf(word.charAt(i)) != -1) {
            // find the index of vowel and use it to split the word
            pigword = word.substring(i) + word.substring(0, i) + "ay";
            break;
          } else if (i == word.length() - 1) {
            pigword = word + "ay"; // if no vowels in the word
          }
        }
      }
      JOptionPane.showMessageDialog(null, "Pig Latin version:\n" + pigword);
    }
  }
}
