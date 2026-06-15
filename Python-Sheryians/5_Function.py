# What is Function?
# A function is a block of reusable code that performs a specific task.
# Functions help in organizing code, improving readability, and avoiding repetition.
# Functions can take inputs (parameters) and can return outputs (results).
# def keyword is used to define a function in Python.

# Defining a Function
def greet(name):    
    """This function greets the person passed as a parameter."""
    return f"Hello, {name}!"    
# Calling a Function
print(greet("Alice"))  # Output: Hello, Alice!

# Function parameters and Arguments: 
# Parameters are the variables listed inside the parentheses in the function definition.
# Arguments are the values passed to the function when it is called.
def add(a, b):
    """This function returns the sum of two numbers."""
    print(f"Adding {a} and {b}")
    return a + b
result = add(5, 3)
print(f"Result: {result}")  # Output: Result: 8

# Type of Arguments:
# 1. Positional Arguments   
def multiply(x, y):
    return x * y
print(multiply(4, 5))  # Output: 20

# 2. Keyword Arguments
def divide(dividend, divisor):
    return dividend / divisor
print(divide(divisor=2, dividend=10))  # Output: 5.0

# 3. Default Arguments
def power(base, exponent=2):
    return base ** exponent
print(power(3))        # Output: 9 (3^2)
print(power(2, 3))     # Output: 8 (2^3)

# Question: Check palindrome using function
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


# What is return and print?
# The print() function outputs data to the console or terminal.
# The return statement is used in functions to send a result back to the caller.
def square(num):
    """This function returns the square of a number."""
    return num * num
print(square(4))  # Output: 16
# Here, square(4) returns 16, which is then printed to the console.

