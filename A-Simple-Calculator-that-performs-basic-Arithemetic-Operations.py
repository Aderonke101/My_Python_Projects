def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 != 0:
        return num1 / num2
    else:
        return "Error: Division by zero is not allowed"

def get_number_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_operation_input():
    operations = ['+', '-', '*', '/']
    while True:
        operation = input("Select an operation (+, -, *, /): ")
        if operation in operations:
            return operation
        else:
            print("Invalid operation. Please choose from +, -, *, /.")

def calculator():
    print("Welcome to the Simple Calculator!")

    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")

   
    operation = get_operation_input()


    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)

    
    print(f"The result of {num1} {operation} {num2} is: {result}")

calculator()