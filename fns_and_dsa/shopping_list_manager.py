# This script manages a shopping list using a Python list and a continuous menu loop.

def display_menu():
    """Prints the main menu options to the console."""
    print("\n--- Shopping List Manager ---")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    print("----------------------------")

def main():
    """Main function to run the shopping list application."""
    shopping_list = []
    
    # Main application loop
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Add Item functionality
            item = input("Enter the item to add: ").strip()
            if item:
                shopping_list.append(item)
                print(f"'{item}' has been added to the list.")
            else:
                print("Item name cannot be empty.")
            
        elif choice == '2':
            # Remove Item functionality
            if not shopping_list:
                print("The list is currently empty. Nothing to remove.")
                continue

            item_to_remove = input("Enter the item to remove: ").strip()
            
            # Check if the item is in the list before attempting to remove it
            if item_to_remove in shopping_list:
                shopping_list.remove(item_to_remove)
                print(f"'{item_to_remove}' has been removed from the list.")
            else:
                print(f"Error: '{item_to_remove}' not found in the list.")
            
        elif choice == '3':
            # View List functionality
            print("\n*** Current Shopping List ***")
            if not shopping_list:
                print("The list is empty!")
            else:
                # Use a for loop with enumerate for clean, numbered output
                for index, item in enumerate(shopping_list, 1):
                    print(f"{index}. {item}")
            print("***************************")
            
        elif choice == '4':
            # Exit functionality
            print("Goodbye! Your final list contains the following items:")
            print(shopping_list)
            break
            
        else:
            # Handle invalid menu choice
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()