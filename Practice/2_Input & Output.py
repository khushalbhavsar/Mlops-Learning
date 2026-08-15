# What is Input & Output
# Input and output are fundamental concepts in programming that allow a program to interact with the user or other systems. 
# Input refers to the data that is provided to the program, while output refers to the data that the program produces as a result of processing the input.

# Common methods of input and output in programming include:
# Input: 
# - Using the input() function to get user input from the console.
# Output:
# - Using the print() function to display information to the console.

print("Question 1 : Take your name as input and print ")
name = input("Enter your name: ")
print(f"Hello, {name}!")

print("Question 2 : Take two numbers as input and print their sum.")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Sum of {num1} and {num2} is: {num1 + num2}")

print("Question 3 : Take two numbers as input and print all arithmetic operations.")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Modulus: {num1 % num2}")
print(f"Exponentiation: {num1 ** num2}")
print(f"Floor Division: {num1 // num2}")

print("Question 4 : Take length and width and calculate rectangle area.")
length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
print(f"Area of rectangle: {length * width}")

print("Question 5 : Take radius and calculate circle area.")
radius = float(input("Enter radius of circle: "))
import math # importing math module to use pi constant
print(f"Area of circle: {math.pi * radius ** 2}")

print("Question 6 : Take temperature in Celsius and convert it to Fahrenheit.")
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32   
print(f"{celsius}°C is equal to {fahrenheit}°F")

print("Question 7 : Take three numbers and calculate their average.")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
average = (num1 + num2 + num3) / 3
print(f"Average of {num1}, {num2}, and {num3} is: {average}")

print("Question 8 : Take a number and print its square and cube.")
number = float(input("Enter a number: "))
print(f"Square of {number} is: {number ** 2}")
print(f"Cube of {number} is: {number ** 3}")

print("Question 9 : Take principal, rate and time and calculate simple interest.")
p = float(input("Enter principal amount: ")) # principal amount
r = float(input("Enter rate of interest: ")) # rate of interest
t = float(input("Enter time in years: ")) # time in years
simple_interest = (p * r * t) / 100
print(f"Simple Interest: {simple_interest}")

print("Question 10 : Take a user's name, age and city and print them in a formatted sentence.")
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
user_city = input("Enter your city: ")
print(f"{user_name} is {user_age} years old and lives in {user_city}.")

