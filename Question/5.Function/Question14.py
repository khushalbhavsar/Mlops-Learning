# 4. Create a function to divide two numbers.

def divide_numbers(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
result = divide_numbers(a, b)
if isinstance(result, str): # Check if the result is an error message
    print(result) 
else:
    print(f"The quotient of {a} and {b} is: {result}")
