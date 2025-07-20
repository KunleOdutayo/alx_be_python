num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

result = None

match operation:
    case '+':
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result= num1*num2
    case "/":
        if num2 == 0:
            print('Error: Cannot be divided by zero.')
        else:
            result= num1/num2
    case _:
        print("Error:Invalid operation selscted.")
if result is not None:
    print("The result is", result, ".")