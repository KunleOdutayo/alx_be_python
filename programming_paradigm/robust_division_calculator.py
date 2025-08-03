def safe_divide(numerator, denominator):
    try:
        nom1 = float(numerator)
        nom2 = float(denominator)

        if nom2 == 0:
            return "Error: Cannont divide by zero."
        
        return nom1 / nom2
    except ValueError:
        return "Error: Non-numeric input. Arguements must be numbers."