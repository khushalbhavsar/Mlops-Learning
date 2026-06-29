# What is Notebook
A **Notebook** is an interactive environment where you can write **code, text, equations, visualizations, and outputs** all in one document. It is widely used by data scientists, machine learning engineers, and researchers for experimentation and analysis.

The most common notebook is **Jupyter Notebook**.

## Why use a Notebook?

A notebook lets you:

* Write and execute Python code one section (cell) at a time.
* View the output immediately below the code.
* Add explanations using Markdown.
* Display graphs, tables, and images.
* Save your entire analysis in a single file.

## Example

A notebook contains cells.

**Cell 1 (Code):**

```python
x = 10
y = 20
print(x + y)
```

**Output:**

```
30
```

**Cell 2 (Markdown):**

```markdown
# Addition Example
This notebook demonstrates basic addition.
```

## Features

* **Code Cells** – Write and run Python code.
* **Markdown Cells** – Write notes, headings, and documentation.
* **Output Cells** – Show results, charts, and error messages.
* **Interactive Execution** – Run only the cells you want.

## Why is it popular in Machine Learning?

Notebooks make it easy to:

* Load datasets.
* Clean and preprocess data.
* Train machine learning models.
* Visualize results with graphs.
* Test ideas quickly without running an entire program.

## Common Notebook Platforms

* Jupyter Notebook – Runs on your local computer.
* JupyterLab – A more advanced version of Jupyter Notebook.
* Google Colaboratory (Google Colab) – Runs in the cloud for free and provides access to GPUs.
* Visual Studio Code – Supports opening and running Jupyter notebooks directly.
* Anaconda Navigator – Lets you launch Jupyter Notebook and JupyterLab easily.

## Notebook vs Python Script

| Notebook                           | Python Script (`.py`)                               |
| ---------------------------------- | --------------------------------------------------- |
| Interactive                        | Runs from start to finish                           |
| Execute one cell at a time         | Execute the whole file                              |
| Best for learning and experiments  | Best for production applications                    |
| Displays charts and outputs inline | Output appears in the terminal or a separate window |

### For your MLOps journey

Since you're learning MLOps, you'll use notebooks extensively for:

* Data exploration (EDA)
* Learning NumPy and Pandas
* Building machine learning models with scikit-learn
* Testing ML code before converting it into production-ready Python scripts

A common workflow is:
**Notebook (`.ipynb`) → Python script (`.py`) → Git → CI/CD → Docker → Kubernetes → Deployment.**

# What is jupyter Notebook?
## What is Jupyter Notebook?

**Jupyter Notebook** is a free, open-source web application that allows you to write, run, and document code in an interactive notebook. It is one of the most widely used tools for **Python, Data Science, Machine Learning, and MLOps**.

Instead of writing an entire Python program and running it all at once, you can execute your code **one cell at a time** and immediately see the output.

---

## Why is it called "Jupyter"?

The name **Jupyter** comes from the three programming languages it originally supported:

* **Ju** → Julia
* **Pyt** → Python
* **R** → R

Today, it supports many more programming languages through kernels.

---

## Features of Jupyter Notebook

* ✅ Write Python code interactively
* ✅ Run code one cell at a time
* ✅ View outputs immediately
* ✅ Create graphs and charts
* ✅ Display tables and images
* ✅ Write explanations using Markdown
* ✅ Save work in a single `.ipynb` notebook file

---

## Structure of a Notebook

A notebook is made up of **cells**.

### 1. Code Cell

```python
a = 10
b = 20

print(a + b)
```

**Output**

```
30
```

---

### 2. Markdown Cell

```markdown
# NumPy Tutorial

This notebook explains NumPy arrays.
```

This is used to add:

* Headings
* Notes
* Documentation
* Images
* Tables
* Mathematical equations

---

## Why do Data Scientists use Jupyter?

Suppose you are building an ML model.

Instead of writing everything in one Python file, you can work step by step:

```
Import libraries
        ↓
Load dataset
        ↓
Clean data
        ↓
Visualize data
        ↓
Train model
        ↓
Evaluate results
```

You can run each step separately, making debugging and experimentation much easier.

---

## Common Shortcut Keys

