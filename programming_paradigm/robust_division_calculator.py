def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        num1 = float(denominator)        
        result= num / num1

        return f"The result of the division is {result}"
        

    
    except ValueError:
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except Exception as e:
        # Catch any other unexpected errors (good practice)
        return f"An unexpected error occurred: {e}"

safe_divide("he", 10)
