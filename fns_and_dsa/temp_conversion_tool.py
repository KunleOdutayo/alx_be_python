# define global variables
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    return (celsius *CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def main():
    temp_input = float(input("Enter the temperature to convert: "))
    temp_unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

    if temp_unit == "F":
        converted_temp = convert_to_celsius(temp_input)
        print("{temp_input}°F is equal to {converted_temp}°C")
    elif temp_unit == "C":
        converted_temp = convert_to_fahrenheit(temp_input)
        print("{temp_input}°C is equal to {converted_temp}°F")
    else:
        print("Invalid unit. Please enter 'C' or 'F'" )


if __name__ == "__main__":
    main()