| Shortcut          | Action                                |
| ----------------- | ------------------------------------- |
| **Shift + Enter** | Run current cell and move to the next |
| **Ctrl + Enter**  | Run current cell and stay there       |
| **A**             | Insert a cell above (Command mode)    |
| **B**             | Insert a cell below (Command mode)    |
| **DD**            | Delete current cell (Command mode)    |
| **M**             | Convert cell to Markdown              |
| **Y**             | Convert cell to Code                  |

---

## Installing Jupyter Notebook

First install Jupyter:

```bash
pip install notebook
```

Then start it:

```bash
jupyter notebook
```

This opens Jupyter Notebook in your web browser.

---

## Jupyter Notebook vs Python Script

| Jupyter Notebook                          | Python Script (`.py`)              |
| ----------------------------------------- | ---------------------------------- |
| Interactive                               | Runs from start to finish          |
| Execute code one cell at a time           | Execute the entire file            |
| Shows output directly below the code      | Output appears in the terminal     |
| Great for learning, data analysis, and ML | Better for production applications |

---

## Why you'll use it in MLOps

Since you're learning MLOps, Jupyter Notebook is especially useful for:

* Learning **NumPy**, **Pandas**, and **Matplotlib**
* Performing Exploratory Data Analysis (EDA)
* Training and testing machine learning models
* Experimenting with code before turning it into production-ready Python scripts

A typical workflow is:

```
Jupyter Notebook (.ipynb)
          ↓
Experiment & Build ML Model
          ↓
Convert to Python Script (.py)
          ↓
Git → CI/CD → Docker → Kubernetes → Deploy
```

For beginners in Python, Machine Learning, and MLOps, Jupyter Notebook is one of the best environments because it provides instant feedback and makes it easy to learn by experimenting.

# What is Numpy?
**NumPy** (short for **Numerical Python**) is a popular open-source Python library used for **fast numerical computing**. It provides a powerful **N-dimensional array (`ndarray`)** and a large collection of functions for performing mathematical operations efficiently. It is a foundational library for data science, machine learning, and scientific computing in Python. ([NumPy][1])

Some of the main features of NumPy include:

* Fast, memory-efficient arrays
* Mathematical operations on entire arrays (vectorization)
* Linear algebra functions
* Statistical functions
* Random number generation
* Fourier transforms

Here's a simple example:

```python
import numpy as np

# Create an array
arr = np.array([1, 2, 3, 4, 5])

# Multiply every element by 2
print(arr * 2)
```

**Output:**

```python
[ 2  4  6  8 10]
```

Without NumPy, you would typically need to loop through each element manually.

### Why use NumPy instead of Python lists?

* **Faster:** Operations on arrays are implemented in optimized C code.
* **Less memory usage:** Arrays store data more efficiently.
* **Powerful:** Supports multidimensional arrays and advanced mathematical operations.

### Common applications

* Data analysis
* Machine learning
* Scientific simulations
* Image processing
* Signal processing
* Artificial intelligence

To install NumPy, run:

```bash
pip install numpy
```

