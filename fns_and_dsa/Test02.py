from datetime import datetime, timedelta

def display_current_datetime():
    """
    Displays the current date and time in 'YYYY-MM-DD HH:MM:SS' format.
    """
    current_date = datetime.now()
    print(f"Current Date and Time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")

def calculate_future_date():
    """
    Prompts the user for a number of days, calculates a future date based on
    the current date, and prints it in 'YYYY-MM-DD' format.
    """
    try:
        days_to_add = int(input("Enter the number of days to add: "))
        if days_to_add < 0:
            print("Please enter a non-negative number of days.")
            return

        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        print(f"Future Date ({days_to_add} days from now): {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter an integer for the number of days.")

def main():
    """
    Main function to run the datetime operations.
    """
    print("--- Date and Time Explorer ---")
    display_current_datetime()
    print("\n--- Calculating Future Date ---")
    calculate_future_date()
    print("\nExploration complete, Kay!")

if __name__ == "__main__":
    main()