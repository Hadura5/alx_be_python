class BankAccount:
    def __init__(self, initial_balance=0):
       
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
        
        print(f"Current Balance: ${self.account_balance:.2f}")



main-0.py

import sys
from bank_account import BankAccount


def main():
    account = BankAccount(100) 


    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)