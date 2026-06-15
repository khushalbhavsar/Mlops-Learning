# What is exception handling in Python?
# Exception handling in Python is a mechanism that allows developers to manage and respond to runtime errors in a controlled manner. It enables the program to continue executing or to fail gracefully instead of crashing unexpectedly.
# The primary keywords used for exception handling in Python are try, except, else, and finally.
# Here's a brief overview of each keyword:
# - try: This block of code is where you write the code that might raise an exception
# - except: This block of code is executed if an exception occurs in the try block. You can specify the type of exception to catch.
# - else: This block of code is executed if no exceptions are raised in the try block
# - finally: This block of code is executed regardless of whether an exception occurred or not. It is typically used for cleanup actions, such as closing files or releasing resources.
# - raise: This keyword is used to manually raise an exception in your code.

# What is Error Handling in Python?
# Error handling in Python refers to the process of anticipating, detecting, and managing errors that may occur during the execution of a program. It involves using exception handling techniques to catch and respond to errors, ensuring that the program can handle unexpected situations gracefully.
# Error handling is essential for creating robust and reliable applications, as it helps prevent crashes and allows developers to provide meaningful feedback to users when errors occur.
# Type of Errors in Python:
# 1. Syntax Errors: These occur when the code violates the rules of the Python language, such as missing colons or parentheses.
# 2. Runtime Errors: These occur during the execution of the program, such as division by zero or accessing an undefined variable.
# 3. Logical Errors: These occur when the code runs without crashing but produces incorrect results due to flawed logic or incorrect algorithms.

# What is Exception in Python?
# An exception in Python is an event that occurs during the execution of a program that disrupts the normal flow of instructions. When an exception is raised, Python generates an error message and halts the program unless the exception is caught and handled using exception handling techniques.
# Exceptions can be caused by various factors, such as invalid input, file not found errors, or division by zero.
# Python provides a wide range of built-in exceptions, and developers can also create custom exceptions to handle specific error conditions in their applications.

print("----- Exception and Error Handling Example In Python -----")
# Example of Exception and Error Handling in Python:
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
# In this example:
# - The try block contains code that may raise exceptions (e.g., division by zero or invalid input).
# - The except blocks handle specific exceptions (ZeroDivisionError and ValueError) and provide appropriate error messages.
# - The else block executes if no exceptions occur, displaying the result of the division.
# - The finally block executes regardless of whether an exception occurred, indicating that the execution is complete.

# What is File?
# A file is a collection of data or information that is stored on a computer's filesystem. Files can contain various types of data, such as text, images, audio, video, or binary data. They are used to organize and store information for easy access and retrieval.
# Files are typically identified by their names and extensions (e.g., .txt, .jpg, .mp3) and can be created, modified, and deleted using file management operations provided by the operating system or programming languages.

# What is open() function in Python?
# The open() function in Python is a built-in function used to open a file and return a file object. This function allows you to perform various operations on the file, such as reading from it, writing to it, or appending data to it.
# The syntax of the open() function is as follows:
# open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
# - file: The name of the file to be opened (including the path if it's not in the current directory).
# - mode: The mode in which the file is opened. Common modes include:
#   - 'r': Read mode (default) - Opens the file for reading.
#   - 'w': Write mode - Opens the file for writing (creates a new file or truncates an existing file).
#   - 'a': Append mode - Opens the file for appending data to the end.
#   - 'b': Binary mode - Opens the file in binary mode (used for non-text files).

# What is File Handling in Python?
# File handling in Python refers to the process of creating, reading, writing, and manipulating files using built-in functions and methods. Python provides a simple and efficient way to work with files, allowing developers to perform various operations on files stored on the filesystem.
# Common file handling operations in Python include:
# 1. Opening a file: Using the open() function to open a file in different modes (read, write, append, etc.)
# 2. Reading from a file: Using methods like read(), readline(), and readlines() to read data from a file.
# 3. Writing to a file: Using methods like write() and writelines() to write data to a file.
# 4. Closing a file: Using the close() method to close a file and free up system resources.
# 5. Using context managers: Using the with statement to automatically handle file opening and closing.

print("----- Exception Handling Example In Python -----")
# Example of File Handling in Python:
# Writing to a file
with open("example.txt", "w") as file: # Open file in write mode 
    file.write("Hello, World!\n") # Write a line to the file
    file.write("This is an example of file handling in Python.\n") # Write another line to the file
# Reading from a file
with open("example.txt", "r") as file: # Open file in read mode
    content = file.read() # Read the content of the file
    print("File Content:") # Print header
    print(content) # Print the content of the file
# In this example:
# - The first with block opens a file named "example.txt" in write mode ("w") and writes two lines of text to it.
# - The second with block opens the same file in read mode ("r") and reads its content, which is then printed to the console.
# Using context managers (with statement) ensures that the file is properly closed after the operations are completed, even if an error occurs during file handling.
# Note: Make sure to run this code in an environment where you have permission to create and write files.

print("----- Combined Exception and File Handling Example In Python -----")
# This code demonstrates both exception handling and file handling in Python.
try:
    # Code that may raise an exception
    num1 = int(input("Enter a numerator: "))
    num2 = int(input("Enter a denominator: "))
    result = num1 / num2
    # Writing the result to a file
    with open("result.txt", "w") as file: # Open file in write mode
        file.write(f"The result of {num1} divided by {num2} is: {result}\n") # Write result to file
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
# In this combined example:
# - The try block contains code that may raise exceptions (e.g., division by zero or invalid input) and writes the result to a file.
# - The except blocks handle specific exceptions (ZeroDivisionError, ValueError, and IOError) and provide appropriate error messages.
# - The else block executes if no exceptions occur, displaying the result of the division.
# - The finally block executes regardless of whether an exception occurred, indicating that the execution is complete.

