# Complete Python Learning Guide

## Table of Contents

1. [Basics & Core Data Handling](#basics--core-data-handling)
2. [Operators & Expressions](#operators--expressions)
3. [Conditional Statements](#conditional-statements)
4. [Loops](#loops)
5. [Functions](#functions)
6. [Data Structures](#data-structures)
7. [Exception & File Handling](#exception--file-handling)

---

# Basics & Core Data Handling

## What is Python?

Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

Python is widely used for web development, data analysis, artificial intelligence, scientific computing, and more. It has a large standard library and a vibrant ecosystem of third-party packages.

Example of a simple Python program:

```python
print("Hello, World!")
```

## What is an Interpreter in Python?

An interpreter in Python is a program that reads and executes Python code line by line. It translates the high-level Python code into machine code that the computer's processor can understand and execute.

The Python interpreter allows for interactive programming, where you can type and execute code in real-time, making it easy to test and debug code snippets.

```python
>>> print("Hello, World!")
```

## What is a Comment in Python?

A comment in Python is a line that starts with the '#' symbol. It is used to explain the code and is ignored by the Python interpreter during execution. Comments are useful for documenting code.

Example of comments:

```python
# This is a single-line comment
print("Hello, Python!")  # This is an inline comment
```

## What is a Variable in Python?

A variable in Python is a named location used to store data in memory. It acts as a container for values that can be changed and manipulated throughout the program.

Variables are created by assigning a value to a name using the '=' operator.

```python
age = 25  # Here, 'age' is a variable that stores the integer value
print("I am", age, "years old.")
```

## Variable Naming Rules

1. Variable names must start with a letter (a-z, A-Z) or an underscore (\_)
2. The rest can contain letters, digits (0-9), or underscores
3. Variable names are case-sensitive (e.g., 'age' and 'Age' are different)
4. Cannot use Python reserved keywords (e.g., 'if', 'for', 'while')
5. Should be descriptive and meaningful to enhance readability

```python
valid_variable = 10
myVariable = 40      # Valid
# 2ndVariable = 30   # Invalid: starts with a digit

print("Valid variable value:", valid_variable)
print("My variable value:", myVariable)
```

## Variable Naming Conventions

1. Use lowercase letters with underscores (snake_case)
2. Avoid single-character names except for counters
3. Use descriptive names that convey purpose

```python
user_name = "Alice"  # Descriptive and follows snake_case
user_age = 30        # Descriptive and follows snake_case
print("User Name:", user_name)
print("User Age:", user_age)
```

## Data Types in Python

Python has several built-in data types:

- **int**: Integer values (e.g., 1, -5)
- **float**: Floating-point numbers (e.g., 3.14, -0.001)
- **str**: Strings (sequences of characters)
- **bool**: Boolean values (True or False)
- **complex**: Complex numbers (e.g., 3+4j)

```python
integer_var = 10          # int
float_var = 3.14         # float
string_var = "Hello"     # str
boolean_var = True       # bool
complex_var = 2 + 3j    # complex

print("Integer:", integer_var)
print("Float:", float_var)
print("String:", string_var)
print("Boolean:", boolean_var)
print("Complex:", complex_var)
```

## String and Type Conversion

A string in Python is a sequence of characters enclosed in single quotes, double quotes, or triple quotes. Strings are used to represent text data.

Type conversion refers to the process of converting a variable from one data type to another. Python provides built-in functions like `int()`, `float()`, `str()`, and `bool()`.

```python
greeting = "Hello, World!"
print(greeting)

num_str = "123"          # str
num_int = int(num_str)   # Convert str to int
num_float = float(num_int)  # Convert int to float

print("String to Integer:", num_int)
print("Integer to Float:", num_float)
print("Type of num_str:", type(num_str))
print("Type of num_int:", type(num_int))
print("Type of num_float:", type(num_float))
```

**Note**: Type conversion may lead to data loss (e.g., converting a float to int truncates the decimal).

```python
float_value = 9.99
int_value = int(float_value)  # Data loss
print("Float to Integer (data loss):", int_value)
print("Type of int_value:", type(int_value))
```

## String Slicing and Indexing

String slicing allows you to extract a substring by specifying a range of indices. The syntax is `string[start:end]`.

```python
sample_string = "Hello, Python!"
substring = sample_string[7:13]  # Extracting "Python"
print("Substring:", substring)

# Indexing
first_character = sample_string[0]  # First character
last_character = sample_string[-1]  # Last character
print("First character:", first_character)
print("Last character:", last_character)

# Slicing with step
step_slice = sample_string[0:6:2]  # Every 2nd character
print("Step slice:", step_slice)

# Slicing with omitted indices
omitted_start = sample_string[:4]  # From start to index 4
omitted_end = sample_string[2:]    # From index 2 to end
print("Omitted start slice:", omitted_start)
print("Omitted end slice:", omitted_end)

# Reversing a string
reversed_string = sample_string[::-1]
print("Reversed string:", reversed_string)
```

## Boolean Type Conversion

```python
bool_from_int = bool(1)         # True
bool_from_zero = bool(0)        # False
bool_from_str = bool("Hello")   # True (non-empty string)
bool_from_empty_str = bool("")  # False (empty string)

print("Boolean from int 1:", bool_from_int)
print("Boolean from int 0:", bool_from_zero)
print("Boolean from non-empty string:", bool_from_str)
print("Boolean from empty string:", bool_from_empty_str)
```

## Implicit vs Explicit Type Conversion

**Implicit type conversion** (type coercion) occurs when Python automatically converts one data type to another.

**Explicit type conversion** is when the programmer manually converts using built-in functions.

```python
# Implicit conversion
int_num = 5
float_num = 2.5
result = int_num + float_num  # int converted to float
print("Result of implicit conversion:", result)
print("Type of result:", type(result))

# Explicit conversion
str_num = "10"
int_num = int(str_num)
print("Explicitly converted integer:", int_num)
print("Type:", type(int_num))
```

## String Methods

```python
original_string = "  Hello, World!  "
upper_string = original_string.upper()      # Uppercase
lower_string = original_string.lower()      # Lowercase
stripped_string = original_string.strip()   # Remove whitespace

print("Uppercase:", upper_string)
print("Lowercase:", lower_string)
print("Stripped string:", stripped_string)
```

## String Concatenation and Formatting

```python
str1 = "Hello"
str2 = "World"
concatenated = str1 + ", " + str2 + "!"
print("Concatenated:", concatenated)

# f-string formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print("Formatted string:", formatted_string)
```

## Input and Output in Python

Input in Python is handled using the `input()` function, which reads user input as a string.

Output is done using the `print()` function.

```python
user_name = input("Enter your name: ")
print("Hello,", user_name + "!")

print("This is an example of output in Python.")

age_str = input("Enter your age: ")
age_int = int(age_str)
print("You are", age_int, "years old.")

height = 88
print(f"Your height is {height} feet.")

num1, num2 = input("Enter two numbers separated by space: ").split()
num1 = int(num1)
num2 = int(num2)
sum_result = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum_result)
```

---

# Operators & Expressions

## Operators and Expressions in Python

Operators are special symbols in Python that perform operations on variables and values. Expressions are combinations of variables, values, and operators that Python evaluates to produce a result.

Python supports various types of operators:

### 1. Arithmetic Operators

Used for mathematical operations: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `%` (modulus), `**` (exponentiation), `//` (floor division)

```python
print("Arithmetic Operators:")
a = 10
b = 3
print("Addition:", a + b)              # 13
print("Subtraction:", a - b)           # 7
print("Multiplication:", a * b)        # 30
print("Division:", a / b)              # 3.3333...
print("Modulus:", a % b)               # 1
print("Exponentiation:", a ** b)       # 1000
print("Floor Division:", a // b)       # 3
```

### 2. Comparison Operators

Used to compare two values: `==` (equal), `!=` (not equal), `>` (greater than), `<` (less than), `>=` (greater or equal), `<=` (less or equal)

```python
print("\nComparison Operators:")
x = 5
y = 10
print("Equal to:", x == y)             # False
print("Not equal to:", x != y)         # True
print("Greater than:", x > y)          # False
print("Less than:", x < y)             # True
print("Greater than or equal to:", x >= y)  # False
print("Less than or equal to:", x <= y)     # True

# String comparison
str1 = "hello"
str2 = "world"
print("String Equal to:", str1 == str2)      # False
print("String Not equal to:", str1 != str2)  # True
```

### 3. Logical Operators

Used to combine conditional statements: `and`, `or`, `not`

```python
print("\nLogical Operators:")
p = True
q = False
print("Logical AND:", p and q)        # False
print("Logical OR:", p or q)          # True
print("Logical NOT:", not p)           # False

# Additional examples
a = 7
b = 12
print("Logical AND with conditions:", (a < 10) and (b > 10))  # True
print("Logical OR with conditions:", (a > 10) or (b > 10))    # True
print("Logical NOT with condition:", not (a < 10))            # False
```

### 4. Assignment Operators

Used to assign values to variables: `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`

```python
print("\nAssignment Operators:")
c = 5
c += 3  # Equivalent to c = c + 3
print("Assignment += :", c)           # 8
c *= 2  # Equivalent to c = c * 2
print("Assignment *= :", c)           # 16

# Additional examples
a = 10
print("Initial a =", a)               # 10
a += 20
print("Assignment = :", a)            # 30
a += 30
print("Assignment = :", a)            # 60
```

### 5. Bitwise Operators

Used for bit-level operations: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift)

```python
print("\nBitwise Operators:")
m = 6   # Binary: 110
n = 3   # Binary: 011
print("Bitwise AND:", m & n)          # 2 (Binary: 010)
print("Bitwise OR:", m | n)           # 7 (Binary: 111)
print("Bitwise XOR:", m ^ n)          # 5 (Binary: 101)
print("Bitwise NOT:", ~m)             # -7
print("Left Shift:", m << 1)          # 12 (Binary: 1100)
print("Right Shift:", m >> 1)         # 3 (Binary: 011)
```

## Operator Precedence

Operator precedence determines the order in which operations are performed in an expression.

```python
result = 10 + 5 * 2  # Multiplication has higher precedence than addition
print("Operator Precedence Result:", result)  # 20
```

---

# Conditional Statements

## What are Conditional Statements in Python?

Conditional statements are used to perform different actions based on whether a condition is true or false.

### Types of Conditional Statements:

- **if statement**: Executes a block of code if a condition is true
- **elif statement**: Allows you to check multiple conditions
- **else statement**: Executes if none of the previous conditions are true

### If Statement

```python
print("\nIf Statement:")
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")
```

### If-Elif-Else Statement

```python
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
```

### Nested If Statement

```python
print("\nNested If Statement:")
money = int(input("Enter the amount you have: "))
if money >= 100:
    if money >= 500:
        print("You can buy a laptop.")
    else:
        print("You can buy a smartphone.")
else:
    print("You can buy a snack.")
```

## Practice Questions

### Q1: Print the Greatest of Two Numbers

```python
print("\nGreatest of Two Numbers:")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"The greatest number is: {num1}")
else:
    print(f"The greatest number is: {num2}")
```

### Q2: Gender-based Greeting

Accept gender from user (M/F) and print greeting.

```python
print("\nGreeting Message Based on Gender:")
gender = input("Enter your gender (M/F): ").upper()
if gender == 'M':
    print("Good Morning Sir")
elif gender == 'F':
    print("Good Morning Ma'am")
else:
    print("Invalid input. Please enter M or F.")
```

### Q3: Check if Even or Odd

```python
print("\nEven or Odd Check:")
number = int(input("Enter an integer: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
```

### Q4: Check if Valid Voter

```python
print("\nVoter Eligibility Check:")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    print(f"Hello {name}, you are a valid voter.")
else:
    print(f"Hello {name}, you are not a valid voter.")
```

### Q5: Check Leap Year

```python
print("\nLeap Year Check:")
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
```

### Q6: Temperature Classification

Classify temperature in Celsius:

- Below 0°C → Freezing Cold
- 0°C to 10°C → Very Cold
- 10°C to 20°C → Cold
- 20°C to 30°C → Pleasant
- 30°C to 40°C → Hot
- Above 40°C → Very Hot

```python
print("\nTemperature Classification:")
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
```

**Note:** Indentation is crucial in Python as it defines code blocks. Proper indentation is necessary for correct execution of conditional statements.

---

# Loops

## What is a Loop in Python?

Loops in Python are used to execute a block of code repeatedly as long as a certain condition is met. The main types of loops are:

- **for loop**: Iterates over a sequence (list, tuple, dict, set, string) a fixed number of times
- **while loop**: Repeats a block of code as long as a condition is true

## The range() Function

The `range()` function generates a sequence of numbers commonly used in for loops:

- `range(stop)`: Numbers from 0 to stop-1
- `range(start, stop)`: Numbers from start to stop-1
- `range(start, stop, step)`: Numbers from start to stop-1, incrementing by step

## For Loop Examples

```python
print("For Loop Example:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

## While Loop Examples

```python
print("\nWhile Loop Example:")
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1
```

## Using range() in For Loops

```python
print("\nUsing range() in For Loop:")
for num in range(1, 6):  # Numbers 1 to 5
    print(num)
```

## Nested Loops

```python
print("\nNested Loop Example:")
for i in range(1, 4):  # Outer loop 1 to 3
    for j in range(1, 4):  # Inner loop 1 to 3
        print(f"i: {i}, j: {j}")
```

## Break and Continue Statements

The `break` statement exits a loop prematurely, while `continue` skips the current iteration.

```python
print("\nLoop with break statement:")
for i in range(1, 11):
    if i == 6:
        print("Breaking the loop at i =", i)
        break
    else:
        print(i)

print("\nLoop with continue statement:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)  # Print only odd numbers
```

## Else with Loops

```python
print("\nFor loop with else statement:")
for i in range(1, 6):
    print(i)
else:
    print("Loop completed successfully!")
```

## While Loop Details

### What is a While Loop in Python?

A while loop in Python repeatedly executes a block of code as long as a specified condition is true. It's useful when the number of iterations is not predetermined and depends on dynamic conditions.

### Syntax

```python
while condition:
    # code block to be executed
```

### Basic While Loop Example

```python
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Increment to avoid infinite loop
```

### While Loop with Break Statement

```python
print("\nWhile Loop with break statement:")
num = 1
while num <= 10:
    if num == 6:
        print("Breaking the loop at num =", num)
        break  # Exit the loop when num is 6
    print(num)
    num += 1
```

### While Loop with Continue Statement

```python
print("\nWhile Loop with continue statement:")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)  # Print only odd numbers
```

## Loop Practice Questions

### Q1: Print Hello World n times

```python
n = int(input("Enter an integer: "))
print(f"Printing 'Hello, World!' {n} times:")
for i in range(n):
    print("Hello, World!")
```

### Q2: Print Natural Numbers up to n

```python
n = int(input("Enter a natural number n: "))
print(f"Natural numbers up to {n}:")
for i in range(1, n + 1):
    print(i)
```

### Q3: Print Numbers in Reverse (n to 1)

```python
n = int(input("Enter a natural number n: "))
print(f"Natural numbers from {n} to 1:")
for i in range(n, 0, -1):  # Reverse order
    print(i)
```

### Q4: Print Multiplication Table

```python
print("\n5 Table:")
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")

num = int(input("Enter a number to print its table: "))
print(f"Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
```

### Q5: Sum of First n Natural Numbers

```python
n = int(input("Enter a natural number n: "))
sum_n = 0
for i in range(1, n + 1):
    sum_n += i
print(f"Sum of first {n} natural numbers is: {sum_n}")
```

### Q6: Factorial of a Number

```python
n = int(input("Enter a natural number n: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n} is: {factorial}")
```

### Q7: Print All Factors of a Number

```python
n = int(input("Enter a natural number n: "))
print(f"Factors of {n} are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)
```

### Q8: Sum of Even and Odd Numbers

```python
n = int(input("Enter a natural number n: "))
sum_even = 0
sum_odd = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i
print(f"Sum of even numbers up to {n} is: {sum_even}")
print(f"Sum of odd numbers up to {n} is: {sum_odd}")
```

### Q9: Check if Perfect Number

A perfect number is one where the sum of its factors equals the number itself (e.g., 6 = 1 + 2 + 3).

```python
n = int(input("Enter a natural number n: "))
sum_of_factors = 0
for i in range(1, n):
    if n % i == 0:
        sum_of_factors += i
if sum_of_factors == n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")
```

### Q10: Check if Prime Number

```python
n = int(input("Enter a natural number n: "))
is_prime = True
if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")
```

## Looping Through Strings

```python
print("\nLooping through a string:")
my_string = "Hello World 2026"

print("\nUsing range():")
for i in range(len(my_string)):
    print(my_string[i])

print("\nDirect iteration:")
for char in my_string:
    print(char)
```

### Q11: Reverse a String

```python
string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print(f"Reversed string: {reversed_string}")
```

### Q12: Check if Palindrome

```python
string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
if string == reversed_string:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")
```

### Q13: Count Characters, Digits, and Symbols

Given: str1 = "P@#yn26at^&i5ve"
Expected output: Chars = 8, Digits = 3, Symbols = 4

```python
string = input("Enter a string: ")
count_chars = 0
count_digits = 0
count_symbols = 0
for char in string:
    if char.isalpha():
        count_chars += 1
    elif char.isdigit():
        count_digits += 1
    else:
        count_symbols += 1
print(f"Chars = {count_chars}")
print(f"Digits = {count_digits}")
print(f"Symbols = {count_symbols}")
```

### Q14: Separate Each Digit of a Number

```python
number = int(input("Enter a number: "))
print("The digits are:")
while number > 0:
    digit = number % 10  # Get the last digit
    print(digit)
    number = number // 10  # Remove the last digit
```

### Q15: Reverse a Number

```python
num = int(input("Enter a number to reverse: "))
reversed_num = 0
while num > 0:
    digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Build reversed number
    num = num // 10  # Remove the last digit
print(f"The reversed number is: {reversed_num}")
```

### Q16: Check if Palindromic Number

Check if a number and its reverse are equal.

```python
num = int(input("Enter a number to check for palindrome: "))
original_num = num
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
if original_num == reversed_num:
    print(f"{original_num} is a palindrome.")
else:
    print(f"{original_num} is not a palindrome.")
```

### Q17: Number Guessing Game

Create a random number guessing game with Python.

```python
import random

random_number = random.randint(1, 100)  # Random number between 1 and 100
attempts = 0
print("Welcome to the Number Guessing Game! Try to guess the number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < random_number:
        print("Too low! Try again.")
    elif guess > random_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
        break
```

---

# Functions

## What is a Function?

A function is a block of reusable code that performs a specific task. Functions help in:

- Organizing code
- Improving readability
- Avoiding code repetition
- Making code modular and maintainable

Functions can take inputs (parameters) and return outputs (results). The `def` keyword is used to define a function.

## Defining and Calling a Function

```python
def greet(name):
    """This function greets the person passed as a parameter."""
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!
```

## Function Parameters and Arguments

**Parameters** are variables listed in the function definition.
**Arguments** are the values passed to the function when it is called.

```python
def add(a, b):
    """This function returns the sum of two numbers."""
    print(f"Adding {a} and {b}")
    return a + b

result = add(5, 3)
print(f"Result: {result}")  # Output: Result: 8
```

## Types of Arguments

### 1. Positional Arguments

Arguments are passed in the order they are defined.

```python
def multiply(x, y):
    return x * y

print(multiply(4, 5))  # Output: 20
```

### 2. Keyword Arguments

Arguments are passed with the parameter name specified.

```python
def divide(dividend, divisor):
    return dividend / divisor

print(divide(divisor=2, dividend=10))  # Output: 5.0
```

### 3. Default Arguments

Parameters have default values if no argument is provided.

```python
def power(base, exponent=2):
    return base ** exponent

print(power(3))        # Output: 9 (3^2)
print(power(2, 3))     # Output: 8 (2^3)
```

## Return vs Print

- **print()**: Outputs data to the console
- **return**: Sends a result back to the caller

```python
def square(num):
    """This function returns the square of a number."""
    return num * num

print(square(4))  # Output: 16
```

The `square(4)` returns 16, which is then printed to the console.

## Practice Example: Check Palindrome Using Function

```python
def is_palindrome(s):
    reversed = ""
    for i in range(len(s) - 1, -1, -1):
        reversed += s[i]

    if s == reversed:
        return True
    else:
        return False

# Test the function
test_string = "radar"
if is_palindrome(test_string):
    print(f'"{test_string}" is a palindrome.')
else:
    print(f'"{test_string}" is not a palindrome.')
# Output: "radar" is a palindrome.
```

## Key Concepts

- Functions are defined with the `def` keyword
- Functions can take parameters and return values
- Parameters can be positional, keyword, or have default values
- Functions improve code reusability and organization
- Always return a value if the result is needed elsewhere
- Use `print()` to display output, `return` to send results back

---

# Data Structures

Data structures are ways of organizing and storing data so it can be accessed and modified efficiently. Common data structures in Python include lists, tuples, sets, and dictionaries.

## Lists in Python

### What is a List?

A list is an ordered collection of items that can be of different types, defined using square brackets `[]`.

### List Characteristics

**1. Mutable**: Lists can be modified after creation.

```python
my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3]
```

**2. Duplicates**: Lists can contain duplicate elements.

```python
my_list = [1, 2, 2, 3]
print(my_list)  # Output: [1, 2, 2, 3]
```

**3. Ordered**: Lists maintain insertion order.

```python
my_list = [5, 3, 8]
print(my_list)  # Output: [5, 3, 8]
```

**4. Heterogeneous**: Lists can contain different data types.

```python
my_list = [1, "hello", 3.14, True]
print(my_list)  # Output: [1, 'hello', 3.14, True]
```

### List Traversal and Methods

```python
numbers = [1, 2, 3, 4, 5]

# Using for loop
for num in numbers:
    print(num)

# Using index
for i in range(len(numbers)):
    print(numbers[i])
```

### Common List Methods

```python
# append(): Add element to end
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# remove(): Remove first occurrence
my_list.remove(2)
print(my_list)  # [1, 3, 4]

# pop(): Remove and return element at index
popped = my_list.pop()
print(popped, my_list)  # 4, [1, 3]

# sort(): Sort in ascending order
my_list = [3, 1, 4, 2]
my_list.sort()
print(my_list)  # [1, 2, 3, 4]

# reverse(): Reverse order
my_list.reverse()
print(my_list)  # [4, 3, 2, 1]

# len(): Length
print(len(my_list))  # 4

# index(): Find first occurrence
print(my_list.index(3))  # 1

# extend(): Add multiple elements
my_list.extend([5, 6])
print(my_list)  # [4, 3, 2, 1, 5, 6]

# count(): Count occurrences
print(my_list.count(2))  # 1

# clear(): Remove all elements
my_list.clear()
print(my_list)  # []
```

### List Practice Examples

```python
# Print positive and negative numbers
numbers = [10, -5, 3, -1, 0, 7, -8]
print("Positive:", [n for n in numbers if n > 0])
print("Negative:", [n for n in numbers if n < 0])

# Find mean
numbers = [10, 20, 30, 40, 50]
mean = sum(numbers) / len(numbers)
print(f"Mean: {mean}")  # 30.0

# Find greatest element and index
numbers = [10, 25, 5, 40, 15]
greatest = max(numbers)
index = numbers.index(greatest)
print(f"Greatest: {greatest} at index {index}")

# Find second greatest
numbers = [10, 25, 5, 40, 15]
first = numbers[0]
second = numbers[0]
for num in numbers:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num
print(f"Second greatest: {second}")

# Check if sorted
numbers = [1, 2, 3, 4, 5]
is_sorted = all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
print(f"Is sorted: {is_sorted}")
```

## Tuples in Python

### What is a Tuple?

A tuple is an ordered, immutable collection of items, defined using parentheses `()`.

### Tuple Characteristics

**1. Immutable**: Cannot be changed after creation.

```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This raises TypeError
print(my_tuple)
```

**2. Duplicates**: Can contain duplicates.

```python
my_tuple = (1, 2, 2, 3)
print(my_tuple)
```

**3. Ordered**: Maintains insertion order.

```python
my_tuple = (5, 3, 8)
print(my_tuple)
```

**4. Heterogeneous**: Can contain different types.

```python
my_tuple = (1, "hello", 3.14, True)
print(my_tuple)
```

### Tuple Unpacking

```python
my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a, b, c)  # 10 20 30
```

### Common Tuple Methods

```python
my_tuple = (1, 2, 2, 3)

# count(): Count occurrences
print(my_tuple.count(2))  # 2

# index(): Find index
print(my_tuple.index(3))  # 3
```

**Note**: Tuples don't have methods like append(), remove(), pop(), sort(), etc.

## Sets in Python

### What are Sets?

A set is an unordered collection of unique items defined using curly braces `{}` or the `set()` function.

### Set Characteristics

**1. Mutable**: Elements can be added or removed after creation.

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}
```

**2. No Duplicates**: Sets automatically remove duplicate elements.

```python
my_set = {1, 2, 2, 3}
print(my_set)  # {1, 2, 3}
```

**3. Unordered**: Sets do not maintain element order.

```python
my_set = {5, 3, 8}
print(my_set)  # Order may vary
```

**4. Heterogeneous**: Sets can contain different data types.

```python
my_set = {1, "hello", 3.14, True}
print(my_set)  # Order may vary
```

### Set Traversal

```python
numbers = {1, 2, 3, 4, 5}
for num in numbers:
    print(num)
```

### Common Set Methods

```python
# add(): Add single element
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

# remove(): Remove element (raises KeyError if not found)
my_set.remove(2)
print(my_set)  # {1, 3, 4}

# discard(): Remove element without error
my_set.discard(5)
print(my_set)  # {1, 3, 4}

# pop(): Remove arbitrary element
element = my_set.pop()
print(element, my_set)

# clear(): Remove all elements
my_set.clear()
print(my_set)  # set()

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# union(): Combine sets
union = set1.union(set2)
print(union)  # {1, 2, 3, 4, 5}

# intersection(): Common elements
intersection = set1.intersection(set2)
print(intersection)  # {3}

# difference(): Elements in set1 but not set2
difference = set1.difference(set2)
print(difference)  # {1, 2}

# symmetric_difference(): Elements in either but not both
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)  # {1, 2, 4, 5}
```

## Dictionaries in Python

### What are Dictionaries?

A dictionary is an unordered collection of key-value pairs defined using curly braces with colons `{"key": value}`.

### Dictionary Characteristics

**1. Mutable**: Can be modified after creation.

```python
my_dict = {"a": 1, "b": 2}
my_dict["a"] = 10
print(my_dict)  # {'a': 10, 'b': 2}
```

**2. No Duplicate Keys**: Keys must be unique. Values can be duplicated.

```python
my_dict = {"a": 1, "b": 2, "a": 3}
print(my_dict)  # {'a': 3, 'b': 2}
```

**3. Unordered**: Prior to Python 3.7, order was not guaranteed.

```python
my_dict = {"b": 2, "a": 1}
print(my_dict)
```

**4. Heterogeneous**: Keys and values can be different types.

```python
my_dict = {1: "one", "two": 2, 3.0: [1, 2, 3]}
print(my_dict)
```

### Dictionary Traversal

```python
my_dict = {"a": 1, "b": 2, "c": 3}
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")
```

### Common Dictionary Methods

```python
my_dict = {"a": 1, "b": 2, "c": 3}

# keys(): Get all keys
print(my_dict.keys())  # dict_keys(['a', 'b', 'c'])

# values(): Get all values
print(my_dict.values())  # dict_values([1, 2, 3])

# items(): Get key-value pairs
print(my_dict.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])

# get(): Get value by key
value = my_dict.get("b")
print(value)  # 2

# pop(): Remove and return value
removed = my_dict.pop("c")
print(removed)  # 3
print(my_dict)  # {'a': 1, 'b': 2}

# update(): Merge dictionaries
my_dict.update({"d": 4, "e": 5})
print(my_dict)  # {'a': 1, 'b': 2, 'd': 4, 'e': 5}

# clear(): Remove all pairs
my_dict.clear()
print(my_dict)  # {}
```

## Shallow Copy vs Deep Copy

Understanding the difference between shallow and deep copies is crucial when working with nested data structures.

**Shallow Copy**: Creates a new container but references the original nested objects.

**Deep Copy**: Creates a completely independent copy, including nested objects.

```python
import copy

original_list = [1, 2, [3, 4]]

# Shallow copy
shallow = copy.copy(original_list)

# Deep copy
deep = copy.deepcopy(original_list)

# Modify nested list
original_list[2][0] = 99

print("Original:", original_list)        # [1, 2, [99, 4]]
print("Shallow:", shallow)               # [1, 2, [99, 4]]
print("Deep:", deep)                     # [1, 2, [3, 4]]
```

## Dictionary Practice Examples

### Merge Two Dictionaries

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Using update()
dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 3, 'c': 4}

# Using loop
for key, value in dict2.items():
    dict1[key] = value
print(dict1)  # {'a': 1, 'b': 3, 'c': 4}
```

### Sum All Dictionary Values

```python
my_dict = {"a": 10, "b": 20, "c": 30}

# Method 1: Loop
total = 0
for value in my_dict.values():
    total += value
print("Total:", total)  # 60

# Method 2: sum() function
total = sum(my_dict.values())
print("Total:", total)  # 60
```

### Count Frequency of Elements

```python
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = {}

for element in elements:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

print(frequency)  # {'apple': 3, 'banana': 2, 'orange': 1}
```

### Combine Two Dictionaries with Value Addition

```python
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}

combined = {}
for key in dict1.keys() | dict2.keys():
    combined[key] = dict1.get(key, 0) + dict2.get(key, 0)

print(combined)  # {'a': 400, 'b': 400, 'c': 300, 'd': 400}
```

## Summary of Data Structures

| Structure  | Ordered | Mutable | Duplicates | Key-Value | Syntax |
| ---------- | ------- | ------- | ---------- | --------- | ------ |
| List       | Yes     | Yes     | Yes        | No        | `[]`   |
| Tuple      | Yes     | No      | Yes        | No        | `()`   |
| Set        | No      | Yes     | No         | No        | `{}`   |
| Dictionary | No      | Yes     | No (keys)  | Yes       | `{}`   |

---

# Exception & File Handling

## What is Exception Handling in Python?

Exception handling is a mechanism that allows developers to manage and respond to runtime errors in a controlled manner. It enables the program to continue executing or fail gracefully instead of crashing unexpectedly.

### Primary Keywords

- **try**: Block where code that might raise an exception is written
- **except**: Block executed if an exception occurs in the try block
- **else**: Block executed if no exceptions are raised in the try block
- **finally**: Block executed regardless of exceptions (used for cleanup)
- **raise**: Keyword to manually raise an exception

## What is Error Handling in Python?

Error handling refers to the process of anticipating, detecting, and managing errors during program execution. It helps create robust applications by handling unexpected situations gracefully.

### Types of Errors in Python

1. **Syntax Errors**: Violate Python language rules (missing colons, parentheses)
2. **Runtime Errors**: Occur during execution (division by zero, undefined variable)
3. **Logical Errors**: Code runs without crashing but produces incorrect results

## What is an Exception in Python?

An exception is an event that disrupts normal program flow. When raised, Python generates an error message and halts unless caught and handled.

Common causes:

- Invalid input
- File not found errors
- Division by zero
- Accessing undefined variables

## Exception Handling Example

```python
print("----- Exception Handling Example -----")

try:
    # Code that may raise an exception
    num1 = int(input("Enter a numerator: "))
    num2 = int(input("Enter a denominator: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.")
```

**Explanation**:

- The `try` block contains code that may raise exceptions
- The `except` blocks handle specific exceptions with appropriate messages
- The `else` block executes if no exceptions occur
- The `finally` block executes regardless of whether an exception occurred

## What is a File?

A file is a collection of data stored on a computer's filesystem. Files can contain:

- Text data
- Binary data (images, audio, video)
- Structured data

Files are identified by names and extensions (e.g., .txt, .jpg, .mp3).

## The open() Function in Python

The `open()` function opens a file and returns a file object for various operations.

### Syntax

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None)
```

### Parameters

- **file**: File name/path
- **mode**: How to open the file:
  - `'r'`: Read (default)
  - `'w'`: Write (creates or truncates file)
  - `'a'`: Append data to end
  - `'b'`: Binary mode

## What is File Handling in Python?

File handling refers to creating, reading, writing, and manipulating files using built-in functions and methods.

### Common File Operations

1. **Opening**: Using `open()` function
2. **Reading**: Using `read()`, `readline()`, `readlines()`
3. **Writing**: Using `write()`, `writelines()`
4. **Closing**: Using `close()` method
5. **Context managers**: Using `with` statement for automatic handling

## File Handling Example

```python
print("----- File Handling Example -----")

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is an example of file handling.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)
```

**Explanation**:

- The first `with` block opens a file in write mode and writes two lines
- The second `with` block opens the file in read mode and reads its content
- The `with` statement ensures proper file closure, even if errors occur

## Combined Exception and File Handling

```python
print("----- Combined Exception and File Handling -----")

try:
    # Code that may raise an exception
    num1 = int(input("Enter a numerator: "))
    num2 = int(input("Enter a denominator: "))
    result = num1 / num2

    # Writing the result to a file
    with open("result.txt", "w") as file:
        file.write(f"The result of {num1} divided by {num2} is: {result}\n")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except IOError:
    print("Error: An error occurred while handling the file.")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.")
```

**Explanation**:

- The `try` block contains operations that may raise exceptions
- The `except` blocks handle specific exceptions (ZeroDivisionError, ValueError, IOError)
- The `else` block displays the result if no exceptions occur
- The `finally` block indicates execution completion

## Key Points

- Use `try-except` to handle runtime errors gracefully
- Multiple `except` blocks can catch different exception types
- The `finally` block always executes (useful for cleanup)
- Use `with` statement for automatic file handling
- Always handle potential file operation errors
- Close files properly to free system resources

---

## End of Complete Python Learning Guide

This guide covers all fundamental Python concepts from basics to advanced data structures and file handling. Use this as a reference for learning and practicing Python programming.
