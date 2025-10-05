def safe_divide(numerator, denominator):
    try:
        num = float(numerator)
        num1 = float(denominator)        
        result= num / num1

        return f"The result of the division is {result}"
        

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        return "Error: Please enter number value only."
    
safe_divide("ah", 5)