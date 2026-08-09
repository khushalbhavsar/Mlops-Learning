# 7. Create a calculator with default values.

def calculator(a=0, b=0, operation="add"):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"

a = float(input("Enter the first number (or press Enter to use default 0): ") or 0)
b = float(input("Enter the second number (or press Enter to use default 0): ") or 0)
operation = input("Enter the operation (add, subtract, multiply, divide) (or press Enter to use default 'add'): ") or "add"
result = calculator(a, b, operation)
print(f"The result of {operation}ing {a} and {b} is: {result}")
