# What is while loop in Python?
# A while loop in Python repeatedly executes a block of code as long as a specified condition is true. It is useful when the number of iterations is not predetermined and depends on dynamic conditions.
# Syntax of while loop:
# while condition:
#     # code block to be executed

# Example of while loop:
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Increment the count to avoid infinite loop

# Example of using while loop with break statement:
print("\nWhile Loop with break statement:")
num = 1
while num <= 10:
    if num == 6:
        print("Breaking the loop at num =", num)
        break  # Exits the loop when num is 6
    print(num)
    num += 1

# Example of using while loop with continue statement:
print("\nWhile Loop with continue statement:")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skips the rest of the loop for even numbers
    print(num)  # Prints only odd numbers

# Question :  Separate each digit of a number and print it on the new line
number = int(input("Enter a number: "))
print("The digits are:")
while number > 0:
    digit = number % 10  # Get the last digit
    print(digit)  # Print the digit
    number = number // 10  # Remove the last digit

# Question : Accept a number and print its reverse
num = int(input("Enter a number to reverse: "))
reversed_num = 0
while num > 0:
    digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Build the reversed number
    num = num // 10  # Remove the last digit
print(f"The reversed number is: {reversed_num}")

# Question : Accept a number and check if it is a pallindromic number (If number and its reverse are equal?
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

# Question :  Create a random number guessing game with python.
import random
random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
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