# Logic & Conditions Part 3

## What is a While Loop in Python?

A while loop in Python repeatedly executes a block of code as long as a specified condition is true. It's useful when the number of iterations is not predetermined and depends on dynamic conditions.

### Syntax

```python
while condition:
    # code block to be executed
```

## Basic While Loop Example

```python
count = 1
while count <= 5:
    print(f"Count is: {count}")
    count += 1  # Increment to avoid infinite loop
```

## While Loop with Break Statement

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

## While Loop with Continue Statement

```python
print("\nWhile Loop with continue statement:")
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num)  # Print only odd numbers
```

## Practice Questions

### Q1: Separate Each Digit of a Number

```python
number = int(input("Enter a number: "))
print("The digits are:")
while number > 0:
    digit = number % 10  # Get the last digit
    print(digit)
    number = number // 10  # Remove the last digit
```

### Q2: Reverse a Number

```python
num = int(input("Enter a number to reverse: "))
reversed_num = 0
while num > 0:
    digit = num % 10  # Get the last digit
    reversed_num = reversed_num * 10 + digit  # Build reversed number
    num = num // 10  # Remove the last digit
print(f"The reversed number is: {reversed_num}")
```

### Q3: Check if Palindromic Number

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

### Q4: Number Guessing Game

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

## Key Points

- While loops continue as long as a condition is true
- Always increment/change the loop variable to avoid infinite loops
- Use `break` to exit a loop early
- Use `continue` to skip to the next iteration
- While loops are ideal when the number of iterations is unknown
