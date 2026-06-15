# Basics & Core Data Handling

## What is Python?

Python is a high-level, interpreted programming language known for its simplicity and readability. It supports multiple programming paradigms, including procedural, object-oriented, and functional programming.

Python is widely used for web development, data analysis, artificial intelligence, scientific computing, and more. It has a large standard library and a vibrant ecosystem of third-party packages.

Example of a simple Python program:

```python
print("Hello, World!")
```

## What is an Interpreter in Python?

An interpreter in Python is a program that reads and executes Python code line by line. It translates the high-level Python code into machine code that the computer's processor can understand and execute.

The Python interpreter allows for interactive programming, where you can type and execute code in real-time, making it easy to test and debug code snippets.

```python
>>> print("Hello, World!")
```

## What is a Comment in Python?

A comment in Python is a line that starts with the '#' symbol. It is used to explain the code and is ignored by the Python interpreter during execution. Comments are useful for documenting code.

Example of comments:

```python
# This is a single-line comment
print("Hello, Python!")  # This is an inline comment
```

## What is a Variable in Python?

A variable in Python is a named location used to store data in memory. It acts as a container for values that can be changed and manipulated throughout the program.

Variables are created by assigning a value to a name using the '=' operator.

```python
age = 25  # Here, 'age' is a variable that stores the integer value
print("I am", age, "years old.")
```

## Variable Naming Rules

1. Variable names must start with a letter (a-z, A-Z) or an underscore (\_)
2. The rest can contain letters, digits (0-9), or underscores
3. Variable names are case-sensitive (e.g., 'age' and 'Age' are different)
4. Cannot use Python reserved keywords (e.g., 'if', 'for', 'while')
5. Should be descriptive and meaningful to enhance readability

```python
valid_variable = 10
myVariable = 40      # Valid
# 2ndVariable = 30   # Invalid: starts with a digit

print("Valid variable value:", valid_variable)
print("My variable value:", myVariable)
```

## Variable Naming Conventions

1. Use lowercase letters with underscores (snake_case)
2. Avoid single-character names except for counters
3. Use descriptive names that convey purpose

```python
user_name = "Alice"  # Descriptive and follows snake_case
user_age = 30        # Descriptive and follows snake_case
print("User Name:", user_name)
print("User Age:", user_age)
```

## Data Types in Python

Python has several built-in data types:

- **int**: Integer values (e.g., 1, -5)
- **float**: Floating-point numbers (e.g., 3.14, -0.001)
- **str**: Strings (sequences of characters)
- **bool**: Boolean values (True or False)
- **complex**: Complex numbers (e.g., 3+4j)

```python
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
```

## String and Type Conversion

A string in Python is a sequence of characters enclosed in single quotes, double quotes, or triple quotes. Strings are used to represent text data.

Type conversion refers to the process of converting a variable from one data type to another. Python provides built-in functions like `int()`, `float()`, `str()`, and `bool()`.

```python
greeting = "Hello, World!"
print(greeting)

num_str = "123"          # str
num_int = int(num_str)   # Convert str to int
num_float = float(num_int)  # Convert int to float

print("String to Integer:", num_int)
print("Integer to Float:", num_float)
print("Type of num_str:", type(num_str))
print("Type of num_int:", type(num_int))
print("Type of num_float:", type(num_float))
```

**Note**: Type conversion may lead to data loss (e.g., converting a float to int truncates the decimal).

```python
float_value = 9.99
int_value = int(float_value)  # Data loss
print("Float to Integer (data loss):", int_value)
print("Type of int_value:", type(int_value))
```

## String Slicing and Indexing

String slicing allows you to extract a substring by specifying a range of indices. The syntax is `string[start:end]`.

```python
sample_string = "Hello, Python!"
substring = sample_string[7:13]  # Extracting "Python"
print("Substring:", substring)

# Indexing
first_character = sample_string[0]  # First character
last_character = sample_string[-1]  # Last character
print("First character:", first_character)
print("Last character:", last_character)

# Slicing with step
step_slice = sample_string[0:6:2]  # Every 2nd character
print("Step slice:", step_slice)

# Slicing with omitted indices
omitted_start = sample_string[:4]  # From start to index 4
omitted_end = sample_string[2:]    # From index 2 to end
print("Omitted start slice:", omitted_start)
print("Omitted end slice:", omitted_end)

# Reversing a string
reversed_string = sample_string[::-1]
print("Reversed string:", reversed_string)
```

## Boolean Type Conversion

```python
bool_from_int = bool(1)         # True
bool_from_zero = bool(0)        # False
bool_from_str = bool("Hello")   # True (non-empty string)
bool_from_empty_str = bool("")  # False (empty string)

print("Boolean from int 1:", bool_from_int)
print("Boolean from int 0:", bool_from_zero)
print("Boolean from non-empty string:", bool_from_str)
print("Boolean from empty string:", bool_from_empty_str)
```

## Implicit vs Explicit Type Conversion

**Implicit type conversion** (type coercion) occurs when Python automatically converts one data type to another.

**Explicit type conversion** is when the programmer manually converts using built-in functions.

```python
# Implicit conversion
int_num = 5
float_num = 2.5
result = int_num + float_num  # int converted to float
print("Result of implicit conversion:", result)
print("Type of result:", type(result))

# Explicit conversion
str_num = "10"
int_num = int(str_num)
print("Explicitly converted integer:", int_num)
print("Type:", type(int_num))
```

## String Methods

```python
original_string = "  Hello, World!  "
upper_string = original_string.upper()      # Uppercase
lower_string = original_string.lower()      # Lowercase
stripped_string = original_string.strip()   # Remove whitespace

print("Uppercase:", upper_string)
print("Lowercase:", lower_string)
print("Stripped string:", stripped_string)
```

## String Concatenation and Formatting

```python
str1 = "Hello"
str2 = "World"
concatenated = str1 + ", " + str2 + "!"
print("Concatenated:", concatenated)

# f-string formatting
name = "Alice"
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print("Formatted string:", formatted_string)
```

## Input and Output in Python

Input in Python is handled using the `input()` function, which reads user input as a string.

Output is done using the `print()` function.

```python
user_name = input("Enter your name: ")
print("Hello,", user_name + "!")

print("This is an example of output in Python.")

age_str = input("Enter your age: ")
age_int = int(age_str)
print("You are", age_int, "years old.")

height = 88
print(f"Your height is {height} feet.")

num1, num2 = input("Enter two numbers separated by space: ").split()
num1 = int(num1)
num2 = int(num2)
sum_result = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum_result)
```
