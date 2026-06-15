# 📘 DAY 3 – Python Internals + Numbers

> A comprehensive guide to understanding how Python works under the hood, numeric types, comparisons, and the math library.

---

## 📑 Table of Contents

1. [Python Internals: How Python Really Works](#-part-1-python-internals---how-python-really-works)
2. [Python Internal Working with Different Data Types](#-part-2-python-internal-working-with-different-data-types)
3. [Numbers in Python](#-part-3-numbers-in-python)
4. [repr() vs str() vs print()](#-part-4-repr-vs-str-vs-print)
5. [Comparisons in Python](#-part-5-comparisons-in-python)
6. [Python Math Library](#-part-6-python-math-library)
7. [Quick Reference Summary](#-part-7-quick-reference-summary)

---

---

# 🔧 PART 1: Python Internals - How Python Really Works

---

## 🔍 1.1 High-Level Flow (Big Picture)

![Image](https://iqratechnology.com/wp-content/uploads/2024/09/Python-Program-Execution-1.png)

![Image](https://miro.medium.com/1%2A1athPfdP9St4mkB_hElM6g.png)

![Image](https://ayandas.me/assets/posts_res/7/process.jpg)

When you run a Python program, this is what happens behind the scenes:

```
.py file
    ↓
Lexing & Parsing
    ↓
Bytecode (.pyc)
    ↓
Python Virtual Machine (PVM)
    ↓
Execution
```

---

## 🔤 1.2 Source Code → Tokens (Lexical Analysis)

Python first **reads your code line by line** and breaks it into **tokens**:

```python
x = 10
```

**Tokens become:**

| Token | Type       |
|-------|------------|
| `x`   | IDENTIFIER |
| `=`   | OPERATOR   |
| `10`  | INTEGER    |

📌 This phase only checks **syntax structure**, not logic.

---

## 🌳 1.3 Parsing → Abstract Syntax Tree (AST)

![Image](https://earthly.dev/blog/assets/images/python-ast/ehoUfLn.png)

![Image](https://educative.io/api/edpresso/shot/5776472825921536/image/5348039234945024.png)

Tokens are converted into an **AST (Abstract Syntax Tree)**.

**Example:**

```python
x = 10 + 5
```

**AST represents:**

- Assignment
- Binary operation (`+`)
- Operands (`10`, `5`)

👉 This makes Python understand *what* the code means, not just how it looks.

---

## ⚙️ 1.4 Compilation → Bytecode (.pyc)

![Image](https://cdn-blog.adafruit.com/uploads/2022/01/Untitled2-10.jpg)

![Image](https://formats.kaitai.io/python_pyc_27/python_pyc_27.svg)

Python compiles AST into **bytecode**, which is:

- ✅ Platform-independent
- ✅ Low-level
- ✅ Stored in `__pycache__/`

**View bytecode using:**

```python
import dis
dis.dis("x = 10 + 5")
```

**Bytecode example:**

```
LOAD_CONST
LOAD_CONST
BINARY_ADD
STORE_NAME
```

⚡ This makes Python **faster than pure interpretation**.

---

## 🖥️ 1.5 Python Virtual Machine (PVM) – The Real Executor

![Image](https://jasonleaster.github.io/images/img_for_2016_02_21/frame.png)

![Image](https://neerajkarimpuzha.wordpress.com/wp-content/uploads/2011/09/asd.png)

The **PVM**:

- Reads bytecode **instruction by instruction**
- Executes it at runtime
- Manages stack, memory, function calls

👉 Python is often called **"interpreted"**, but technically it is:

> **Compiled to bytecode + interpreted by PVM**

---

## 💾 1.6 Memory Management

![Image](https://files.realpython.com/media/memory_management_3.52bffbf302d3.png)

![Image](https://miro.medium.com/v2/resize%3Afit%3A1400/1%2ALAt8e9s_ggZnHkI5Sz5QiQ.png)

Python handles memory automatically using:

### ✅ Reference Counting

```python
a = []
b = a
```

- Object has **2 references**
- Deleted when count → 0

### ♻️ Garbage Collector

- Cleans **circular references**
- Uses generational GC (young → old objects)

📌 You never manually `free()` memory like in C/C++.

---

## 📊 1.7 Stack vs Heap

| Area  | What it Stores                  |
|-------|--------------------------------|
| Stack | Function calls, local variables |
| Heap  | Objects, lists, dicts, classes  |

```python
def fun():
    x = 10   # reference on stack, object on heap
```

---

## ⏱️ 1.8 Why Python Feels Slow (But Isn't Always)

**Reasons Python is slower:**

- Dynamic typing
- Runtime checks
- Interpreter overhead

**How Python gains speed:**

- C extensions (NumPy, Pandas)
- JIT compilation (PyPy)
- Async & multiprocessing

---

---

# 🔁 PART 2: Python Internal Working with Different Data Types

---

## 📋 2.0 Execution Flow

We'll follow this flow for every data type:

```
Source Code → Compiler → Bytecode → PVM → Output
```

---

## 🔢 2.1 Integer (`int`) Data Type

### 🧾 Source Code

```python
a = 10
b = 20
c = a + b
print(c)
```

### ⚙️ Internal Working

| Step | Description |
|------|-------------|
| **Compiler** | Checks syntax, converts to bytecode |
| **Bytecode** | `LOAD_CONST 10`, `STORE_NAME a`, `LOAD_CONST 20`, `STORE_NAME b`, `LOAD_NAME a`, `LOAD_NAME b`, `BINARY_ADD`, `STORE_NAME c` |
| **PVM** | Fetches values from memory, performs integer addition |

### ✅ Output

```
30
```

📌 `int` objects are stored in **heap**, references are handled by PVM.

---

## 🔢 2.2 Floating Point (`float`) Data Type

### 🧾 Source Code

```python
x = 5.5
y = 2.5
print(x * y)
```

### ⚙️ Internal Working

| Step | Description |
|------|-------------|
| **Compiler** | Recognizes float literals |
| **Bytecode** | `LOAD_CONST 5.5`, `LOAD_CONST 2.5`, `BINARY_MULTIPLY` |
| **PVM** | Uses floating-point arithmetic (C-level operations) |

### ✅ Output

```
13.75
```

📌 Float operations are slower than int due to precision handling.

---

## 📝 2.3 String (`str`) Data Type

### 🧾 Source Code

```python
name = "DevOps"
print("Hello " + name)
```

### ⚙️ Internal Working

| Step | Description |
|------|-------------|
| **Compiler** | Treats strings as immutable objects |
| **Bytecode** | `LOAD_CONST "Hello "`, `LOAD_NAME name`, `BINARY_ADD` |
| **PVM** | Creates a **new string object**, old strings remain unchanged |

### ✅ Output

```
Hello DevOps
```

📌 Strings are **immutable**, so concatenation creates new objects.

---

## 📋 2.4 List (`list`) Data Type

### 🧾 Source Code

```python
nums = [1, 2, 3]
nums.append(4)
print(nums)
```

### ⚙️ Internal Working

| Step | Description |
|------|-------------|
| **Compiler** | Creates list object |
| **Bytecode** | `BUILD_LIST`, `LOAD_METHOD append`, `CALL_METHOD` |
| **PVM** | List stored in heap, `append()` modifies the same object |

### ✅ Output

```
[1, 2, 3, 4]
```

📌 Lists are **mutable**, so memory address stays same.

---

## 📦 2.5 Tuple (`tuple`) Data Type

### 🧾 Source Code

```python
t = (10, 20)
print(t)
```

### ⚙️ Internal Working

| Step | Description |
|------|-------------|
| **Compiler** | Creates fixed-size structure |
| **Bytecode** | `LOAD_CONST (10, 20)` |
| **PVM** | Stores tuple in heap, no modification allowed |

### ✅ Output

```
(10, 20)
```

📌 Tuples are **immutable & faster** than lists.

---

## 📖 2.6 Dictionary (`dict`) Data Type

### 🧾 Source Code

```python
user = {"name": "Khushal", "role": "DevOps"}
print(user["role"])
```

### ⚙️ Internal Working

| Step | Description |
|------|-------------|
| **Compiler** | Builds hash table |
| **Bytecode** | `BUILD_MAP`, `LOAD_CONST "role"`, `BINARY_SUBSCR` |
| **PVM** | Uses hash of key `"role"`, retrieves value in O(1) |

### ✅ Output

```
DevOps
```

📌 Dict uses **hashing internally** for fast lookup.

---

## ✅ 2.7 Boolean (`bool`) Data Type

### 🧾 Source Code

```python
is_active = True
print(is_active)
```

### ⚙️ Internal Working

| Step | Description |
|------|-------------|
| **Compiler** | Converts `True` → constant |
| **Bytecode** | `LOAD_CONST True` |
| **PVM** | Uses singleton objects (`True`, `False`) |

### ✅ Output

```
True
```

📌 `True` and `False` are **single instances** in Python.

---

## 🔀 2.8 Mixed Data Types (Real-World Example)

### 🧾 Source Code

```python
user = {
    "name": "Admin",
    "age": 22,
    "skills": ["AWS", "Docker"]
}
print(user["skills"][0])
```

### ⚙️ Internal Working

- Dict → list → string access
- Multiple heap objects
- PVM resolves references step-by-step

### ✅ Output

```
AWS
```

---

---

# 🔢 PART 3: Numbers in Python

---

## 📊 3.1 Overview of Numeric Types

Python has **three core built-in numeric types**:

| Type | Description | Example |
|------|-------------|---------|
| `int` | Integers (whole numbers) | `10`, `-25`, `0` |
| `float` | Floating-point numbers | `3.14`, `0.1` |
| `complex` | Complex numbers | `3 + 4j` |

📌 `bool` is technically a subtype of `int`.

---

## 🔢 3.2 `int` — Integers

![Image](https://jakevdp.github.io/PythonDataScienceHandbook/figures/cint_vs_pyint.png)

![Image](https://gsp.humboldt.edu/olm/Courses/GSP_318/Images/Convertions.png)

### ✅ What it is

Whole numbers (positive, negative, zero) with **no size limit**.

```python
a = 10
b = -25
c = 999999999999999999
```

### 🧠 Internal Working

- Python `int` is **arbitrary precision**
- Stored as an **object in heap**
- Uses multiple machine words if needed

```python
x = 10
y = x
```

- `x` and `y` reference the **same int object**
- Integers are **immutable**

### 🔥 Example

```python
x = 10
x = x + 1   # new object created
```

---

## 🔢 3.3 `float` — Floating Point Numbers

![Image](https://media.geeksforgeeks.org/wp-content/uploads/Single-Precision-IEEE-754-Floating-Point-Standard.jpg)

![Image](https://i.sstatic.net/GfXXx.png)

### ✅ What it is

Decimal numbers stored using **IEEE-754 double precision (64-bit)**.

```python
pi = 3.14
rate = 0.1
```

### 🧠 Internal Working

- Stored in **binary form**
- Not all decimals can be represented exactly

```python
print(0.1 + 0.2)
```

**Output:**

```
0.30000000000000004
```

⚠️ This is **not a Python bug**, it's floating-point math.

### 🔥 Use `decimal` for accuracy

```python
from decimal import Decimal
print(Decimal("0.1") + Decimal("0.2"))
```

---

## 🔢 3.4 `complex` — Complex Numbers

![Image](https://www.askpython.com/wp-content/uploads/2020/03/python_complex.png)

![Image](https://ds055uzetaobb.cloudfront.net/brioche/uploads/1cBmAHyVZM-diagram.png?width=300)

### ✅ What it is

Numbers with **real + imaginary** parts.

```python
z = 3 + 4j
```

### 🧠 Internal Working

- Stored as **two floats**: `z.real` and `z.imag`
- Used in: Signal processing, Scientific computing

```python
print(z.real, z.imag)   # 3.0 4.0
```

### 🔥 Operations on Complex Numbers

```python
z1 = 2 + 3j
z2 = 1 - 1j

print(z1 + z2)   # (3+2j)
print(z1 * z2)   # (5+1j)
print(abs(z1))   # sqrt(2² + 3²) = 3.605...
```

---

## ✅ 3.5 `bool` — Boolean Numbers

![Image](https://i.vimeocdn.com/video/1075344651-ad1f68755eba55ba2d63a49346b1155530df575c2ce3a842d885e4beee620314-d?f=webp)

![Image](https://bobbyhadz.com/images/blog/python-convert-true-false-to-1-0/convert-true-and-false-to-1-and-0.webp)

```python
True == 1      # True
False == 0     # True
```

### 🧠 Internal Working

- `bool` is a **subclass of int**
- `True → 1`, `False → 0`

```python
print(True + True)   # 2
```

---

## 🔄 3.6 Type Conversion (Casting)

```python
int(3.7)       # 3
float(10)      # 10.0
complex(2, 3)  # (2+3j)
```

⚠️ Conversion creates **new objects**.

---

## ➗ 3.7 Numeric Operators

| Operator | Meaning        | Example | Result |
|----------|----------------|---------|--------|
| `+`      | Addition       | `5 + 3` | `8` |
| `-`      | Subtraction    | `5 - 3` | `2` |
| `*`      | Multiplication | `5 * 3` | `15` |
| `/`      | True division  | `5 / 2` | `2.5` |
| `//`     | Floor division | `5 // 2` | `2` |
| `%`      | Modulus        | `5 % 2` | `1` |
| `**`     | Power          | `2 ** 3` | `8` |

---

## 💾 3.8 Memory Behavior (Important for Interviews)

```python
a = 256
b = 256
print(a is b)   # True
```

```python
a = 500
b = 500
print(a is b)   # False
```

📌 Python **caches small integers** (-5 to 256).

---

## 🔧 3.9 Numeric Functions

```python
abs(-10)          # 10
pow(2, 3)         # 8
round(3.1415, 2)  # 3.14
```

---

---

# 🔍 PART 4: `repr()` vs `str()` vs `print()`

---

## 📊 4.1 Overview

They are related, but they **serve different purposes**.

| Function | Purpose | Audience |
|----------|---------|----------|
| `str()` | Readable output | User |
| `repr()` | Exact/Debug representation | Developer |
| `print()` | Display to console | Output |

---

## 📝 4.2 `str()` — User-friendly String

### 👉 Purpose

- Meant for **humans**
- Easy to read
- Used when displaying output to users

### Example

```python
x = "Hello\nWorld"
print(str(x))
```

### Output

```
Hello
World
```

✅ Newline is **interpreted**

---

## 🔧 4.3 `repr()` — Developer-friendly (Official Representation)

### 👉 Purpose

- Meant for **developers**
- Unambiguous
- Should ideally recreate the object

### Example

```python
x = "Hello\nWorld"
print(repr(x))
```

### Output

```
'Hello\nWorld'
```

✅ Escape characters are **visible**
✅ Shows quotes

---

## 🖨️ 4.4 `print()` — Output Function

### 👉 Purpose

- Displays text to the console
- Internally calls `str()` on the object

### Example

```python
x = 10
print(x)
```

Internally equivalent to:

```python
print(str(x))
```

---

## 🔁 4.5 Key Relationship

```
print(obj) → str(obj)
repr(obj) → developer view
```

---

## 🔥 4.6 Side-by-Side Comparison

```python
x = "Python\nDevOps"

print(x)
print(str(x))
print(repr(x))
```

### Output

```
Python
DevOps
Python
DevOps
'Python\nDevOps'
```

---

## 📋 4.7 Another Example (List)

```python
data = [1, 2, 3]
print(data)
str(data)
repr(data)
```

All output:

```
[1, 2, 3]
```

👉 For simple objects, `str()` and `repr()` may look the same.

---

## 🧠 4.8 Custom Class Example (VERY IMPORTANT)

```python
class User:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"User: {self.name}"

    def __repr__(self):
        return f"User(name='{self.name}')"

u = User("Khushal")

print(u)        # User: Khushal
str(u)          # User: Khushal
repr(u)         # User(name='Khushal')
```

🔥 This shows the **real difference** clearly.

---

## 🧪 4.9 When Each Is Used Internally

| Situation         | Function Used |
|-------------------|---------------|
| `print(obj)`      | `str(obj)` |
| Console / logs    | `repr(obj)` |
| Debugging         | `repr(obj)` |
| `>>> obj` in REPL | `repr(obj)` |

---

---

# 🔍 PART 5: Comparisons in Python

---

## 📊 5.1 Overview

Comparisons are used to **compare values or objects** and always return a **boolean**:

```python
True or False
```

---

## ⚖️ 5.2 Comparison Operators

| Operator | Meaning          | Example  | Result |
|----------|------------------|----------|--------|
| `==`     | Equal to         | `5 == 5` | `True` |
| `!=`     | Not equal        | `5 != 3` | `True` |
| `>`      | Greater than     | `7 > 4`  | `True` |
| `<`      | Less than        | `3 < 9`  | `True` |
| `>=`     | Greater or equal | `5 >= 5` | `True` |
| `<=`     | Less or equal    | `4 <= 6` | `True` |

---

## 🔢 5.3 Comparing Numbers

```python
a = 10
b = 20

print(a < b)     # True
print(a == b)    # False
print(a != b)    # True
```

📌 Python compares **numeric values**, not memory addresses.

---

## 📝 5.4 Comparing Strings (Lexicographical)

Python compares strings **character by character** using ASCII/Unicode values.

```python
print("apple" < "banana")   # True
print("Zoo" < "apple")      # True (capital letters first)
```

⚠️ Capital letters come **before** lowercase letters.

---

## 🔀 5.5 Comparing Different Data Types

```python
print(10 == "10")   # False
print(10 == 10.0)   # True
```

**Rules:**

- Same value but **different types** → usually `False`
- `int` and `float` can be equal if value matches

```python
10 == True   # False
1 == True    # True
```

---

## ⛓️ 5.6 Chained Comparisons (Very Pythonic 🔥)

Python allows **multiple comparisons in one line**.

```python
x = 10
print(5 < x < 20)   # True
```

Equivalent to:

```python
5 < x and x < 20
```

---

## 🆔 5.7 `==` vs `is` (VERY IMPORTANT)

### 🔹 `==` → Value comparison

### 🔹 `is` → Identity (memory) comparison

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)   # True
print(a is b)   # False
```

```python
x = 10
y = 10

print(x is y)   # True (small integer caching)
```

📌 Use `is` for:

```python
if value is None:
```

---

## 📋 5.8 Comparing Lists, Tuples, Sets

### 🔹 Lists & Tuples (element-wise)

```python
print([1, 2] < [1, 3])    # True
print((1, 2) == (1, 2))   # True
```

### 🔹 Sets (only equality)

```python
print({1, 2} == {2, 1})     # True
print({1, 2} < {1, 2, 3})   # True (subset)
```

---

## 📖 5.9 Comparing Dictionaries

```python
a = {"x": 1, "y": 2}
b = {"y": 2, "x": 1}

print(a == b)   # True
```

📌 Order does **not** matter
📌 Only equality comparison is allowed

---

## ⚠️ 5.10 Special Case: `NaN` (Tricky)

```python
x = float("nan")

print(x == x)   # False
print(x != x)   # True
```

📌 `NaN` is **never equal to anything**, even itself.

---

## 🧠 5.11 Custom Object Comparison

```python
class User:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

u1 = User(25)
u2 = User(25)

print(u1 == u2)  # True
```

Without `__eq__`, comparison is based on **identity**.

---

## ✅ 5.12 Truthy & Falsy in Comparisons

**Falsy values:**

```python
False, 0, 0.0, "", [], {}, None
```

```python
if [] == False:
    print("Equal")     # ❌ Won't print
```

But:

```python
if not []:
    print("Falsy")     # ✅ Will print
```

---

---

# 🧮 PART 6: Python Math Library

---

## 📊 6.1 Overview

The **`math` library** provides **fast, optimized mathematical functions** written in **C**, mainly for **real-number (float) operations**.

```python
import math
```

📌 Works with **int & float**
📌 Does **NOT** support complex numbers (use `cmath` for that)

---

## 🔢 6.2 Common Constants

```python
import math

math.pi     # 3.141592653589793
math.e      # 2.718281828459045
math.inf    # Infinity
math.nan    # Not a Number
```

---

## 🔄 6.3 Rounding & Absolute Functions

```python
math.ceil(4.2)     # 5  (round up)
math.floor(4.9)    # 4  (round down)
math.trunc(4.9)    # 4  (remove decimal)
math.fabs(-10.5)   # 10.5 (absolute value)
```

🔹 `fabs()` always returns **float**
🔹 `abs()` is a **built-in**, works for all numeric types

---

## 📈 6.4 Power & Logarithmic Functions

```python
math.pow(2, 3)     # 8.0
math.sqrt(16)      # 4.0
math.log(10)       # Natural log (base e)
math.log10(100)    # 2.0
math.log2(8)       # 3.0
```

📌 `math.pow()` → always float
📌 `**` operator may return int or float

---

## 📐 6.5 Trigonometric Functions (Radians ⚠️)

```python
math.sin(math.pi / 2)   # 1.0
math.cos(0)             # 1.0
math.tan(math.pi / 4)   # 1.0
```

### Degree ↔ Radian Conversion

```python
math.degrees(math.pi)     # 180.0
math.radians(180)         # 3.14159
```

---

## 🔢 6.6 Factorial & Combinations

```python
math.factorial(5)   # 120
```

**Python 3.8+:**

```python
math.comb(5, 2)     # 10 (combinations)
math.perm(5, 2)     # 20 (permutations)
```

📌 Only accepts **non-negative integers**

---

## 🔗 6.7 GCD & LCM (Very Useful 🔥)

```python
math.gcd(20, 8)   # 4
math.lcm(4, 6)    # 12
```

📌 Common in **DSA & number theory**

---

## 🔍 6.8 Floating-Point Utilities

```python
math.isfinite(10)       # True
math.isinf(math.inf)    # True
math.isnan(math.nan)    # True
```

**Comparison helper:**

```python
math.isclose(0.1 + 0.2, 0.3)  # True
```

🔥 Best way to compare floats safely

---

## 🧪 6.9 Special Functions

```python
math.exp(1)        # e¹
math.gamma(5)      # 24.0
math.erf(1)        # Error function
```

**Used in:**

- Statistics
- ML
- Scientific computing

---

## ⚖️ 6.10 `math` vs Built-in Functions

| Task        | Built-in  | math                |
|-------------|-----------|---------------------|
| Absolute    | `abs()`   | `math.fabs()`       |
| Power       | `**`      | `math.pow()`        |
| Square root | `**0.5`   | `math.sqrt()`       |
| Rounding    | `round()` | `ceil()`, `floor()` |

📌 Built-ins are more **general**
📌 `math` is more **precise & faster**

---

## 🔀 6.11 `math` vs `cmath`

| Feature          | math   | cmath   |
|------------------|--------|---------|
| Supports complex | ❌ No  | ✅ Yes  |
| Speed            | Faster | Slower  |
| Return type      | float  | complex |

```python
import cmath
cmath.sqrt(-1)   # 1j
```

---

---

# 📋 PART 7: Quick Reference Summary

---

## 🔢 Numeric Types Summary

| Type      | Example       | Mutable | Notes                    |
|-----------|---------------|---------|--------------------------|
| `int`     | `10`, `-5`    | ❌      | Arbitrary precision      |
| `float`   | `3.14`        | ❌      | IEEE-754 double          |
| `complex` | `3+4j`        | ❌      | Real + Imaginary         |
| `bool`    | `True/False`  | ❌      | Subclass of int          |

---

## 🔍 Comparison Operators Summary

| Operator | Meaning          |
|----------|------------------|
| `==`     | Equal (value)    |
| `!=`     | Not equal        |
| `is`     | Same object      |
| `is not` | Different object |
| `<`      | Less than        |
| `<=`     | Less or equal    |
| `>`      | Greater than     |
| `>=`     | Greater or equal |

---

## 📝 `str()` vs `repr()` Summary

| Function  | Purpose       | Shows Quotes | Escapes Visible |
|-----------|---------------|--------------|-----------------|
| `str()`   | User-friendly | ❌           | ❌              |
| `repr()`  | Developer     | ✅           | ✅              |
| `print()` | Uses `str()`  | ❌           | ❌              |

---

## 🧮 Math Functions Cheat Sheet

```python
import math

# Rounding
math.ceil(4.2)      # 5
math.floor(4.9)     # 4

# Power & Roots
math.sqrt(16)       # 4.0
math.pow(2, 3)      # 8.0

# Logarithms
math.log(10)        # natural log
math.log10(100)     # 2.0

# Trigonometry
math.sin(math.pi/2) # 1.0

# Constants
math.pi             # 3.14159...
math.e              # 2.71828...

# Comparisons
math.isclose(a, b)  # safe float compare
```

---

## 🎯 Interview Tips

1. **Integer Caching**: Python caches integers from -5 to 256
2. **Float Precision**: Use `decimal.Decimal` for exact decimal math
3. **`is` vs `==`**: `is` checks identity, `==` checks value
4. **NaN Behavior**: `float("nan") != float("nan")`
5. **Memory**: All objects stored in heap, references on stack
6. **Immutability**: `int`, `float`, `str`, `tuple` are immutable
7. **`repr()` in REPL**: Interactive Python uses `repr()` for display

---

## 📚 Further Reading

- [Python Official Documentation](https://docs.python.org/3/)
- [Python Memory Management](https://realpython.com/python-memory-management/)
- [IEEE 754 Floating Point](https://en.wikipedia.org/wiki/IEEE_754)

---

> 📅 **Last Updated**: January 2026
> 
> 👤 **Author**: Khushal Bhavsar
