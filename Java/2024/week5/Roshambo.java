
/*
 Filename: Roshambo.java
 Author: Mikhail Zubko
 Created: 2024/09/20
 Purpose: 
*/
import javax.swing.JOptionPane;
import java.util.Random;

public class Roshambo {
  static void showWindow(String usr, String comp, int result) {
    // TODO: Show message window
    String message = "You picked " + usr + "\nComputer picked " + comp + "\n";
    String title;
    if (result == 0) {
      title = "Tie";
    } else if (result == 1) {
      title = "You win!";
    } else {
      title = "You lose.";
    }
    message += title;
    JOptionPane.showConfirmDialog(null, message, title, JOptionPane.DEFAULT_OPTION,
        JOptionPane.INFORMATION_MESSAGE);
  }

  public static void main(String[] args) {
    // TODO: Define variable
    final int lowNum = 1;
    final int topNum = 6;
    int usrNum;
    int rndNum;
    String[] items = { "Rock", "Paper", "Scissors", "Spock", "Lizard" };
    String rules = """
        Rules:
        - Scissors cut paper
        - Paper covers rock
        - Rock crushes lizard
        - Lizard poisons Spock
        - Spock smashes scissors
        - Scissors decapitate lizard
        - Lizard eats paper
        - Paper disproves Spock
        - Spock vaporizes rock
        - Rock crushes scissors
            """;
    String question = """

        Type one of the following numbers
        1 - Rock
        2 - Paper
        3 - Scissors
        4 - Spock
        5 - Lizard
            """;
    Random rnd = new Random();
    // TODO: Start game loop
    while (true) {
      try {
        // TODO: Show welcome window and get input.
        usrNum = Integer
            .parseInt(JOptionPane.showInputDialog(null, rules + question, "Roshambo",
                JOptionPane.INFORMATION_MESSAGE));
      } catch (Exception e) {
        // if user input incorrect or empty, finish the game
        break;
      }
      // TODO: If user input < 1 or > 5 finish the game
      if (usrNum < 1 || usrNum > 5) {
        break;
      }
      rndNum = rnd.nextInt(lowNum, topNum);
      // TODO: Tie condition
      if (rndNum == usrNum) {
        showWindow(items[usrNum - 1], items[rndNum - 1], 0);
        // TODO: Win condition
        // instead of nested conditions I did some math analyzis and found a formula.
      } else if ((5 - ((rndNum + 5 - usrNum) % 5)) % 2 == 1) {
        showWindow(items[usrNum - 1], items[rndNum - 1], 1);
        // TODO: Lose condition
      } else {
        showWindow(items[usrNum - 1], items[rndNum - 1], 2);
      }
    }
  }
}
