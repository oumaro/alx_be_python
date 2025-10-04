
#!/usr/bin/env python3
"""
This module defines the BankAccount class.
"""

class BankAccount:
    """
    A class to represent a simple bank account.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float, optional): The starting balance for the account.
                                              Defaults to 0.
        """
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """
        Adds a specified amount to the account balance.

        Args:
            amount (float): The amount to be deposited.
        """
        if amount > 0:
            self.account_balance += amount

    def withdraw(self, amount):
        """
        Deducts an amount from the account balance if funds are sufficient.

        Args:
            amount (float): The amount to be withdrawn.

        Returns:
            bool: True if the withdrawal was successful, False otherwise.
        """
        if 0 < amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")
