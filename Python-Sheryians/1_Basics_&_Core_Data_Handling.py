# What is Python?
# Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.
# Python is widely used for web development, data analysis, artificial intelligence, scientific computing, and more. It has a large standard library and a vibrant ecosystem of third-party packages.
# Example of a simple Python program:
# print("Hello, World!")

# What is interpreter in Python?
# An interpreter in Python is a program that reads and executes Python code line by line. It translates the high-level Python code into machine code that the computer's processor can understand and execute.
# The Python interpreter allows for interactive programming, where you can type and execute code in real-time, making it easy to test and debug code snippets.
# Example of using the Python interpreter:
# >>> print("Hello, World!")

# What is comment in Python?
# A comment in Python is a line that starts with the '#' symbol. It is used to explain the code and is ignored by the Python interpreter during execution.
# Comments are useful for documenting code, making it easier to understand for others (or yourself) when you revisit it later.  
# Example of a comment:
# This is a single-line comment
print("Hello, Python!")  # This is an inline comment

# What is a variable in Python?
# A variable in Python is a named location used to store data in memory. It acts as a container for values that can be changed and manipulated throughout the program.
# Variables are created by assigning a value to a name using the '=' operator.
# Example of a variable:
age = 25  # Here, 'age' is a variable that stores the integer value
print("I am", age, "years old.")

# Rule variables in Python:
# 1. Variable names must start with a letter (a-z, A-Z) or an underscore (_).
# 2. The rest of the variable name can contain letters, digits (0-9), or underscores.
# 3. Variable names are case-sensitive (e.g., 'age' and 'Age' are different variables).
# 4. Variable names cannot be the same as Python reserved keywords (e.g., 'if', 'for', 'while', etc.).
# 5. Variable names should be descriptive and meaningful to enhance code readability.
# Example of valid and invalid variable names:
valid_variable = 10
_invalidVariable = 20  # Invalid: starts with an underscore followed by a digit
# 2ndVariable = 30      # Invalid: starts with a digit
myVariable = 40      # Valid
print("Valid variable value:", valid_variable)
print("My variable value:", myVariable)
print("Invalid variable names cannot be used in code.")
# Note: The invalid variable names are commented out to avoid syntax errors.

# Naming Conventions for Variables in Python:
# 1. Use lowercase letters with words separated by underscores (snake_case) for variable names.
# 2. Avoid using single-character variable names except for counters or iterators.
# 3. Use descriptive names that convey the purpose of the variable.
# Example of naming conventions:
user_name = "Alice"  # Descriptive and follows snake_case
user_age = 30        # Descriptive and follows snake_case
print("User Name:", user_name)
print("User Age:", user_age)

# What are Data Types in Python?
# Data types in Python define the type of data that a variable can hold. Python has several built-in data types, including:
# 1. int: Represents integer values (e.g., 1, -5,
# 2. float: Represents floating-point numbers (e.g., 3.14, -0.001),
# 3. str: Represents strings, which are sequences of characters (e.g., "Hello", 'Python'),
# 4. bool: Represents boolean values, which can be either True or False.
# 5. complex: Represents complex numbers (e.g., 3+4j)

# Example of data types:
integer_var = 10          # int
float_var = 3.14         # float
string_var = "Hello"     # str
boolean_var = True       # bool
complex_var = 2 + 3j    # complex
print("Integer:", integer_var)
print("Float:", float_var)
print("String:", string_var)
print("Boolean:", boolean_var)
print("Complex:", complex_var)


# Explain string and type conversion in Python with examples.
# A string in Python is a sequence of characters enclosed in single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """). Strings are used to represent text data.
# Example of a string:
greeting = "Hello, World!"
print(greeting)
# Type conversion in Python refers to the process of converting a variable from one data type to another. This is often necessary when performing operations that require specific data types.
# Python provides built-in functions for type conversion, such as int(), float(), str(), and bool().
# Example of type conversion with strings:
num_str = "123"          # str
num_int = int(num_str)   # Convert str to int
num_float = float(num_int)  # Convert int to float
print("String to Integer:", num_int)
print("Integer to Float:", num_float)
print("Type of num_str:", type(num_str))
print("Type of num_int:", type(num_int))
print("Type of num_float:", type(num_float))
# Note: Type conversion may lead to data loss if the conversion is not compatible (e.g., converting a float to an int will truncate the decimal part).
# Example of incompatible type conversion:
float_value = 9.99
int_value = int(float_value)  # Convert float to int (data loss)
print("Float to Integer (data loss):", int_value)   
print("Type of int_value:", type(int_value))

