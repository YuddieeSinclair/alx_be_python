def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "divide":
        if num1 == 0 or num2 == 0:
            print("divide by zero error")
        else:
            return num1/num2
    elif operation == "multiply":
        return num1 * num2
    else:
        print("enter a valid opeartion")