For more information and tutorials, see the official [NumPy website](https://numpy.org/?utm_source=chatgpt.com) and [NumPy documentation](https://numpy.org/doc/?utm_source=chatgpt.com).

[1]: https://numpy.org/?utm_source=chatgpt.com "NumPy"

# Numpy Arrays
NumPy arrays are the core data structure of the NumPy library. They are **homogeneous**, meaning all elements in the array must be of the same data type. NumPy arrays are more efficient than Python lists for numerical computations.

# Difference between Python List and Numpy Array
| Feature                  | Python List                     | NumPy Array                       |
| ------------------------ | ------------------------------- | --------------------------------- |
| Homogeneous              | No                              | Yes                               |
| Memory Efficiency        | Less efficient                  | More efficient                    |
| Performance              | Slower for large datasets       | Faster for large datasets         |
| Mathematical Operations  | Requires loops                  | Supports vectorized operations    |

# Creating NumPy Arrays
You can create NumPy arrays using the `numpy.array()` function. Here are some examples:

```python
import numpy as np
# Create a 1D array
arr1d = np.array([1, 2, 3, 4, 5])
print(f"1D Array: {arr1d}")

# Create a 2D array
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(f"2D Array:\n{arr2d}")

# Create a 3D array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(f"3D Array:\n{arr3d}")
```     

# Vectorization in NumPy
Vectorization is a key feature of NumPy that allows you to perform operations on entire arrays without the need for explicit loops. This leads to more concise code and improved performance.
example:

```python

import numpy as np
# Create two arrays
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
# Add the two arrays
result = arr1 + arr2
print(result)
```

**Output:**

```
[ 7  9 11 13 15]
```

# Matrix Operations in NumPy
NumPy provides a variety of functions for performing matrix operations. Here are some common operations:

```python
import numpy as np
# Create two 2D arrays (matrices)
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])

# Matrix Addition
result_add = matrix1 + matrix2
print("Matrix Addition:")
print(result_add)
# Matrix Multiplication
result_mul = np.dot(matrix1, matrix2)
print("Matrix Multiplication:")
print(result_mul)
# Transpose
result_transpose = np.transpose(matrix1)
print("Transpose of Matrix 1:")
print(result_transpose)
```

## Most Important NumPy Functions 

| No. | Function              | Purpose                                     | Example                     |
| --- | --------------------- | ------------------------------------------- | --------------------------- |
| 1   | `np.array()`          | Create a NumPy array                        | `np.array([1,2,3])`         |
| 2   | `np.zeros()`          | Create an array filled with zeros           | `np.zeros((2,3))`           |
| 3   | `np.ones()`           | Create an array filled with ones            | `np.ones((2,2))`            |
| 4   | `np.arange()`         | Create a sequence with a step size          | `np.arange(1,10,2)`         |
| 5   | `np.linspace()`       | Create evenly spaced values                 | `np.linspace(0,1,5)`        |
| 6   | `reshape()`           | Change the shape of an array                | `arr.reshape(2,3)`          |
| 7   | `flatten()`           | Convert a multi-dimensional array to 1D     | `arr.flatten()`             |
| 8   | `np.sum()`            | Find the sum of elements                    | `np.sum(arr)`               |
| 9   | `np.mean()`           | Find the average                            | `np.mean(arr)`              |
| 10  | `np.max()`            | Find the maximum value                      | `np.max(arr)`               |
| 11  | `np.min()`            | Find the minimum value                      | `np.min(arr)`               |
| 12  | `np.argmax()`         | Find the index of the maximum value         | `np.argmax(arr)`            |
| 13  | `np.argmin()`         | Find the index of the minimum value         | `np.argmin(arr)`            |
| 14  | `np.sort()`           | Sort the array                              | `np.sort(arr)`              |
| 15  | `np.where()`          | Find elements based on a condition          | `np.where(arr > 5)`         |
| 16  | `np.unique()`         | Return unique values                        | `np.unique(arr)`            |
| 17  | `np.concatenate()`    | Join two or more arrays                     | `np.concatenate((a,b))`     |
| 18  | `np.random.randint()` | Generate random integers                    | `np.random.randint(1,10,5)` |
| 19  | `np.dot()`            | Perform dot product / matrix multiplication | `np.dot(a,b)`               |
| 20  | `np.linalg.inv()`     | Find the inverse of a matrix                | `np.linalg.inv(A)`          |

---

## Most Important Array Attributes

| Attribute  | Purpose                                  | Example        |
| ---------- | ---------------------------------------- | -------------- |
| `shape`    | Returns the dimensions of the array      | `arr.shape`    |
| `ndim`     | Returns the number of dimensions         | `arr.ndim`     |
| `size`     | Returns the total number of elements     | `arr.size`     |
| `dtype`    | Returns the data type of the elements    | `arr.dtype`    |
| `itemsize` | Returns the size of each element (bytes) | `arr.itemsize` |

---

## Frequently Used Random Functions

| Function              | Purpose                                       |
| --------------------- | --------------------------------------------- |
| `np.random.rand()`    | Random decimal numbers (uniform distribution) |
| `np.random.randn()`   | Random numbers from a normal distribution     |
| `np.random.randint()` | Random integers                               |
| `np.random.choice()`  | Randomly select elements                      |
| `np.random.shuffle()` | Shuffle an array in place                     |
| `np.random.seed()`    | Set a seed for reproducible random numbers    |

---

# NumPy Array Attributes and Methods

In NumPy, an **attribute** gives you **information about an array**, while a **method** performs **an operation on the array**.

* **Attributes** → Describe the array (shape, size, data type, etc.).
* **Methods** → Perform actions (reshape, flatten, sort, sum, etc.).

---

# NumPy Array Attributes

| Attribute  | Purpose                                    | Example        | Output           |
| ---------- | ------------------------------------------ | -------------- | ---------------- |
| `shape`    | Returns the dimensions of the array        | `arr.shape`    | `(2, 3)`         |
| `ndim`     | Returns the number of dimensions           | `arr.ndim`     | `2`              |
| `size`     | Returns the total number of elements       | `arr.size`     | `6`              |
| `dtype`    | Returns the data type                      | `arr.dtype`    | `int64`          |
| `itemsize` | Returns the size (in bytes) of one element | `arr.itemsize` | `8`              |
| `nbytes`   | Returns the total memory used by the array | `arr.nbytes`   | `48`             |
| `T`        | Returns the transpose of the array         | `arr.T`        | Transposed array |

### Example

```python
import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])

print(arr.shape)      # (2, 3)
print(arr.ndim)       # 2
print(arr.size)       # 6
print(arr.dtype)      # int64 (or int32)
print(arr.itemsize)   # 8 (or 4)
print(arr.nbytes)     # 48 (or 24)
```

---

# NumPy Array Methods

| Method        | Purpose                       | Example            |
| ------------- | ----------------------------- | ------------------ |
| `reshape()`   | Change the shape of the array | `arr.reshape(3,2)` |
| `flatten()`   | Convert to a 1D array         | `arr.flatten()`    |
| `ravel()`     | Flatten without copying       | `arr.ravel()`      |
| `transpose()` | Transpose the array           | `arr.transpose()`  |
| `copy()`      | Create a copy of the array    | `arr.copy()`       |
| `sort()`      | Sort the array                | `arr.sort()`       |
| `sum()`       | Sum of all elements           | `arr.sum()`        |
| `mean()`      | Average of elements           | `arr.mean()`       |
| `max()`       | Maximum value                 | `arr.max()`        |
| `min()`       | Minimum value                 | `arr.min()`        |
| `argmax()`    | Index of the maximum value    | `arr.argmax()`     |
| `argmin()`    | Index of the minimum value    | `arr.argmin()`     |

### Example

```python
import numpy as np

arr = np.array([10,20,30,40])

print(arr.sum())      # 100
print(arr.mean())     # 25.0
print(arr.max())      # 40
print(arr.min())      # 10
print(arr.argmax())   # 3
print(arr.argmin())   # 0
```

---

# Attribute vs Method

| Feature          | Attribute                         | Method                             |
| ---------------- | --------------------------------- | ---------------------------------- |
| What it does     | Gives information about the array | Performs an operation on the array |
| Parentheses `()` | ❌ No                              | ✅ Yes                              |
| Example          | `arr.shape`                       | `arr.reshape(2,2)`                 |

### Example

```python
import numpy as np

arr = np.array([[1,2],
                [3,4]])

print(arr.shape)      # Attribute
print(arr.sum())      # Method
```

---

# NumPy Reshaping & Resizing 

| Function      | Purpose                                                                | Example             | Output              |
| ------------- | ---------------------------------------------------------------------- | ------------------- | ------------------- |
| `reshape()`   | Changes the **shape** of the array (number of elements stays the same) | `arr.reshape(2,3)`  | `[[1 2 3],[4 5 6]]` |
| `resize()`    | Changes the **shape and size** of the array (can add/remove elements)  | `arr.resize((2,3))` | `[[1 2 3],[4 0 0]]` |
| `flatten()`   | Converts the array into a **1D copy**                                  | `arr.flatten()`     | `[1 2 3 4 5 6]`     |
| `ravel()`     | Converts the array into a **1D view** (if possible)                    | `arr.ravel()`       | `[1 2 3 4 5 6]`     |
| `transpose()` | Swaps rows and columns                                                 | `arr.transpose()`   | Transposed array    |
| `T`           | Shortcut for transpose                                                 | `arr.T`             | Transposed array    |

---

## Difference Between `reshape()` and `resize()`

| Feature                    | `reshape()` | `resize()` |
| -------------------------- | ----------- | ---------- |
| Changes shape              | ✅           | ✅          |
| Changes number of elements | ❌           | ✅          |
| Modifies original array    | ❌           | ✅          |
| Adds/removes elements      | ❌           | ✅          |

---

## Must-Remember Rules

* ✅ `reshape()` **cannot change** the total number of elements.
* ✅ `resize()` **can add or remove** elements.
* ✅ `flatten()` returns a **copy**.
* ✅ `ravel()` returns a **view** (whenever possible).
* ✅ `transpose()` (or `T`) swaps rows and columns.

---

# NumPy Array Indexing & Slicing

**Array Indexing** and **Array Slicing** are used to access elements from a NumPy array.

* **Indexing** → Access **a single element**.
* **Slicing** → Access **multiple elements**.

---

# 1. Array Indexing

**Definition:**
Indexing is used to access a **single element** from an array using its index (position).

## 1D Array Indexing

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])    # First element
print(arr[2])    # Third element
print(arr[-1])   # Last element
```

**Output**

```python
10
30
50
```

### Explanation

| Syntax    | Meaning                             | Output |
| --------- | ----------------------------------- | ------ |
| `arr[0]`  | First element (index starts from 0) | `10`   |
| `arr[2]`  | Third element                       | `30`   |
| `arr[-1]` | Last element                        | `50`   |

> **Note:** NumPy uses **zero-based indexing**, so the first element is always at index `0`.

---

## 2D Array Indexing

```python
arr = np.array([
    [1,2,3],
    [4,5,6]
])

