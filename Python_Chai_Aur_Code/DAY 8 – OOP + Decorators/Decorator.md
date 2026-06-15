# 🧠 Decorators in Python

## What is a Decorator?

A **decorator** is a function that:

- Takes another function as input
- Adds extra behavior
- Returns a new function

> 👉 **Without modifying the original function**

---

## Basic Syntax

```python
@decorator
def my_function():
    pass
```

This is equivalent to:

```python
my_function = decorator(my_function)
```

---

## 📝 Practice Problems

### 🔹 Problem 1: Timing Function Execution

**Goal:** Measure how long a function takes to execute.

**Concepts Used:**
- `time.time()`
- Function wrapping

```python
import time  # Import time module to measure execution time


# Decorator function
# It takes another function as input
def timer(func):

    # Wrapper function that wraps the original function
    # *args   → positional arguments
    # **kwargs → keyword arguments
    def wrapper(*args, **kwargs):

        # Record the start time before function execution
        start = time.time()

        # Call the original function with given arguments
        result = func(*args, **kwargs)

        # Record the end time after function execution
        end = time.time()

        # Calculate and print total execution time
        print(f"{func.__name__} ran in {end - start} time")

        # Return the result of the original function
        return result

    # Return the wrapper function
    return wrapper


# Apply the timer decorator
# Same as: example_function = timer(example_function)
@timer
def example_function(n):

    # Pause execution for n seconds (simulates a slow function)
    time.sleep(n)


# Call the decorated function
# This actually calls wrapper()
example_function(2)
```

---

### 🔹 Problem 2: Debugging Function Calls

**Goal:** Print function name and arguments passed.

**Concepts Used:**
- `*args` and `**kwargs`
- `func.__name__`

```python
# Decorator function
# It takes another function as an argument
def debug(func):

    # Wrapper function that wraps the original function
    # *args  -> positional arguments
    # **kwargs -> keyword arguments
    def wrapper(*args, **kwargs):

        # Convert positional arguments into a readable string
        # Example: args = ("chai",) → "chai"
        args_value = ', '.join(str(arg) for arg in args)

        # Convert keyword arguments into a readable string
        # Example: kwargs = {"greeting": "hanji "}
        # Result: "greeting=hanji "
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.items())

        # Print function name and its arguments for debugging
        print(
            f"calling: {func.__name__} "
            f"with args {args_value} "
            f"and kwargs {kwargs_value}"
        )

        # Call the original function with the same arguments
        return func(*args, **kwargs)

    # Return the wrapper function
    return wrapper


# Apply debug decorator to hello function
# Same as: hello = debug(hello)
@debug
def hello():
    # Function body
    print("hello")


# Apply debug decorator to greet function
@debug
def greet(name, greeting="Hello"):
    # Print greeting message
    print(f"{greeting}, {name}")


# Call hello() → actually calls wrapper()
hello()

# Call greet() with positional and keyword arguments
greet("chai", greeting="hanji ")
```

---

### 🔹 Problem 3: Cache Return Values

**Goal:** Store results so repeated calls with same arguments are faster.

**Concepts Used:**
- Dictionary as cache
- Function arguments as key

```python
import time  # Import time module to simulate a slow function


# Decorator function for caching
# It stores previously computed results
def cache(func):

    # Dictionary to store cached values
    # Key   → function arguments (args)
    # Value → result returned by function
    cache_value = {}

    # This print shows the empty cache when decorator is applied
    print(cache_value)

    # Wrapper function
    def wrapper(*args):

        # Check if the arguments already exist in cache
        # args is a tuple (hashable, so it can be used as a key)
        if args in cache_value:
            # If result is cached, return it directly
            return cache_value[args]

        # If not cached, call the original function
        result = func(*args)

        # Store the result in cache dictionary
        cache_value[args] = result

        # Return the newly computed result
        return result

    # Return the wrapper function
    return wrapper


# Apply cache decorator
# Same as: long_running_function = cache(long_running_function)
@cache
def long_running_function(a, b):

    # Simulate a long computation (4 seconds delay)
    time.sleep(4)

    # Return the sum of a and b
    return a + b


# First call → takes 4 seconds (not cached)
print(long_running_function(2, 3))

# Second call with same arguments → instant (cached result)
print(long_running_function(2, 3))

# New arguments → takes 4 seconds again
print(long_running_function(4, 3))
