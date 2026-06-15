# Logic & Conditions Part 1

## Operators and Expressions in Python

Operators are special symbols in Python that perform operations on variables and values. Expressions are combinations of variables, values, and operators that Python evaluates to produce a result.

Python supports various types of operators:

### 1. Arithmetic Operators

Used for mathematical operations: `+` (addition), `-` (subtraction), `*` (multiplication), `/` (division), `%` (modulus), `**` (exponentiation), `//` (floor division)

```python
print(“Arithmetic Operators:”)
a = 10
b = 3
print(“Addition:”, a + b)              # 13
print(“Subtraction:”, a - b)           # 7
print(“Multiplication:”, a * b)        # 30
print(“Division:”, a / b)              # 3.3333...
print(“Modulus:”, a % b)               # 1
print(“Exponentiation:”, a ** b)       # 1000
print(“Floor Division:”, a // b)       # 3
```

### 2. Comparison Operators

Used to compare two values: `==` (equal), `!=` (not equal), `>` (greater than), `<` (less than), `>=` (greater or equal), `<=` (less or equal)

```python
print(“\nComparison Operators:”)
x = 5
y = 10
print(“Equal to:”, x == y)             # False
print(“Not equal to:”, x != y)         # True
print(“Greater than:”, x > y)          # False
print(“Less than:”, x < y)             # True
print(“Greater than or equal to:”, x >= y)  # False
print(“Less than or equal to:”, x <= y)     # True

# String comparison
str1 = “hello”
str2 = “world”
print(“String Equal to:”, str1 == str2)      # False
print(“String Not equal to:”, str1 != str2)  # True
```

### 3. Logical Operators

Used to combine conditional statements: `and`, `or`, `not`

```python
print(“\nLogical Operators:”)
p = True
q = False
print(“Logical AND:”, p and q)        # False
print(“Logical OR:”, p or q)          # True
print(“Logical NOT:”, not p)           # False

# Additional examples
a = 7
b = 12
print(“Logical AND with conditions:”, (a < 10) and (b > 10))  # True
print(“Logical OR with conditions:”, (a > 10) or (b > 10))    # True
print(“Logical NOT with condition:”, not (a < 10))            # False
```

### 4. Assignment Operators

Used to assign values to variables: `=`, `+=`, `-=`, `*=`, `/=`, `%=`, `**=`, `//=`

```python
print(“\nAssignment Operators:”)
c = 5
c += 3  # Equivalent to c = c + 3
print(“Assignment += :”, c)           # 8
c *= 2  # Equivalent to c = c * 2
print(“Assignment *= :”, c)           # 16

# Additional examples
a = 10
print(“Initial a =”, a)               # 10
a += 20
print(“Assignment = :”, a)            # 30
a += 30
print(“Assignment = :”, a)            # 60
```

### 5. Bitwise Operators

Used for bit-level operations: `&` (AND), `|` (OR), `^` (XOR), `~` (NOT), `<<` (left shift), `>>` (right shift)

```python
print(“\nBitwise Operators:”)
m = 6   # Binary: 110
n = 3   # Binary: 011
print(“Bitwise AND:”, m & n)          # 2 (Binary: 010)
print(“Bitwise OR:”, m | n)           # 7 (Binary: 111)
print(“Bitwise XOR:”, m ^ n)          # 5 (Binary: 101)
print(“Bitwise NOT:”, ~m)             # -7
print(“Left Shift:”, m << 1)          # 12 (Binary: 1100)
print(“Right Shift:”, m >> 1)         # 3 (Binary: 011)
```

## Operator Precedence

Operator precedence determines the order in which operations are performed in an expression.

```python
result = 10 + 5 * 2  # Multiplication has higher precedence than addition
print(“Operator Precedence Result:”, result)  # 20
```

## Conditional Statements in Python

Conditional statements are used to perform different actions based on whether a condition is true or false.

### Types of Conditional Statements:

- **if statement**: Executes a block of code if a condition is true
- **elif statement**: Allows you to check multiple conditions
- **else statement**: Executes if none of the previous conditions are true

### If Statement

```python
print(“\nIf Statement:”)
age = int(input(“Enter your age: “))
if age >= 18:
    print(“You are eligible to vote.”)
else:
    print(“You are not eligible to vote.”)
```

### If-Elif-Else Statement

```python
print(“\nIf-Elif-Else Statement:”)
marks = int(input(“Enter your marks: “))
if marks >= 90:
    print(“Grade: A”)
elif marks >= 75:
    print(“Grade: B”)
elif marks >= 60:
    print(“Grade: C”)
else:
    print(“Grade: F”)
```

### Nested If Statement

```python
print(“\nNested If Statement:”)
money = int(input(“Enter the amount you have: “))
if money >= 100:
    if money >= 500:
        print(“You can buy a laptop.”)
    else:
        print(“You can buy a smartphone.”)
else:
    print(“You can buy a snack.”)
```

## Practice Questions

### Q1: Print the Greatest of Two Numbers

```python
print(“\nGreatest of Two Numbers:”)
num1 = int(input(“Enter first number: “))
num2 = int(input(“Enter second number: “))
if num1 > num2:
    print(f”The greatest number is: {num1}”)
else:
    print(f”The greatest number is: {num2}”)
```

### Q2: Gender-based Greeting

Accept gender from user (M/F) and print greeting.

```python
print(“\nGreeting Message Based on Gender:”)
gender = input(“Enter your gender (M/F): “).upper()
if gender == 'M':
    print(“Good Morning Sir”)
elif gender == 'F':
    print(“Good Morning Ma'am”)
else:
    print(“Invalid input. Please enter M or F.”)
```

### Q3: Check if Even or Odd

```python
print(“\nEven or Odd Check:”)
number = int(input(“Enter an integer: “))
if number % 2 == 0:
    print(f”{number} is an even number.”)
else:
    print(f”{number} is an odd number.”)
```

### Q4: Check if Valid Voter

```python
print(“\nVoter Eligibility Check:”)
name = input(“Enter your name: “)
age = int(input(“Enter your age: “))
if age >= 18:
    print(f”Hello {name}, you are a valid voter.”)
else:
    print(f”Hello {name}, you are not a valid voter.”)
```

### Q5: Check Leap Year

```python
print(“\nLeap Year Check:”)
year = int(input(“Enter a year: “))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f”{year} is a leap year.”)
else:
    print(f”{year} is not a leap year.”)
```

### Q6: Temperature Classification

Classify temperature in Celsius:

- Below 0°C → Freezing Cold
- 0°C to 10°C → Very Cold
- 10°C to 20°C → Cold
- 20°C to 30°C → Pleasant
- 30°C to 40°C → Hot
- Above 40°C → Very Hot

```python
print(“\nTemperature Classification:”)
temperature = float(input(“Enter the temperature in Celsius: “))
if temperature < 0:
    print(“Freezing Cold”)
elif 0 <= temperature <= 10:
    print(“Very Cold”)
elif 10 < temperature <= 20:
    print(“Cold”)
elif 20 < temperature <= 30:
    print(“Pleasant”)
elif 30 < temperature <= 40:
    print(“Hot”)
else:
    print(“Very Hot”)
```

**Note:** Indentation is crucial in Python as it defines code blocks. Proper indentation is necessary for correct execution of conditional statements.
