# temp_conversion_tool.py

# ============================
# Global Conversion Factors
# ============================
c = 0
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = c * 9 / 5
FREEZING_POINT_F = 32  # offset used in conversions



# ============================
# Conversion Functions
# ============================
def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    return (fahrenheit - FREEZING_POINT_F) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + FREEZING_POINT_F


# ============================
# User Interaction
# ============================
def main():
    temp_input = input("Enter the temperature to convert: ").strip()
    # Validate temperature input and raise the exact error if invalid
    try:
        temperature = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "F":
        result = convert_to_celsius(temperature)
        print(f"{temperature}°F is {result}°C")
    elif unit == "C":
        result = convert_to_fahrenheit(temperature)
        print(f"{temperature}°C is {result}°F")
    else:
        raise ValueError("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")


if __name__ == "__main__":
    main()
