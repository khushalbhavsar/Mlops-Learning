# 6. Write a program to divide two numbers.

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
if num2 != 0:
    quotient = num1 / num2
    print(f"The quotient of {num1} and {num2} is: {quotient}")
else:
    print("Error: Division by zero is not allowed.")

    