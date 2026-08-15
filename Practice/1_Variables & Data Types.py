# What is a variable?
# A variable is a named location in memory that stores a value. It can hold different types of data, such as numbers, strings, or more complex data structures. Variables are used to store and manipulate data in a program.

# What are data types?
# Data types define the type of data that a variable can hold. Common data types include:
# - Integer (int): Whole numbers, e.g., 1, 42, -5
# - Float (float): Decimal numbers, e.g., 3.14, -0
# - String (str): Text, e.g., "Hello", 'Python'
# - Boolean (bool): True or False values
# - List (list): Ordered collection of items, e.g., [1, 2, 3]
# - Dictionary (dict): Key-value pairs, e.g., {"name": "Alice", "age": 30}
# - Tuple (tuple): Ordered, immutable collection of items, e.g., (1, 2, 3)
# - Set (set): Unordered collection of unique items, e.g., {1, 2, 3}
# - None (NoneType): Represents the absence of a value, e.g., None

print("Question 1 : Create variables for your name, age, CGPA and city and print them.")
name = "Khushal"
age = 20
CGPA = 9.5
city = "Mumbai"
print(f"Name: {name}, Age: {age}, CGPA: {CGPA}, City: {city}")

print("Question 2 : Take two integers and print their sum.")
num1 = 10
num2 = 20
print(f"Sum of {num1} and {num2} is: {num1 + num2}")

print("Question 3 : Take two numbers and print all arithmetic operations.")
num1 = 15
num2 = 5
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Modulus: {num1 % num2}")

print("Question 4 : Calculate rectangle area and perimeter.")
length = 10
width = 5
print(f"Area of rectangle: {length * width}")
print(f"Perimeter of rectangle: {2 * (length + width)}")

print("Question 5 : Calculate circle area and circumference.")
radius = 7
import math # importing math module to use pi constant
print(f"Area of circle: {math.pi * radius ** 2}")
print(f"Circumference of circle: {2 * math.pi * radius}")

print("Question 6 : Convert Celsius to Fahrenheit.")
celsius = 25
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C is equal to {fahrenheit}°F")

print("Question 7 : Convert kilometers to meters.")
kilometers = 5
meters = kilometers * 1000
print(f"{kilometers} kilometers is equal to {meters} meters")

print("Question 8 : Swap two numbers.")
a = 10
b = 20
print(f"Before swapping: a = {a}, b = {b}")
a, b = b, a # Swapping values using tuple unpacking 
print(f"After swapping: a = {a}, b = {b}")

print("Question 9 : Calculate simple interest.")
p = 1000 # principal amount
r = 5 # rate of interest
t = 2 # time in years
simple_interest = (p * r * t) / 100
print(f"Simple Interest: {simple_interest}")

print("Question 10 : Take a value and print its type.")
value = 42
print(f"The type of the value {value} is: {type(value)}")
