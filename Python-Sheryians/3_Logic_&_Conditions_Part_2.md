# Logic & Conditions Part 2

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

## Practice Questions

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
