# What is operators and expressions in Python?
# Operators are special symbols in Python that perform operations on variables and values. Expressions are combinations of variables, values, and operators that Python evaluates to produce a result.
# Python supports various types of operators, including:
# 1. Arithmetic Operators: Used for mathematical operations.
#    Examples: + (addition), - (subtraction), * (multiplication), / (division), % (modulus), ** (exponentiation), // (floor division)
from email.mime import message
from sympy import take
print("Arithmetic Operators:")
a = 10
b = 3
print("Addition:", a + b)          # Output: 13
print("Subtraction:", a - b)       # Output: 7
print("Multiplication:", a * b)    # Output: 30
print("Division:", a / b)          # Output: 3.3333...
print("Modulus:", a % b)           # Output: 1
print("Exponentiation:", a ** b)   # Output: 1000
print("Floor Division:", a // b)    # Output: 3

# 2. Comparison Operators: Used to compare two values.
#    Examples: == (equal to), != (not equal to), > (greater than), < (less than), >= (greater than or equal to), <= (less than or equal to)
print("\nComparison Operators:")
x = 5
y = 10
print("Equal to:", x == y)          # Output: False
print("Not equal to:", x != y)      # Output: True
print("Greater than:", x > y)       # Output: False
print("Less than:", x < y)          # Output: True
print("Greater than or equal to:", x >= y)  # Output: False
print("Less than or equal to:", x <= y)     # Output: True
# Additional example:
str1 = "hello"
str2 = "world"
print("String Equal to:", str1 == str2)          # Output: False
print("String Not equal to:", str1 != str2)      # Output: True

# 3. Logical Operators: Used to combine conditional statements.
#    Examples: and, or, not
print("\nLogical Operators:")
p = True
q = False
print("Logical AND:", p and q)      # Output: False
print("Logical OR:", p or q)        # Output: True
print("Logical NOT:", not p)         # Output: False
# Additional example:
a = 7
b = 12
print("Logical AND with conditions:", (a < 10) and (b > 10))  # Output: True
print("Logical OR with conditions:", (a > 10) or (b > 10))    # Output: True
print("Logical NOT with condition:", not (a < 10))             # Output: False  


# 4. Assignment Operators: Used to assign values to variables.
#    Examples: =, +=, -=, *=, /=, %=, **=, //=
print("\nAssignment Operators:")
c = 5
c += 3  # Equivalent to c = c + 3
print("Assignment += :", c)         # Output: 8
c *= 2  # Equivalent to c = c * 2
print("Assignment *= :", c)         # Output: 16
# Additional example:
a = 10
print("Initial a =", a)            # Output: 10
a = a + 20  # Equivalent to a += 20
print("Assignment = :", a)          # Output: 30
a = a + 30   # Equivalent to a += 30
print("Assignment = :", a)          # Output: 60

# 5. Bitwise Operators: Used to perform bit-level operations.
#    Examples: & (AND), | (OR), ^ (XOR), ~ (NOT), << (left shift), >> (right shift)
print("\nBitwise Operators:")
m = 6  # Binary: 110
n = 3  # Binary: 011
print("Bitwise AND:", m & n)       # Output: 2 (Binary: 010)
print("Bitwise OR:", m | n)        # Output: 7 (Binary: 111)
print("Bitwise XOR:", m ^ n)       # Output: 5 (Binary: 101)
print("Bitwise NOT:", ~m)          # Output: -7 (Binary: ...11111001)
print("Left Shift:", m << 1)       # Output: 12 (Binary: 1100)
print("Right Shift:", m >> 1)      # Output: 3 (Binary: 011) 101)
# Note: Operator precedence determines the order in which operations are performed in an expression.
# Example of operator precedence:
result = 10 + 5 * 2  # Multiplication has higher precedence than addition
print("Operator Precedence Result:", result)  # Output: 20

# What is conditional statements in Python?
# Conditional statements in Python are used to perform different actions based on whether a certain condition is true or false. The main conditional statements in Python are if, elif, and else.
# Types of conditional statements:
# 1. if statement: Executes a block of code if a specified condition is true.
# 2. elif statement: Stands for "else if" and allows you to check multiple conditions.
# 3. else statement: Executes a block of code if none of the previous conditions are true.

# Example of if statement:
print("\nIf Statement:")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")  
else:
    print("You are not eligible to vote.")

# Example of if-elif-else statement:
print("\nIf-Elif-Else Statement:")
marks = int(input("Enter your marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# Example of nested if statement:
print("\nNested If Statement:")
money = int(input("Enter the amount you have: "))
if money >= 100:
    if money >= 500:
        print("You can buy a laptop.")
    else:
        print("You can buy a smartphone.")
else:
    print("You can buy a snack.")

# Question : Accept two numbers and print the greatest between them.
print("\nGreatest of Two Numbers:")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"The greatest number is: {num1}")
else:
    print(f"The greatest number is: {num2}")

# Question : Accept the gender from the user as char and print the respective greeting message 
# Ex - Good Morning Sir (on the basis of gender M or F).
print("\nGreeting Message Based on Gender:")
gender = input("Enter your gender (M/F): ").upper()
if gender == 'M':
    print("Good Morning Sir")
elif gender == 'F':
    print("Good Morning Ma'am")
else:
    print("Invalid input. Please enter M or F.")

# Question : Accept an integer and check whether it is an even number or odd.
print("\nEven or Odd Check:")
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# Question :  Accept name and age from the user. Check if the user is a valid voter or not.
# Ex- “hello shery you are a valid voter” or “hello shery you are not a valid voter”
print("\nVoter Eligibility Check:")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"Hello {name}, you are a valid voter.")
else:
    print(f"Hello {name}, you are not a valid voter.")

# Question :  Accept a year and check if it a leap year or not (google to find out what is a leap year)
print("\nLeap Year Check:")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


# Question : You cna also create if elif ladder using multiple conditions of elif.
print("\nTemperature Classification:")
# For understanding solve this question take the input of temperature in celsius
# Below 0°C → "Freezing Cold 
# 0°C to 10°C → "Very Cold 
# 10°C to 20°C → "Cold 
# 20°C to 30°C → "Pleasant 
# 30°C to 40°C → "Hot 
# Above 40°C → "Very Hot " 
temperature = float(input("Enter the temperature in Celsius: "))
if temperature < 0:
    print("Freezing Cold")
elif 0 <= temperature <= 10:
    print("Very Cold")
elif 10 < temperature <= 20:
    print("Cold")
elif 20 < temperature <= 30:
    print("Pleasant")
elif 30 < temperature <= 40:
    print("Hot")
else:
    print("Very Hot")
# Note: Indentation is crucial in Python as it defines the blocks of code. Proper indentation is necessary for the correct execution of conditional statements.