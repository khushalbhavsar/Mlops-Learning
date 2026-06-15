# Functions in Python

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
