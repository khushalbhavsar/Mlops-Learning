# What is a module in Python?
# A module is a file containing Python code that can define functions, classes, and variables.

# ==========================================
# 1. Import the math module
# ==========================================
import math

print("Math Module Imported")


# ==========================================
# 2. Use sqrt() -> Returns square root
# ==========================================
print("Square Root of 25:", math.sqrt(25))


# ==========================================
# 3. Use factorial() -> Returns factorial
# ==========================================
print("Factorial of 5:", math.factorial(5))


# ==========================================
# 4. Use random.randint() -> Generates random integer
# ==========================================
import random

print("Random Number:", random.randint(1, 10))


# ==========================================
# 5. Import only one function
# ==========================================
from math import pi

print("Value of PI:", pi)


# ==========================================
# 6. Import with alias
# ==========================================
import math as m

print("Power (2^3):", m.pow(2, 3))


# ==========================================
# 7. Create your own module
# File Name: mymodule.py
# ==========================================

def greet(name):
    return f"Hello {name}"


# ==========================================
# 8. Import your module
# (Save the above code in mymodule.py)
# ==========================================
import mymodule

print(mymodule.greet("Khushal"))


# ==========================================
# 9. Use the datetime module
# ==========================================
import datetime

today = datetime.datetime.now()

print("Current Date & Time:", today)


# ==========================================
# 10. Use the os module
# ==========================================
import os

print("Current Working Directory:", os.getcwd())