# Demonstrate string slicing and indexing with examples.
# String slicing in Python allows you to extract a substring from a string by specifying a range of indices. The syntax for slicing is: string[start:end], where 'start' is the starting index (inclusive) and 'end' is the ending index (exclusive).
# Example of string slicing:
sample_string = "Hello, Python!"
substring = sample_string[7:13]  # Extracting substring "Python"
print("Substring:", substring) # Output: "Python"

# Example of indexing in string:
sample_string = "Python"
first_character = sample_string[0]  # Accessing the first character
last_character = sample_string[-1]   # Accessing the last character
print("First character:", first_character)
print("Last character:", last_character)
# Note: String indices start at 0, and negative indices can be used to access characters from the end of the string.
# Example of slicing with step:
step_slice = sample_string[0:6:2]  # Extracting characters with a step of 2
print("Step slice:", step_slice)
# Example of slicing with omitted indices:
omitted_start = sample_string[:4]  # From start to index 4 (exclusive)
omitted_end = sample_string[2:]    # From index 2 to the end
print("Omitted start slice:", omitted_start)
print("Omitted end slice:", omitted_end)
# Example of reversing a string using slicing:
reversed_string = sample_string[::-1]  # Reversing the string
print("Reversed string:", reversed_string)

# Example bool type conversion
bool_from_int = bool(1)    # Converts integer 1 to True
bool_from_zero = bool(0)   # Converts integer 0 to False
bool_from_str = bool("Hello")  # Non-empty string converts to True
bool_from_empty_str = bool("")   # Empty string converts to False
print("Boolean from int 1:", bool_from_int) 
print("Boolean from int 0:", bool_from_zero)
print("Boolean from non-empty string:", bool_from_str)
print("Boolean from empty string:", bool_from_empty_str)


# Define Implicit and Explicit type conversion with examples.
# Implicit type conversion, also known as type coercion, occurs when Python automatically converts one data type to another without any user intervention. This usually happens during operations involving mixed data types.
# Explicit type conversion, on the other hand, is when the programmer manually converts a variable from one data type to another using built-in functions like int(), float(), str(), etc.  
# Implicit type conversion (type coercion) example
int_num = 5        # int
float_num = 2.5   # float
result = int_num + float_num  # int is implicitly converted to float
print("Result of implicit type conversion (int + float):", result)
print("Type of result:", type(result))
# Explicit type conversion example
str_num = "10"    # str
int_num = int(str_num)  # Explicitly converting str to int
print("Explicitly converted integer:", int_num)
print("Type of explicitly converted integer:", type(int_num))
# Example of string methods
original_string = "  Hello, World!  "
upper_string = original_string.upper()  # Convert to uppercase
lower_string = original_string.lower()  # Convert to lowercase
stripped_string = original_string.strip()  # Remove leading and trailing whitespace
print("Uppercase:", upper_string)
print("Lowercase:", lower_string)
print("Stripped string:", stripped_string)
# Example of string concatenation
str1 = "Hello"
str2 = "World"
concatenated_string = str1 + ", " + str2 + "!"  # Concatenating strings
print("Concatenated string:", concatenated_string)
# Example of string formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."  # Using f-string for formatting
print("Formatted string:", formatted_string)

# Input and Output in Python
# Input in Python is handled using the input() function, which allows users to enter data during program execution. The input() function reads a line from input, converts it into a string, and returns it.
# Example of input:
user_name = input("Enter your name: ")  # Prompting user for input
print("Hello,", user_name + "!")  # Outputting a greeting message
# Output in Python is typically done using the print() function, which displays data to the console or standard output.
# Example of output:
print("This is an example of output in Python.")
# Example of input with type conversion
age_str = input("Enter your age: ")  # Input as string
age_int = int(age_str)  # Converting string to integer
print("You are", age_int, "years old.")  # Outputting the age
# Example of formatted output
height = 88
print(f"Your height is {height} feet.")  # Using f-string for formatted output
# Example of multiple inputs
num1, num2 = input("Enter two numbers separated by space: ").split()
num1 = int(num1)
num2 = int(num2)
sum_result = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum_result)   
