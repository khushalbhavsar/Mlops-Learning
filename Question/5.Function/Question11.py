# 1. Create a function to add two numbers.

def add_numbers(a, b):
    return a + b

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
result = add_numbers(a, b)
print(f"The sum of {a} and {b} is: {result}")