# Exception and File Handling in Python

## What is Exception Handling in Python?

Exception handling is a mechanism that allows developers to manage and respond to runtime errors in a controlled manner. It enables the program to continue executing or fail gracefully instead of crashing unexpectedly.

### Primary Keywords

- **try**: Block where code that might raise an exception is written
- **except**: Block executed if an exception occurs in the try block
- **else**: Block executed if no exceptions are raised in the try block
- **finally**: Block executed regardless of exceptions (used for cleanup)
- **raise**: Keyword to manually raise an exception

## What is Error Handling in Python?

Error handling refers to the process of anticipating, detecting, and managing errors during program execution. It helps create robust applications by handling unexpected situations gracefully.

### Types of Errors in Python

1. **Syntax Errors**: Violate Python language rules (missing colons, parentheses)
2. **Runtime Errors**: Occur during execution (division by zero, undefined variable)
3. **Logical Errors**: Code runs without crashing but produces incorrect results

## What is an Exception in Python?

An exception is an event that disrupts normal program flow. When raised, Python generates an error message and halts unless caught and handled.

Common causes:

- Invalid input
- File not found errors
- Division by zero
- Accessing undefined variables

## Exception Handling Example

```python
print("----- Exception Handling Example -----")

try:
    # Code that may raise an exception
    num1 = int(input("Enter a numerator: "))
    num2 = int(input("Enter a denominator: "))
    result = num1 / num2
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.")
```

**Explanation**:

- The `try` block contains code that may raise exceptions
- The `except` blocks handle specific exceptions with appropriate messages
- The `else` block executes if no exceptions occur
- The `finally` block executes regardless of whether an exception occurred

## What is a File?

A file is a collection of data stored on a computer's filesystem. Files can contain:

- Text data
- Binary data (images, audio, video)
- Structured data

Files are identified by names and extensions (e.g., .txt, .jpg, .mp3).

## The open() Function in Python

The `open()` function opens a file and returns a file object for various operations.

### Syntax

```python
open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None)
```

### Parameters

- **file**: File name/path
- **mode**: How to open the file:
  - `'r'`: Read (default)
  - `'w'`: Write (creates or truncates file)
  - `'a'`: Append data to end
  - `'b'`: Binary mode

## What is File Handling in Python?

File handling refers to creating, reading, writing, and manipulating files using built-in functions and methods.

### Common File Operations

1. **Opening**: Using `open()` function
2. **Reading**: Using `read()`, `readline()`, `readlines()`
3. **Writing**: Using `write()`, `writelines()`
4. **Closing**: Using `close()` method
5. **Context managers**: Using `with` statement for automatic handling

## File Handling Example

```python
print("----- File Handling Example -----")

# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is an example of file handling.\n")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:")
    print(content)
```

**Explanation**:

- The first `with` block opens a file in write mode and writes two lines
- The second `with` block opens the file in read mode and reads its content
- The `with` statement ensures proper file closure, even if errors occur

## Combined Exception and File Handling

```python
print("----- Combined Exception and File Handling -----")

try:
    # Code that may raise an exception
    num1 = int(input("Enter a numerator: "))
    num2 = int(input("Enter a denominator: "))
    result = num1 / num2

    # Writing the result to a file
    with open("result.txt", "w") as file:
        file.write(f"The result of {num1} divided by {num2} is: {result}\n")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
except IOError:
    print("Error: An error occurred while handling the file.")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.")
```

**Explanation**:

- The `try` block contains operations that may raise exceptions
- The `except` blocks handle specific exceptions (ZeroDivisionError, ValueError, IOError)
- The `else` block displays the result if no exceptions occur
- The `finally` block indicates execution completion

## Key Points

- Use `try-except` to handle runtime errors gracefully
- Multiple `except` blocks can catch different exception types
- The `finally` block always executes (useful for cleanup)
- Use `with` statement for automatic file handling
- Always handle potential file operation errors
- Close files properly to free system resources
