# temp_conversion_tool.py

# Define global variables for conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """
    Converts a temperature from Fahrenheit to Celsius using a global factor.
    """
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """
    Converts a temperature from Celsius to Fahrenheit using a global factor.
    """
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    """
    Main function to handle user interaction and temperature conversion.
    """
    try:
        # Prompt the user for temperature and unit
        temp_input = input("Enter the temperature value: ")
        temp_value = float(temp_input)
        
        unit_input = input("Enter the unit ('C' for Celsius, 'F' for Fahrenheit): ").strip().upper()

        # Perform conversion based on the unit
        if unit_input == 'F':
            converted_temp = convert_to_celsius(temp_value)
            print(f"{temp_value}°F is equal to {converted_temp:.2f}°C")
        elif unit_input == 'C':
            converted_temp = convert_to_fahrenheit(temp_value)
            print(f"{temp_value}°C is equal to {converted_temp:.2f}°F")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")

    except ValueError:
        # Handle non-numeric input
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()