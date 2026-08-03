# What is Functions in Python?  
# Reusable block of code.

# Python Functions - One Complete Example

# ------------------------------------
# Simple Function -> Performs a task
# ------------------------------------
def greet():
    print("Hello, Welcome!")

greet()

# ------------------------------------
# Function with Parameters -> Accepts input values
# ------------------------------------
def add(a, b):
    print("Addition:", a + b)

add(10, 20)

# ------------------------------------
# Function with Return -> Returns a value
# ------------------------------------
def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("multiply():", result)

# ------------------------------------
# Default Parameters -> Uses default value if not provided
# ------------------------------------
def welcome(name="Guest"):
    print("Welcome", name)

welcome()
welcome("Khushal")

# ------------------------------------
# Keyword Arguments -> Pass arguments by parameter name
# ------------------------------------
def student(name, age):
    print("Name:", name)
    print("Age :", age)

student(age=22, name="Khushal")

# ------------------------------------
# *args -> Accepts multiple positional arguments
# ------------------------------------
def total(*numbers):
    print("Sum:", sum(numbers))

total(10, 20, 30, 40)

# ------------------------------------
# **kwargs -> Accepts multiple keyword arguments
# ------------------------------------
def details(**info):
    print(info)

details(name="Khushal", city="Pune", age=22)

# ------------------------------------
# Lambda Function -> Small anonymous function
# ------------------------------------
square = lambda x: x * x

print("lambda:", square(5))

# ------------------------------------
# Recursive Function -> Function calls itself
# ------------------------------------
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print("factorial:", factorial(5))

# Write a function to add two numbers.
def add_numbers(a, b):
    return a + b
add_result = add_numbers(10, 20)
print("Addition of two numbers:", add_result)

# Write a function to find the square of a number.
def square_number(num):
    return num * num
result_square = square_number(5)
print("Square of the number:", result_square)

# Find the maximum of three numbers.
def find_maximum(a, b, c):
    return max(a, b, c)
max_result = find_maximum(10, 20, 30)
print("Maximum of three numbers:", max_result)

# Check whether a number is even.
def is_even(num):
    return num % 2 == 0
print("Is 10 even?", is_even(10))
print("Is 15 even?", is_even(15))

# Return a string in uppercase.
def to_uppercase(s):
    return s.upper()
print("Uppercase of 'hello':", to_uppercase("hello"))

# Calculate factorial using a function.
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)
print("Factorial of 5:", factorial(5))

# Calculate Fibonacci using a function.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
print("Fibonacci of 5:", fibonacci(5))

# Check palindrome using a function.
def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]
print("Is 'racecar' a palindrome?", is_palindrome("racecar"))
print("Is 'hello' a palindrome?", is_palindrome("hello"))

# Calculate the area of a circle.
def area_of_circle(radius):
    import math
    return math.pi * radius ** 2
area_circle = area_of_circle(5)
print("Area of the circle:", area_circle)

# Create a calculator using functions.
def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print("Result:", add_numbers(num1, num2))
    elif choice == '2':
        print("Result:", num1 - num2)
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Error: Division by zero is not allowed.")
