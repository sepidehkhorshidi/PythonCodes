def add(num1, num2):
    """Function to add two numbers"""
    return num1 + num2

def subtract(num1, num2):
    """Function to subtract two numbers"""
    return num1 - num2

def multiply(num1, num2):
    """Function to multiply two numbers"""
    return num1 * num2

def divide(num1, num2):
    """Function to divide two numbers"""
    if num2 == 0:
        print("Error: cannot divide by zero!")
        return None
    else:
        return num1 / num2

if __name__ == '__main__':
    # Take user input for two numbers and the operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    
    # Perform the selected operation
    if operation == '+':
        result = add(num1, num2)
    elif operation == '-':
        result = subtract(num1, num2)
    elif operation == '*':
        result = multiply(num1, num2)
    elif operation == '/':
        result = divide(num1, num2)
    else:
        print("Error: invalid operation!")
        result = None
    
    # Print the result of the operation
    if result is not None:
        print("The result is:", result)