print(arr[0,1])
print(arr[1,2])
```

**Output**

```python
2
6
```

### Explanation

| Syntax     | Meaning         | Output |
| ---------- | --------------- | ------ |
| `arr[0,1]` | Row 0, Column 1 | `2`    |
| `arr[1,2]` | Row 1, Column 2 | `6`    |

**Remember:**

```text
arr[row, column]
```

For example,

```text
[[1 2 3]
 [4 5 6]]
```

* `arr[0,0]` → `1`
* `arr[0,2]` → `3`
* `arr[1,1]` → `5`

---

# 2. Array Slicing

**Definition:**
Slicing is used to access **multiple elements** from an array.

### Syntax

```python
arr[start : stop : step]
```

* **start** → Starting index (included)
* **stop** → Ending index (excluded)
* **step** → Number of positions to skip

---

## 1D Array Slicing

```python
arr = np.array([10,20,30,40,50])
```

### Example 1

```python
print(arr[1:4])
```

**Output**

```python
[20 30 40]
```

### Explanation

Starts from index **1** and stops **before** index **4**.

| Index | Value |
| ----- | ----- |
| 1     | 20    |
| 2     | 30    |
| 3     | 40    |

---

### Example 2

```python
print(arr[:3])
```

**Output**

```python
[10 20 30]
```

### Explanation

Starts from the beginning and stops before index `3`.

---

### Example 3

```python
print(arr[2:])
```

**Output**

```python
[30 40 50]
```

### Explanation

Starts from index `2` and continues until the end.

---

### Example 4

```python
print(arr[::2])
```

**Output**

```python
[10 30 50]
```

### Explanation

Selects every **2nd** element.

---

### Example 5

```python
print(arr[::-1])
```

**Output**

```python
[50 40 30 20 10]
```

### Explanation

A step of `-1` reverses the array.

---

# 2D Array Slicing

```python
arr = np.array([
    [1,2,3],
    [4,5,6]
])
```

### First Row

```python
print(arr[0,:])
```

**Output**

```python
[1 2 3]
```

**Explanation:** Row `0`, all columns (`:` means all).

---

### Second Row

```python
print(arr[1,:])
```

**Output**

```python
[4 5 6]
```

---

### First Column

```python
print(arr[:,0])
```

**Output**

```python
[1 4]
```

**Explanation:** All rows, column `0`.

---

### Second Column

```python
print(arr[:,1])
```

**Output**

```python
[2 5]
```

---

### First Two Columns

```python
print(arr[:,0:2])
```

**Output**

```python
[[1 2]
 [4 5]]
