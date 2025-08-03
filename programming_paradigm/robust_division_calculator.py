def safe_divide(numerator, denominator):
    try:
        nom1 = float(numerator)
        nom2 = float(denominator)

        result = nom1 / nom2
        return f"Result: {result}"
    except ValueError:
        return ["Error: Must enter numeric value."]
    
    except ZeroDivisionError:
        return ["Error: Cannot divide by zero."]