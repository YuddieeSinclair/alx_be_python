num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /):")
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1/num2
match operation:
    case "+":
        print(f"The result is: {addition}")
    case "-":
        print(f"The result is: {subtraction}")
    case "*":
        print(f"The result is: {multiplication}")
    case "/":
        print(f"The result is: {division}")
    case _:
        print("Cannot divide by zero.")