```

**Explanation:** All rows, columns from `0` to `1` (`2` is excluded).

---

# Indexing vs Slicing

| Feature | Indexing           | Slicing                  |
| ------- | ------------------ | ------------------------ |
| Purpose | Access one element | Access multiple elements |
| Returns | Single value       | Array                    |
| Example | `arr[2]`           | `arr[1:4]`               |

---

# Must-Remember Points

* ✅ NumPy uses **0-based indexing**.
* ✅ Negative indexing starts from the end (`-1` is the last element).
* ✅ Slicing syntax is `arr[start:stop:step]`.
* ✅ The **start index is included**, but the **stop index is excluded**.
* ✅ In 2D arrays, use `arr[row, column]`.

---

# Quick Cheat Sheet

| Operation            | Syntax      | Description                  |
| -------------------- | ----------- | ---------------------------- |
| First element        | `arr[0]`    | Access first element         |
| Last element         | `arr[-1]`   | Access last element          |
| Slice                | `arr[1:4]`  | Elements from index 1 to 3   |
| From start           | `arr[:3]`   | First three elements         |
| To end               | `arr[2:]`   | From index 2 to the end      |
| Every second element | `arr[::2]`  | Skip one element each time   |
| Reverse array        | `arr[::-1]` | Reverse the array            |
| First row            | `arr[0,:]`  | All columns of the first row |
| First column         | `arr[:,0]`  | All rows of the first column |
| Specific element     | `arr[1,2]`  | Row 1, Column 2              |

### Interview Tip

A very common interview question is:

> **What is the difference between indexing and slicing?**

**Answer:**

* **Indexing** is used to access **a single element** from an array.
* **Slicing** is used to access **multiple elements** (a subarray) from an array.

---

## What is Boolean Indexing?

**Boolean Indexing** is a technique used to **filter or select elements from a NumPy array based on a condition**.

It returns only the elements for which the condition is **True**.

---

## Syntax

```python
arr[condition]
```

The condition can be:

* `>`
* `<`
* `>=`
* `<=`
* `==`
* `!=`

---

## Example 1: Select Elements Greater Than 30

```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[arr > 30])
```

**Output**

```python
[40 50]
```

### Explanation

Condition:

```python
arr > 30
```

Result:

```python
[False False False True True]
```

Only the elements corresponding to **True** are returned.

---

## Example 2: Select Even Numbers

```python
arr = np.array([1,2,3,4,5,6])

