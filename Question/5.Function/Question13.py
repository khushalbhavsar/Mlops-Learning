# 3. Create a function to multiply two numbers.

def multiply_numbers(a, b):
    return a * b    

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
result = multiply_numbers(a, b)
print(f"The product of {a} and {b} is: {result}")

