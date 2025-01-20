
/*
 Filename: Roshambo.java
 Author: Mikhail Zubko
 Created: 2024/09/20
 Purpose: 
*/
import javax.swing.JOptionPane;
import java.util.Random;

public class Roshambo2 {
  static int showWindow(String usr, String comp, int result, int total, int w, int t, int l) {
    // TODO: Show message window
    String title;
    if (result == 0) {
      title = "Tie";
    } else if (result == 1) {
      title = "You win!";
    } else {
      title = "You lose.";
    }
    String message = "You picked " + usr + "\nComputer picked " + comp + "\n" + title + "\n\nTotal games: " + total
        + "\nWin games: " + w + "\nTie games: " + t + "\nLose games: " + l;
    return JOptionPane.showConfirmDialog(null, message, title, JOptionPane.YES_NO_OPTION,
        JOptionPane.INFORMATION_MESSAGE);

  }

  public static void main(String[] args) {
    // TODO: Define variable
    final int lowNum = 1;
    final int topNum = 6;
    int usrNum;
    int rndNum;
    int wins = 0;
    int total = 0;
    int tie = 0;
    int lose = 0;
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
      total++;
      // TODO: Tie condition
      if (rndNum == usrNum) {
        tie++;
        if (showWindow(items[usrNum - 1], items[rndNum - 1], 0, total, wins, tie, lose) == 1) {
          break;
        }
        // TODO: Win condition
        // instead of nested conditions I did some math analyzis and found a formula.
      } else if ((5 - ((rndNum + 5 - usrNum) % 5)) % 2 == 1) {
        wins++;
        if (showWindow(items[usrNum - 1], items[rndNum - 1], 1, total, wins, tie, lose) == 1) {
          break;
        }
        // TODO: Lose condition
      } else {
        lose++;
        if (showWindow(items[usrNum - 1], items[rndNum - 1], 2, total, wins, tie, lose) == 1) {
          break;
        }
      }
    }
  }
}
