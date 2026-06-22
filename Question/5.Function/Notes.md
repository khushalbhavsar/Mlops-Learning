# Functions in Python (Detailed Explanation)

A **function** is a reusable block of code that performs a specific task. Instead of writing the same code multiple times, you can put it inside a function and call it whenever needed.

---

# Why Use Functions?

### Without Function

```python
a = 10
b = 20
print(a + b)

x = 5
y = 15
print(x + y)
```

Here, the addition logic is repeated.

### With Function

```python
def add(a, b):
    print(a + b)

add(10, 20)
add(5, 15)
```

**Benefits:**

* Code Reusability
* Better Organization
* Easier Debugging
* Reduces Duplication
* Improves Readability

---

# Creating a Function

### Syntax

```python
def function_name(parameters):
    # function body
    # code
```

### Example

```python
def greet():
    print("Hello, Welcome to Python!")

greet()
```

### Output

```text
Hello, Welcome to Python!
```

---

# Parts of a Function

```python
def greet():
    print("Hello")
```

| Part    | Meaning                      |
| ------- | ---------------------------- |
| def     | Keyword to define a function |
| greet   | Function name                |
| ()      | Parameters                   |
| :       | Starts function body         |
| print() | Function code                |

---

# Function with Parameters

Parameters allow functions to accept values.

### Example

```python
def greet(name):
    print("Hello", name)

greet("Khushal")
```

### Output

```text
Hello Khushal
```

### Dry Run

```text
Function Call:
greet("Khushal")

name = "Khushal"

print("Hello", name)

Output:
Hello Khushal
```

---

# Function with Multiple Parameters

```python
def add(a, b):
    print(a + b)

add(10, 20)
```

### Output

```text
30
```

---

# Return Statement

The `return` statement sends a value back to the caller.

### Example

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

### Output

```text
30
```

### Dry Run

```text
add(10,20)

a = 10
b = 20

return 30

result = 30

print(result)
```

---

# Difference Between print() and return

### Using print()

```python
def add(a, b):
    print(a + b)

result = add(10, 20)

print(result)
```

Output:

```text
30
None
```

Why?

```text
print() displays output
Function returns nothing
Default return value = None
```

---

### Using return()

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

---

# Types of Functions

## 1. Built-in Functions

Python already provides them.

```python
print()
len()
max()
min()
sum()
type()
```

Example:

```python
numbers = [1, 2, 3, 4]

print(len(numbers))
```

Output:

```text
4
```

---

## 2. User-defined Functions

Created by programmers.

```python
def square(num):
    return num * num

print(square(5))
```

Output:

```text
25
```

---

# Function Arguments

## 1. Positional Arguments

```python
def student(name, age):
    print(name, age)

student("Khushal", 22)
```

Output:

```text
Khushal 22
```

---

## 2. Keyword Arguments

```python
def student(name, age):
    print(name, age)

student(age=22, name="Khushal")
```

Output:

```text
Khushal 22
```

---

## 3. Default Arguments

```python
def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Khushal")
```

Output:

```text
Hello Guest
Hello Khushal
```

---

# Variable Scope

## Local Variable

Created inside a function.

```python
def test():
    x = 10
    print(x)

test()
```

Output:

```text
10
```

Outside function:

```python
print(x)
```

Output:

```text
NameError
```

---

## Global Variable

```python
x = 100

def show():
    print(x)

show()
```

Output:

```text
100
```

---

# Return Multiple Values

```python
def calculate(a, b):
    return a+b, a-b, a*b

sum1, sub, mul = calculate(10, 5)

print(sum1)
print(sub)
print(mul)
```

Output:

```text
15
5
50
```

---

# Recursive Function

A function calling itself.

### Example: Factorial

```python
def factorial(n):

    if n == 1:
        return 1

    return n * factorial(n-1)

print(factorial(5))
```

### Dry Run

```text
factorial(5)

5 * factorial(4)

5 * 4 * factorial(3)

5 * 4 * 3 * factorial(2)

5 * 4 * 3 * 2 * factorial(1)

5 * 4 * 3 * 2 * 1

120
```

---

# Lambda Function

Small anonymous function.

### Syntax

```python
lambda arguments : expression
```

Example:

```python
square = lambda x: x*x

print(square(5))
```

Output:

```text
25
```

---

# Nested Functions

Function inside another function.

```python
def outer():

    def inner():
        print("Inner Function")

    inner()

outer()
```

Output:

```text
Inner Function
```

---

# Function Example: Even or Odd

```python
def check_even_odd(num):

    if num % 2 == 0:
        return "Even"

    return "Odd"

print(check_even_odd(10))
```

Output:

```text
Even
```

---

# Function Example: Prime Number

```python
def is_prime(n):

    if n <= 1:
        return False

    for i in range(2, n):

        if n % i == 0:
            return False

    return True

print(is_prime(7))
```

Output:

```text
True
```

---
