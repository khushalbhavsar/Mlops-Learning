# What is a variable in Python?
# A variable is a named location in memory that stores a value.
# In Python, you can create a variable by assigning a value to it using the equals sign (=). Variables can hold different data types such as integers, floats, strings, lists, dictionaries, etc.

# Swap two variables without using a third variable.
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
a = a + b
b = a - b
a = a - b
print("After swapping:")    
print("a =", a, "b =", b)

# Find the data type of a variable.
int_var = 10
float_var = 10.5
string_var = "Hello"
print("Data type of int_var:", type(int_var))
print("Data type of float_var:", type(float_var))
print("Data type of string_var:", type(string_var))

# Convert a string to an integer.
string_num = "123"
int_num = int(string_num)
print("Converted integer:", int_num)

# Convert an integer to a string.
int_num = 456
string_num = str(int_num)
print("Converted string:", string_num)

# Take user input and print it.
user_input = input("Enter something: ")
print("You entered:", user_input)

# Calculate the area of a rectangle.
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area_rectangle = length * width
print("Area of the rectangle:", area_rectangle)

# Calculate the area of a circle.
import math
radius = float(input("Enter the radius of the circle: "))
area_circle = math.pi * radius ** 2
print("Area of the circle:", area_circle)

# Calculate simple interest.
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))
simple_interest = (principal * rate * time) / 100
print("Simple interest:", simple_interest)

# Calculate the average of three numbers.
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
average = (num1 + num2 + num3) / 3
print("Average of the three numbers:", average)