print(arr[arr % 2 == 0])
```

**Output**

```python
[2 4 6]
```

---

## Example 3: Select Odd Numbers

```python
print(arr[arr % 2 != 0])
```

**Output**

```python
[1 3 5]
```

---

## Example 4: Elements Less Than 25

```python
arr = np.array([10,20,30,40,50])

print(arr[arr < 25])
```

**Output**

```python
[10 20]
```

---

## Boolean Indexing on a 2D Array

```python
arr = np.array([
    [10,20,30],
    [40,50,60]
])

print(arr[arr > 30])
```

**Output**

```python
[40 50 60]
```

### Explanation

The condition is applied to every element, and only elements greater than `30` are returned.

---

# Common Boolean Conditions

| Condition             | Example          | Output                   |
| --------------------- | ---------------- | ------------------------ |
| Greater than          | `arr[arr > 20]`  | Elements greater than 20 |
| Less than             | `arr[arr < 20]`  | Elements less than 20    |
| Equal to              | `arr[arr == 20]` | Elements equal to 20     |
| Not equal to          | `arr[arr != 20]` | Elements except 20       |
| Greater than or equal | `arr[arr >= 20]` | Elements ≥ 20            |
| Less than or equal    | `arr[arr <= 20]` | Elements ≤ 20            |

---

# Multiple Conditions

Use `&` for **AND** and `|` for **OR**.

### AND (`&`)

```python
arr = np.array([10,20,30,40,50])

print(arr[(arr > 20) & (arr < 50)])
```

**Output**

```python
[30 40]
```

---

### OR (`|`)

```python
print(arr[(arr < 20) | (arr > 40)])
```

**Output**

```python
[10 50]
```

---

# Boolean Indexing vs Normal Indexing

| Feature | Normal Indexing          | Boolean Indexing             |
| ------- | ------------------------ | ---------------------------- |
| Purpose | Access elements by index | Access elements by condition |
| Example | `arr[2]`                 | `arr[arr > 20]`              |
| Returns | Specific element         | Filtered array               |

---

# Must-Remember Points

* ✅ Boolean indexing filters data based on a condition.
* ✅ It returns only the elements where the condition is **True**.
* ✅ Use comparison operators like `>`, `<`, `==`, `!=`, `>=`, and `<=`.
* ✅ Use `&` for **AND** and `|` for **OR** when combining multiple conditions.
* ✅ Enclose each condition in parentheses when using `&` or `|`.

---
