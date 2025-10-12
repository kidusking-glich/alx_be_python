class Calculator:
    """
    A class demonstrating the use of static methods and class methods.
    """
    # Class attribute accessible by the class method
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method: Returns the sum of two numbers.
        It does not access class or instance state.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method: Returns the product of two numbers.
        It accesses the class attribute via the 'cls' parameter.
        """
        # Accessing the class attribute using the 'cls' parameter
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

# --- End of Calculator Class ---
