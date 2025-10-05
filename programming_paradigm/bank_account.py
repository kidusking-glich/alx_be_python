# Objective: Define the BankAccount class for banking operations.

class BankAccount:
    """
    A simple bank account class to demonstrate OOP principles.
    Encapsulates account balance and provides methods for deposit,
    withdrawal, and balance display.
    """
    def __init__(self, initial_balance=0.0):
        # Initialize the account balance. Use a private-like attribute convention.
        # Fixed typo: using self._account_balance consistently.
        if initial_balance < 0:
            print("Warning: Initial balance cannot be negative. Setting to 0.")
            self._account_balance = 0.0
        else:
            self._account_balance = float(initial_balance)

    def deposit(self, amount: float):
        """Adds a positive amount to the account balance."""
        try:
            amount = float(amount)
            if amount > 0:
                self._account_balance += amount
            else:
                # Note: In a real app, you would raise an error here.
                print("Deposit amount must be positive.")
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")

    def withdraw(self, amount: float) -> bool:
        """
        Deducts a positive amount if funds are sufficient.
        Returns True on success, False otherwise.
        """
        try:
            amount = float(amount)
            if amount > 0 and self._account_balance >= amount:
                self._account_balance -= amount
                return True
            else:
                # Returns False if amount is negative or insufficient funds
                return False
        except ValueError:
            # Handle case where the amount passed is not convertible to float
            print("Invalid amount. Please enter a numeric value.")
            return False

    def display_balance(self):
        """Prints the current account balance."""
        print(f"Current Balance: ${self._account_balance:.2f}")
