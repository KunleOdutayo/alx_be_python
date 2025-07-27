def perform_operation(num1: float, num2: float, operation: str):
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second Number: "))
    operation = input ("Enter type of operation (add, subtract, multiply, divide): ")
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by 0"
        else:
            return num1/num2
    else:
        return "Error: Invalid operation"
    
        result = perform_operation (num1, num2, operation)
    print(f"Result: {result}")