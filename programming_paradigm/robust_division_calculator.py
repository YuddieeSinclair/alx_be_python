def safe_divide(numerator, denominator):
    while True:
        try:
            numerator = int(numerator)
            denominator = int(denominator)
            numerator / denominator
        except ZeroDivisionError:
            return('Error: Cannot divide by zero.')
            break
        except ValueError:
            return("Error: Please enter numeric values only.")
            break
        else:
            return f"The result of the division is {numerator / denominator}"
