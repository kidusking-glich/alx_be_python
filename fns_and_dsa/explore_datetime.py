# Objective: Familiarize yourself with Python’s datetime module.
# Task: Display current date/time and calculate a future date.

from datetime import datetime, timedelta

def display_current_datetime():
    """
    Part 1: Gets and prints the current date and time in a readable format.
    """
    # Get the current date and time
    current_date = datetime.now()
    
    # Format and print the current date and time
    # Format: YYYY-MM-DD HH:MM:SS
    formatted_datetime = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_datetime}")
    
    # Return the current_date object for use in Part 2
    return current_date

def calculate_future_date(current_date):
    """
    Part 2: Prompts the user for a number of days and calculates the future date.
    
    Parameters:
        current_date (datetime): The starting date object from which to calculate.
    """
    while True:
        try:
            # Prompt user for the number of days
            days_to_add = int(input("Enter the number of days to add to the current date: "))
            
            # Use timedelta to calculate the future date
            time_change = timedelta(days=days_to_add)
            future_date = current_date + time_change
            
            # Print the future date in the format "YYYY-MM-DD"
            formatted_future_date = future_date.strftime("%Y-%m-%d")
            print(f"Future date: {formatted_future_date}")
            break # Exit loop on successful calculation
            
        except ValueError:
            # Handle non-integer input
            print("Invalid input. Please enter a whole number for the days.")

if __name__ == "__main__":
    # Part 1: Display current date and get the datetime object
    current_date = display_current_datetime()
    
    # Part 2: Calculate and display the future date
    calculate_future_date(current_date)
