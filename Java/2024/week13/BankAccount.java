/*
 Filename: BankAccount.java
 Author: Mikhail Zubko
 Created: 2024/11/16
 Purpose: 
*/

public class BankAccount {
  private String owner;
  private int balance;

  public BankAccount(String owner) {
    this(owner, 0);
  }

  public BankAccount(String owner, int balance) {
    this.owner = owner;
    this.balance = balance;
  }

  public void deposit(int amount) {
    if (amount > 0) {
      this.balance += amount;
    } else {
      System.out.println("Amount to deposit must be greater than 0");
    }
  }

  public void withdraw(int amount) {
    if (amount > 0 && amount <= this.balance) {
      this.balance -= amount;
    } else {
      System.out.println("The amount to deposit must be greater that 0 and less than your balance.");
    }
  }

  public String getOwner() {
    return this.owner;
  }

  public int getBalance() {
    return this.balance;
  }
}
