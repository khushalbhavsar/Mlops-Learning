# What is Loops in Python?
# Loops in Python are used to execute a block of code repeatedly as long as a certain condition is met. The main types of loops in Python are for loops and while loops.
# Types of loops:   
# 1. for loop: Used to iterate over a sequence (like a list, tuple, dictionary, set, or string) a fixed number of times.
# 2. while loop: Repeats a block of code as long as a specified condition is true.

# range() function: The range() function generates a sequence of numbers, which is commonly used in for loops. It can take one, two, or three arguments:
# 1. range(stop): Generates numbers from 0 to stop-1.
# 2. range(start, stop): Generates numbers from start to stop-1.
# 3. range(start, stop, step): Generates numbers from start to stop-1, incrementing by step.

# Example of for loop:
print("For Loop Example:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Example of while loop:
print("\nWhile Loop Example:")
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1

# Example of using range() in for loop:
print("\nUsing range() in For Loop:")
for num in range(1, 6): # Generates numbers from 1 to 5
    print(num) # Prints numbers 1 to 5

# Example of nested loops:
print("\nNested Loop Example:")
for i in range(1, 4): # Outer loop from 1 to 3
    for j in range(1, 4): # Inner loop from 1 to 3
        print(f"i: {i}, j: {j}") # Prints combinations of i and j

# Question : Print 5 table using range() function.print("\n5 Table:")
print("\n5 Table:")
for i in range(1, 11):  # From 1 to 10
    print(f"5 x {i} = {5 * i}")  # Prints 5 times i 

# Example loops for string:
print("\nLooping through a string:")
my_string = "Hello World 2026"
# above using range() function
print("\nLooping through a string using range():")  
for i in range(len(my_string)):
    print(my_string[i])  # Prints each character in the string using index
print("\nLooping through a string directly:") # using direct iteration
for char in my_string:
    print(char)  # Prints each character in the string

# Example loops with break and continue:
# The break statement is used to exit a loop prematurely when a certain condition is met, while the continue statement is used to skip the current iteration and move to the next one.
print("\nLoop with break statement:")
for i in range(1, 11):
    if i == 6:
        print("Breaking the loop at i =", i)
        break  # Exits the loop when i is 6
    else:
        print(i)  # Prints numbers from 1 to 5
print("\nLoop with continue statement:")
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skips the even numbers
    print(i)  # Prints only odd numbers

# Example of else with loops:
print("\nFor loop with else statement:")
for i in range(1, 6):
    print(i)
else:
    print("Loop completed successfully!")

# Question : Accept an integer and Print hello world n times
n = int(input("Enter an integer: "))
print(f"Printing 'Hello, World!' {n} times:")
for i in range(n):
    print("Hello, World!")

# Question : Print natural number up to n 
n = int(input("Enter a natural number n: "))
print(f"Natural numbers up to {n}:")
for i in range(1, n + 1):
    print(i)   

# Question : Reverse for loop. Print n to 1 
n = int(input("Enter a natural number n: "))
print(f"Natural numbers from {n} to 1:")
for i in range(n, 0, -1): # Reverse order 
    print(i)

# Question : Take a number as input and print its table 
num = int(input("Enter a number to print its table: "))
print(f"Table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Question :  Sum up to n terms
n = int(input("Enter a natural number n: "))
sum_n = 0
for i in range(1, n + 1):
    sum_n += i
print(f"Sum of first {n} natural numbers is: {sum_n}")

# Question : Factorial of a number 
n = int(input("Enter a natural number n: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"Factorial of {n} is: {factorial}")

# Question: Print all the factors of a number 
n = int(input("Enter a natural number n: "))
print(f"Factors of {n} are:")
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# Question : Print the sum of all even & odd numbers in a range separately
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

# Question : Accept a number and check if it a perfect number or not. A number whose sum of factors is equal to the number itself Ex - 6 = 1, 2, 3 = 6
n = int(input("Enter a natural number n: "))
sum_of_factors = 0
for i in range(1, n):
    if n % i == 0:
        sum_of_factors += i
if sum_of_factors == n:
    print(f"{n} is a perfect number.")
else:
    print(f"{n} is not a perfect number.")

# Question : Check wether the number is prime or not 
n = int(input("Enter a natural number n: "))
is_prime = True
if n <= 1:
    is_prime = False
else:
    for i in range(2, int(n**0.5) + 1): # Check for factors from 2 to sqrt(n)
        if n % i == 0: # If n is divisible by any number in this range, it is not prime
            is_prime = False # Set is_prime to False if a factor is found
            break
if is_prime:
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

# Question : Reverse a string without using in build functions.
string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
print(f"Reversed string: {reversed_string}")

# Question : Check string is Palindrome or not
string = input("Enter a string: ")
reversed_string = ""
for char in string:
    reversed_string = char + reversed_string
if string == reversed_string:
    print(f"{string} is a palindrome.")
else:
    print(f"{string} is not a palindrome.")

# Question : Count all letters, digits, and special symbols from a given string Given: str1 = "P@#yn26at^&i5ve"
# Expected Outcome:
# Total counts of chars, digits, and symbols
# Chars = 8
# Digits = 3
# Symbol = 4
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
