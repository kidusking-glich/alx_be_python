def perform_operation(num1, num2, operation):
    if operation == "add":
        result = num1 + num2
    elif operation == "subtract":
        result = num1 - num2
    elif operation == "multiply":
        result = num1 * num2
    elif operation == "divide":
        if num2 > 0:
            result = num1 / num2
        elif num2 == 0:
            return "Error: Cannot divide by zero."

    else:
        return "Error: Invalid operation."
    return result



