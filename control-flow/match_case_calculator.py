# This script implements a simple calculator using a match case statement.

# Prompt the user to enter the first number.
num1 = float(input("Enter the first number: "))

# Prompt the user to enter the second number.
num2 = float(input("Enter the second number: "))

# Prompt the user to choose an operation.
operation = input("Choose the operation (+, -, *, /): ")

# Use a match case statement to perform the calculation.
match operation:
    case '+':
        result = num1 + num2
        print(f"The result is {result}.")
    case '-':
        result = num1 - num2
        print(f"The result is {result}.")
    case '*':
        result = num1 * num2
        print(f"The result is {result}.")
    case '/':
        # Handle division by zero gracefully.
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        # Handle unexpected or invalid operation input.
        print("Invalid operation. Please choose from +, -, *, or /.")
