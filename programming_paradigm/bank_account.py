class BankAccount:
    def __init__(self, initial_balance = 0):
        self.acount_balance = initial_balance
    def deposit (self, amount):
        if amount > 0:
            self.acount_balance += amount
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount):
        if amount > 0 and self.acount_balance >= amount:
            self.acount_balance -= amount
            return True
        else:
            return False
        
    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")
    def safe_divide(numerator, denominator):
        try:
            # Convert to float, handle non-numeric input
            num = float(numerator)
            den = float(denominator)
            
            # Handle division by zero
            if den == 0:
                return "Error: Cannot divide by zero."
            
            # Perform division
            result = num / den
            return f"The result of the division is {result}"
        
        except ValueError:
            return "Error: Please enter numeric values only."
        except ZeroDivisionError:
            return "Error: Cannot divide by zero."  # Redundant but explicit
    

        