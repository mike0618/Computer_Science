/*
 Filename: BankAccountApp.java
 Author: Mikhail Zubko
 Created: 2024/11/16
 Purpose: 
*/

public class BankAccountApp {
  public static void main(String[] args) {
    BankAccount myAccount = new BankAccount("Mike Zubko", 5555);
    BankAccount bobsAccount = new BankAccount("Bob Robinson");

    bobsAccount.deposit(500);
    System.out.println("Owner: " + bobsAccount.getOwner());
    System.out.println("Balance: " + bobsAccount.getBalance());

    bobsAccount.withdraw(1000);// warning
    System.out.println("Owner: " + bobsAccount.getOwner());
    System.out.println("Balance: " + bobsAccount.getBalance());
    System.out.println();

    System.out.println("Owner: " + myAccount.getOwner());
    System.out.println("Balance: " + myAccount.getBalance());
    System.out.println();

    System.out.println("Deposit 1000?");
    myAccount.deposit(1000);
    System.out.println("Owner: " + myAccount.getOwner());
    System.out.println("Balance: " + myAccount.getBalance());
  }
}
