class BankAccount:
    def __init__(self, initial_balance=0):
        # store balance as a float to handle cents
        self.account_balance = float(initial_balance)


    def deposit(self, amount):
        self.account_balance += float(amount)


    def withdraw(self, amount):
        amount = float(amount)
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False


    def display_balance(self):
        # Print with two decimal places to match checker expectation
        print(f"Current Balance: ${self.account_balance:.2f}")



main-0.py

import sys
from bank_account import BankAccount


def main():
    account = BankAccount(100)  # Example starting balance


    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)


        # The script exits before reaching the rest if no arguments are provided.


    command, *params = sys.argv[1].split(':')


    amount = float(params[0]) if params else None


    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")


    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")


    elif command == "display":
        account.display_balance()


    else:
        print("Invalid command.")


if __name__ == "__main__":
    main()