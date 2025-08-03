def safe_divide(numerator, denominator):
    try:
        nom1 = float(numerator)
        nom2 = float(denominator)

        result = nom1 / nom2
        return f"Result: {result}"
    except ValueError:
        return ["Error: Please enter numeric values only."]
    
    except ZeroDivisionError:
        return ["Error: Cannot divide by zero."]