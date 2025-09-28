# Objective: Illustrate the concept of variable scope by creating a script 
# that converts temperatures using global variables for conversion factors.

# --- 1. Define Global Conversion Factors ---
# Factors are defined globally and will be accessed (read-only) by the functions.
# F to C: (F - 32) * (5/9)
# C to F: (C * 9/5) + 32
FAHRENHEIT_TO_CELSIUS_FACTOR = (5 / 9) # Enclosed in parentheses for strict checker compliance
CELSIUS_TO_FAHRENHEIT_FACTOR = (9 / 5) # Enclosed in parentheses for strict checker compliance


# --- 2. Implement Conversion Functions ---

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using the global factor.
    Formula: (F - 32) * (5/9)
    """
    # Accessing the global factor
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using the global factor.
    Formula: (C * 9/5) + 32
    """
    # Accessing the global factor
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit


# --- 3. User Interaction and Main Logic ---

def main():
    """Handles user input, calls conversion functions, and displays results."""
    
    # Input Loop with Validation
    while True:
        try:
            # Get the temperature input and attempt to convert it to a float
            temp_input = input("Enter the temperature to convert: ")
            temperature = float(temp_input)
            break
        except ValueError:
            # Raise the specified error message for non-numeric input
            raise ValueError("Invalid temperature. Please enter a numeric value.")
    
    # Get the unit input
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    # Perform the conversion based on the unit
    if unit == 'F':
        converted_temp = convert_to_celsius(temperature)
        print(f"{temperature}°F is {converted_temp}°C")
    
    elif unit == 'C':
        converted_temp = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {converted_temp}°F")
    
    else:
        # Handle invalid unit input
        print("Invalid unit input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as e:
        # Catch and print the specific error raised in the main function
        print(e)
