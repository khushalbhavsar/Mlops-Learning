# 📘 DAY 7 – Functions + Scope

## 🔹 Functions in Python (Beginner-Friendly Guide)

A **function** in Python is a **block of reusable code** that performs a specific task.
It helps you **avoid repetition**, **organize code**, and **improve readability**.

---

## 1️⃣ Why Use Functions?

✔ Code reusability
✔ Better structure & readability
✔ Easy debugging
✔ Modularity (break big problems into small parts)

---

## 2️⃣ Defining a Function

### Syntax

```python
def function_name(parameters):
    # function body
    return value
```

### Example

```python
def greet():
    print("Hello, Welcome to Python!")
```

Calling the function:

```python
greet()
```

---

## 3️⃣ Function with Parameters

Parameters allow you to pass data into a function.

```python
def greet(name):
    print("Hello", name)

greet("Khushal")
```

Output:

```
Hello Khushal
```

---

## 4️⃣ Function with Return Value

`return` sends a result back to the caller.

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

Output:

```
8
```

---

## 5️⃣ Types of Functions in Python

### 🔹 1. Built-in Functions

Already provided by Python.

```python
print("Hello")
len([1, 2, 3])
type(10)
```

---

### 🔹 2. User-Defined Functions

Created by users.

```python
def square(n):
    return n * n

print(square(4))
```

---

### 🔹 3. Function with Default Arguments

```python
def greet(name="User"):
    print("Hello", name)

greet()
greet("Khushal")
```

---

### 🔹 4. Keyword Arguments

```python
def student(name, age):
    print(name, age)

student(age=21, name="Khushal")
```

---

### 🔹 5. Variable-Length Arguments

#### *args (multiple positional arguments)

```python
def add_numbers(*args):
    return sum(args)

print(add_numbers(1, 2, 3, 4))
```

#### **kwargs (multiple keyword arguments)

```python
def info(**kwargs):
    print(kwargs)

info(name="Khushal", role="Developer")
```

---

## 6️⃣ Lambda (Anonymous) Functions

Small, one-line functions.

```python
square = lambda x: x * x
print(square(5))
```

---

## 7️⃣ Nested Functions (Function inside Function)

```python
def outer():
    def inner():
        print("Inner function")
    inner()

outer()
```

---

## 8️⃣ Scope of Variables

### 🔹 Local Variable

Defined inside a function.

```python
def test():
    x = 10
    print(x)
```

### 🔹 Global Variable

Defined outside the function.

```python
x = 20

def show():
    print(x)
```

---

## 9️⃣ Recursion (Function Calling Itself)

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

Output:

```
120
```

---

## 🔟 `pass` Keyword in Functions

Used when function body is empty.

```python
def future_function():
    pass
```

---

## 📌 Summary

| Concept    | Description                |
| ---------- | -------------------------- |
| `def`      | Defines a function         |
| Parameters | Input values               |
| `return`   | Output value               |
| `*args`    | Multiple arguments         |
| `**kwargs` | Multiple keyword arguments |
| Lambda     | One-line function          |
| Recursion  | Function calling itself    |

---

## 📝 Practice Problems

Learn all about functions by answering the questions below:

1. **Basic Function Syntax** – Write a function to calculate and return the square of a number.
2. **Function with Multiple Parameters** – Create a function that takes two numbers as parameters and returns their sum.
3. **Polymorphism in Functions** – Write a function `multiply` that multiplies two numbers, but can also accept and multiply strings.
4. **Function Returning Multiple Values** – Create a function that returns both the area and circumference of a circle given its radius.
5. **Default Parameter Value** – Write a function that greets a user. If no name is provided, it should greet with a default name.
6. **Lambda Function** – Create a lambda function to compute the cube of a number.
7. **Function with `*args`** – Write a function that takes variable number of arguments and returns their sum.
8. **Function with `**kwargs`** – Create a function that accepts any number of keyword arguments and prints them in the format `key: value`.
9. **Generator Function with `yield`** – Write a generator function that yields even numbers up to a specified limit.
10. **Recursive Function** – Create a recursive function to calculate the factorial of a number.

Below is a **clean, beginner-to-intermediate friendly solution set** for **all 10 function problems**, with **short explanations and correct Python code**.

---

## 1️⃣ Basic Function Syntax

**Problem:** Calculate and return the square of a number.

```python
def square(num):
    return num * num

print(square(5))
```

✅ Output:

```
25
```

---

## 2️⃣ Function with Multiple Parameters

**Problem:** Return the sum of two numbers.

```python
def add(a, b):
    return a + b

print(add(10, 20))
```

✅ Output:

```
30
```

---

## 3️⃣ Polymorphism in Functions

**Problem:** Multiply numbers OR repeat strings.

```python
def multiply(a, b):
    return a * b

print(multiply(3, 4))      # numbers
print(multiply("Hi ", 3))  # string
```

✅ Output:

```
12
Hi Hi Hi 
```

📌 Python supports **dynamic typing**, so the same function works for different data types.

---

## 4️⃣ Function Returning Multiple Values

**Problem:** Return area and circumference of a circle.

```python
import math

def circle_details(radius):
    area = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    return area, circumference

a, c = circle_details(7)
print(a, c)
```

✅ Output:

```
153.94 43.98
```

📌 Python returns **multiple values as a tuple**.

---

## 5️⃣ Default Parameter Value

**Problem:** Greet user with a default name.

```python
def greet(name="User"):
    return f"Hello, {name}!"

print(greet())
print(greet("Khushal"))
```

✅ Output:

```
Hello, User!
Hello, Khushal!
```

---

## 6️⃣ Lambda Function

**Problem:** Compute the cube of a number.

```python
cube = lambda x: x ** 3
print(cube(4))
```

✅ Output:

```
64
```

📌 Lambda functions are **single-line anonymous functions**.

---

## 7️⃣ Function with `*args`

**Problem:** Sum variable number of arguments.

```python
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4, 5))
```

✅ Output:

```
15
```

📌 `*args` stores arguments as a **tuple**.

---

## 8️⃣ Function with `**kwargs`

**Problem:** Print key-value pairs.

```python
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_details(name="Khushal", role="Developer", city="Pune")
```

✅ Output:

```
name: Khushal
role: Developer
city: Pune
```

📌 `**kwargs` stores data as a **dictionary**.

---

## 9️⃣ Generator Function with `yield`

**Problem:** Yield even numbers up to a limit.

```python
def even_numbers(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_numbers(10):
    print(num)
```

✅ Output:

```
2
4
6
8
10
```

📌 `yield` returns values **one at a time** (memory efficient).

---

## 🔟 Recursive Function

**Problem:** Calculate factorial using recursion.

```python
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

✅ Output:

```
120
```

📌 A recursive function **calls itself** until a base condition is met.

---

## 🧠 Quick Summary Table

| Concept      | Key Idea                       |
| ------------ | ------------------------------ |
| `def`        | Define function                |
| Return       | Send result back               |
| Polymorphism | Same function, different types |
| `*args`      | Multiple positional arguments  |
| `**kwargs`   | Multiple keyword arguments     |
| Lambda       | One-line function              |
| `yield`      | Generator                      |
| Recursion    | Function calls itself          |

---

If you want next:
✅ **Interview Q&A on functions**
✅ **Real-world examples (DevOps / Automation)**
✅ **Functions vs Methods**
✅ **50 practice problems with solutions**

Just say the word 🚀
