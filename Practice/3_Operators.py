# What is Operators?
# Operators are special symbols or keywords that perform operations on one or more operands (values or variables). 
# They are used to manipulate data and perform calculations in programming. Operators can be classified into several categories based on the type of operation they perform.

# Common types of operators include:
# 1. Arithmetic Operators: Used for mathematical calculations.
#   - Addition (+): Adds two operands.
#   - Subtraction (-): Subtracts the second operand from the first.
#   - Multiplication (*): Multiplies two operands.
#   - Division (/): Divides the first operand by the second.
#   - Modulus (%): Returns the remainder of the division of the first operand by the second.

# 2. Comparison Operators: Used to compare two values.
#   - Equal to (==): Returns True if both operands are equal.
#   - Not equal to (!=): Returns True if operands are not equal.
#   - Greater than (>): Returns True if the left operand is greater than the right.
#   - Less than (<): Returns True if the left operand is less than the right.
#   - Greater than or equal to (>=): Returns True if the left operand is greater than or equal to the right.
#   - Less than or equal to (<=): Returns True if the left operand is less than or equal to the right.

# 3. Logical Operators: Used to combine conditional statements.
#   - AND (and): Returns True if both statements are true.
#   - OR (or): Returns True if at least one statement is true.
#   - NOT (not): Returns True if the statement is false.

# 4. Assignment Operators: Used to assign values to variables.
#   - Assignment (=): Assigns the value of the right operand to the left operand.

# 5. Bitwise Operators: Used to perform bit-level operations on binary numbers.
#   - AND (&): Performs a bitwise AND operation.
#   - OR (|): Performs a bitwise OR operation.
#   - XOR (^): Performs a bitwise XOR operation.

# 6. Membership Operators: Used to test if a value is in a sequence (like a list, tuple, or string).
#   - in: Returns True if the value is found in the sequence.
#   - not in: Returns True if the value is not found in the sequence.

# 7. Identity Operators: Used to compare the memory locations of two objects.
#   - is: Returns True if both operands refer to the same object.
#   - is not: Returns True if both operands do not refer to the same object.

print("Question 1 : Take two numbers and print all arithmetic operations.")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print(f"Addition: {num1 + num2}")
print(f"Subtraction: {num1 - num2}")
print(f"Multiplication: {num1 * num2}")
print(f"Division: {num1 / num2}")
print(f"Modulus: {num1 % num2}")

print("Question 2 : Check whether a number is even or odd using %")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")

print("Question 3 : Check whether a number is divisible by 5.")
num = int(input("Enter a number: "))
if num % 5 == 0:
    print(f"{num} is divisible by 5.")
else:
    print(f"{num} is not divisible by 5.")

print("Question 4 : Find the remainder when one number is divided by another.")
num1 = int(input("Enter the dividend: "))
num2 = int(input("Enter the divisor: "))    
remainder = num1 % num2
print(f"The remainder when {num1} is divided by {num2} is: {remainder}")

print("Question 5 : Calculate square and cube using **")
num = float(input("Enter a number: "))
print(f"Square of {num} is: {num ** 2}")
print(f"Cube of {num} is: {num ** 3}")

print("Question 6 : Check whether a number is between 10 and 50.")
num = float(input("Enter a number: "))
if 10 < num < 50:
    print(f"{num} is between 10 and 50.")
else:
    print(f"{num} is not between 10 and 50.")

print("Question 7 : Check whether a person is eligible to vote using and.")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


print("Question 8 : Check whether a number is divisible by both 3 and 5.")
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print(f"{num} is divisible by both 3 and 5.")
else:
    print(f"{num} is not divisible by both 3 and 5.")

print("Question 9 : Check whether a number is divisible by either 3 or 7.")
num = int(input("Enter a number: "))
if num % 3 == 0 or num % 7 == 0:
    print(f"{num} is divisible by either 3 or 7.")
else:
    print(f"{num} is not divisible by either 3 or 7.")

print("Question 10 : Take a username and check whether it exists in a list using in.")
name_list = ["Alice", "Bob", "Charlie", "David"]
username = input("Enter a username: ")
if username in name_list:
    print(f"{username} exists in the list.")
else:
    print(f"{username} does not exist in the list.")

