# What is Pandas?

**Pandas** is a powerful, open-source Python library used for **data manipulation, data analysis, and data cleaning**. It provides easy-to-use data structures and functions for working with structured data such as tables, spreadsheets, and CSV files.

It is one of the most widely used libraries in **Data Science, Machine Learning, Artificial Intelligence, and MLOps**.

---

# Why is it called Pandas?

The name **Pandas** comes from **"Panel Data"**, a term used in statistics and econometrics for multidimensional structured datasets.

---

# Why Use Pandas?

Pandas helps you to:

* Read data from CSV, Excel, JSON, SQL, etc.
* Clean missing or incorrect data.
* Filter and sort data.
* Perform statistical analysis.
* Merge and join datasets.
* Prepare data for Machine Learning models.

---

# Main Data Structures

Pandas has two primary data structures:

| Data Structure | Description                                             |
| -------------- | ------------------------------------------------------- |
| **Series**     | A one-dimensional labeled array (like a single column). |
| **DataFrame**  | A two-dimensional labeled table with rows and columns.  |

Example:

```text
Series

0    10
1    20
2    30
```

```text
DataFrame

   Name   Age
0  John    25
1  Alice   30
2  Bob     28
```

---

# Installing Pandas

```bash
pip install pandas
```

---

# Importing Pandas

```python
import pandas as pd
```

`pd` is the standard alias used for Pandas.

---

# Simple Example

```python
import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 28]
}

df = pd.DataFrame(data)

print(df)
```

### Output

```text
    Name   Age
0   John    25
1  Alice    30
2    Bob    28
```

---

# Features of Pandas

* ✅ Fast and efficient data manipulation
* ✅ Easy handling of missing values
* ✅ Powerful filtering and sorting
* ✅ Read and write multiple file formats
* ✅ Grouping and aggregation
* ✅ Merge and join datasets
* ✅ Time-series analysis
* ✅ Built on top of NumPy

---

# Applications of Pandas

* Data Cleaning
* Data Analysis
* Data Visualization (with Matplotlib/Seaborn)
* Machine Learning Data Preprocessing
* Financial Analysis
* Business Intelligence
* Data Engineering

---

# NumPy vs Pandas

| NumPy                             | Pandas                                              |
| --------------------------------- | --------------------------------------------------- |
| Works with arrays                 | Works with tables (DataFrames)                      |
| Faster for numerical computations | Better for data analysis                            |
| Homogeneous data (same data type) | Can store different data types in different columns |
| Mainly numerical operations       | Data manipulation and analysis                      |
| Foundation library                | Built on top of NumPy                               |

---

# Commonly Used Pandas Objects

| Object            | Purpose                     |
| ----------------- | --------------------------- |
| `pd.Series()`     | Create a Series             |
| `pd.DataFrame()`  | Create a DataFrame          |
| `pd.read_csv()`   | Read a CSV file             |
| `pd.read_excel()` | Read an Excel file          |
| `df.head()`       | View the first 5 rows       |
| `df.tail()`       | View the last 5 rows        |
| `df.info()`       | Display dataset information |
| `df.describe()`   | Display statistical summary |

---

# Interview Questions

| Question                                         | Answer                                                      |
| ------------------------------------------------ | ----------------------------------------------------------- |
| What is Pandas?                                  | A Python library for data manipulation and analysis.        |
| What are the two main data structures in Pandas? | Series and DataFrame.                                       |
| Is Pandas built on NumPy?                        | Yes.                                                        |
| Why is Pandas used?                              | To clean, analyze, manipulate, and prepare structured data. |
| What is the standard alias for Pandas?           | `pd`                                                        |

---

# Key Points to Remember

* **Pandas** is a Python library for **data manipulation and analysis**.
* It is built on top of **NumPy**.
* The two main data structures are **Series** and **DataFrame**.
* It is widely used in **Data Science**, **Machine Learning**, **Data Engineering**, and **MLOps**.
* The standard import statement is:

```python
import pandas as pd
```

* Pandas makes it easy to read, clean, transform, analyze, and export structured data.

# What is a Series in Pandas?

A **Series** is a **one-dimensional labeled array** in Pandas that can store data of any type, such as integers, floats, strings, or even Python objects.

Think of a **Series** as **a single column of a table**.

---

# Syntax

```python
import pandas as pd

s = pd.Series(data)
```

---

# Creating a Series

### Example 1: From a List

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])

print(s)
```

### Output

```text
0    10
1    20
2    30
3    40
dtype: int64
```

### Explanation

* **0, 1, 2, 3** → Index (labels)
* **10, 20, 30, 40** → Data (values)
* **dtype** → Data type of the values

---

# Creating a Series with Custom Index

```python
import pandas as pd

s = pd.Series([10,20,30], index=['A','B','C'])

print(s)
```

### Output

```text
A    10
B    20
C    30
dtype: int64
```

### Explanation

Instead of the default index (`0,1,2`), we use custom labels (`A, B, C`).

---

# Creating a Series from a Dictionary

```python
import pandas as pd

data = {
    "Math":90,
    "Science":85,
    "English":88
}

s = pd.Series(data)

print(s)
```

### Output

```text
Math       90
Science    85
English    88
dtype: int64
```

The dictionary keys become the **index**, and the dictionary values become the **Series values**.

---

# Accessing Elements

### By Index Position

```python
print(s[0])
```

### By Label

```python
print(s["Math"])
```

---

# Series Attributes

| Attribute | Purpose                           |
| --------- | --------------------------------- |
| `index`   | Returns the index labels          |
| `values`  | Returns the data as a NumPy array |
| `dtype`   | Returns the data type             |
| `size`    | Returns the number of elements    |
| `shape`   | Returns the shape of the Series   |

Example:

```python
print(s.index)
print(s.values)
print(s.dtype)
print(s.size)
print(s.shape)
```

---

# Common Series Methods

| Method          | Purpose        |
| --------------- | -------------- |
| `head()`        | First 5 values |
| `tail()`        | Last 5 values  |
| `sum()`         | Sum of values  |
| `mean()`        | Average        |
| `max()`         | Maximum value  |
| `min()`         | Minimum value  |
| `sort_values()` | Sort by values |
| `sort_index()`  | Sort by index  |

Example:

```python
print(s.sum())
print(s.mean())
print(s.max())
```

---

# Series vs NumPy Array

| NumPy Array                     | Pandas Series             |
| ------------------------------- | ------------------------- |
| No labels                       | Has index labels          |
| Only numerical focus            | Can store many data types |
| Faster for numerical operations | Better for data analysis  |
| Uses positions only             | Uses positions and labels |

---

# Real-World Example

```python
import pandas as pd

marks = pd.Series(
    [85,90,78],
    index=["Rahul","Priya","Amit"]
)

print(marks)
```

Output

```text
Rahul    85
Priya    90
Amit     78
dtype: int64
```

This represents the marks of three students.

---

# Interview Questions

| Question                                   | Answer                                                 |
| ------------------------------------------ | ------------------------------------------------------ |
| What is a Series?                          | A one-dimensional labeled array in Pandas.             |
| Can a Series have custom indexes?          | Yes.                                                   |
| What is the default index?                 | `0, 1, 2, ...`                                         |
| Can a Series be created from a dictionary? | Yes.                                                   |
| Difference between NumPy array and Series? | A Series has labels (indexes); a NumPy array does not. |

---

# Key Points to Remember

* **Series** is a **1D labeled array**.
* It stores **values** along with **index labels**.
* It can be created from:

  * Lists
  * Tuples
  * Dictionaries
  * NumPy arrays
* Default index starts from **0**.
* Common constructor:

```python
import pandas as pd

s = pd.Series(data)
```

* A **Series** is like a **single column** of a DataFrame, while a **DataFrame** is a collection of multiple Series.

# What is a DataFrame in Pandas?

A **DataFrame** is a **two-dimensional labeled data structure** in Pandas that stores data in the form of **rows and columns**, similar to an Excel spreadsheet or a SQL table.

A **DataFrame** can store **different data types** (integers, floats, strings, dates, etc.) in different columns.

---

# Syntax

```python
import pandas as pd

df = pd.DataFrame(data)
```

---

# Creating a DataFrame

## Example 1: From a Dictionary

```python
import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 28],
    "City": ["New York", "London", "Paris"]
}

df = pd.DataFrame(data)

print(df)
```

### Output

```text
    Name  Age      City
0   John   25  New York
1  Alice   30    London
2    Bob   28     Paris
```

### Explanation

* **Rows** → Individual records (`0, 1, 2`)
* **Columns** → `Name`, `Age`, `City`
* Each **column** is a **Pandas Series**.

---

# Creating a DataFrame with a Custom Index

```python
import pandas as pd

data = {
    "Name": ["John", "Alice"],
    "Age": [25, 30]
}

df = pd.DataFrame(data, index=["A", "B"])

print(df)
```

### Output

```text
    Name  Age
A   John   25
B  Alice   30
```

---

# Creating a DataFrame from a List of Lists

```python
import pandas as pd

data = [
    ["John", 25],
    ["Alice", 30],
    ["Bob", 28]
]

df = pd.DataFrame(data, columns=["Name", "Age"])

print(df)
```

---

# Creating a DataFrame from a List of Dictionaries

```python
import pandas as pd

data = [
    {"Name":"John","Age":25},
    {"Name":"Alice","Age":30},
    {"Name":"Bob","Age":28}
]

df = pd.DataFrame(data)

print(df)
```

---

# Accessing Data

### Access a Single Column

```python
print(df["Name"])
```

Output

```text
0     John
1    Alice
2      Bob
Name: Name, dtype: object
```

A single column is returned as a **Series**.

---

### Access Multiple Columns

```python
print(df[["Name","Age"]])
```

---

# DataFrame Attributes

| Attribute | Purpose                   |
| --------- | ------------------------- |
| `shape`   | Returns `(rows, columns)` |
| `size`    | Total number of elements  |
| `ndim`    | Number of dimensions      |
| `columns` | Column names              |
| `index`   | Row labels                |
| `dtypes`  | Data type of each column  |
| `values`  | Data as a NumPy array     |

### Example

```python
print(df.shape)
print(df.columns)
print(df.dtypes)
```

---

# Common DataFrame Methods

| Method          | Purpose                        |
| --------------- | ------------------------------ |
| `head()`        | First 5 rows                   |
| `tail()`        | Last 5 rows                    |
| `info()`        | Dataset information            |
| `describe()`    | Statistical summary            |
| `sort_values()` | Sort rows by a column          |
| `sort_index()`  | Sort by index                  |
| `drop()`        | Remove rows or columns         |
| `rename()`      | Rename columns                 |
| `copy()`        | Create a copy of the DataFrame |

---

# Real-World Example

```python
import pandas as pd

students = {
    "Name":["Rahul","Priya","Amit"],
    "Marks":[85,90,78],
    "Grade":["A","A+","B"]
}

df = pd.DataFrame(students)

print(df)
```

Output

```text
    Name  Marks Grade
0  Rahul     85     A
1  Priya     90    A+
2   Amit     78     B
```

This DataFrame stores information about students.

---

# Series vs DataFrame

| Series                      | DataFrame                      |
| --------------------------- | ------------------------------ |
| One-dimensional             | Two-dimensional                |
| Single column               | Multiple columns               |
| Has one index               | Has row and column labels      |
| Created using `pd.Series()` | Created using `pd.DataFrame()` |

---

# Interview Questions

| Question                                      | Answer                                     |
| --------------------------------------------- | ------------------------------------------ |
| What is a DataFrame?                          | A two-dimensional labeled table in Pandas. |
| Can a DataFrame contain different data types? | Yes.                                       |
| What is each column of a DataFrame?           | A Pandas Series.                           |
| Which function creates a DataFrame?           | `pd.DataFrame()`                           |
| What does `shape` return?                     | Number of rows and columns.                |

---

# Key Points to Remember

* **DataFrame** is a **2D labeled data structure** with **rows and columns**.
* It is the **most commonly used** data structure in Pandas.
* Each **column is a Series**.
* It can store **different data types** in different columns.
* Common constructor:

```python
import pandas as pd

df = pd.DataFrame(data)
```

* Common attributes:

  * `shape`
  * `columns`
  * `index`
  * `dtypes`
  * `values`
* Common methods:

  * `head()`
  * `tail()`
  * `info()`
  * `describe()`

### Easy Way to Remember

* **Series = One Column**
* **DataFrame = Multiple Columns (Table)**


## What is Missing Data?

**Missing data** refers to **values that are not available or are empty** in a dataset.

In Pandas, missing values are usually represented as:

* `NaN` (Not a Number)
* `None`
* `pd.NA` (newer missing value indicator)

Missing data is common in real-world datasets due to incomplete data entry, sensor failures, or unavailable information.

---

# Example

```python
import pandas as pd
import numpy as np

data = {
    "Name": ["John", "Alice", "Bob", "David"],
    "Age": [25, np.nan, 28, 30],
    "City": ["New York", "London", None, "Paris"]
}

df = pd.DataFrame(data)

print(df)
```

### Output

```text
    Name   Age      City
0   John  25.0  New York
1  Alice   NaN    London
2    Bob  28.0      None
3  David  30.0     Paris
```

---

# Why Handle Missing Data?

Missing values can:

* Produce incorrect analysis.
* Reduce machine learning model accuracy.
* Cause errors during calculations.
* Affect statistical results.

---

# Common Functions for Missing Data

| Function    | Purpose                   | Example        |
| ----------- | ------------------------- | -------------- |
| `isnull()`  | Detect missing values     | `df.isnull()`  |
| `notnull()` | Detect non-missing values | `df.notnull()` |
| `isna()`    | Same as `isnull()`        | `df.isna()`    |
| `notna()`   | Same as `notnull()`       | `df.notna()`   |
| `dropna()`  | Remove missing values     | `df.dropna()`  |
| `fillna()`  | Replace missing values    | `df.fillna(0)` |

---

# 1. Detect Missing Values

```python
print(df.isnull())
```

### Output

```text
    Name    Age   City
0  False  False  False
1  False   True  False
2  False  False   True
3  False  False  False
```

**Explanation:**

* `True` → Missing value
* `False` → Value is present

---

# 2. Count Missing Values

```python
print(df.isnull().sum())
```

### Output

```text
Name    0
Age     1
City    1
dtype: int64
```

---

# 3. Remove Missing Values

```python
df.dropna()
```

### Output

```text
    Name   Age      City
0   John  25.0  New York
3  David  30.0     Paris
```

Rows containing missing values are removed.

---

# 4. Fill Missing Values

### Fill with 0

```python
df.fillna(0)
```

### Output

```text
    Name   Age      City
0   John  25.0  New York
1  Alice   0.0    London
2    Bob  28.0         0
3  David  30.0     Paris
```

---

### Fill with Mean

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

This replaces missing ages with the average age.

---

### Fill with a Specific Value

```python
df["City"] = df["City"].fillna("Unknown")
```

---

# Difference Between `dropna()` and `fillna()`

| Function   | Purpose                                           |
| ---------- | ------------------------------------------------- |
| `dropna()` | Removes rows or columns containing missing values |
| `fillna()` | Replaces missing values with a specified value    |

---

# Common Parameters

| Function   | Parameter | Purpose               |
| ---------- | --------- | --------------------- |
| `dropna()` | `axis=0`  | Remove rows (default) |
| `dropna()` | `axis=1`  | Remove columns        |
| `fillna()` | `value`   | Replacement value     |

---

# Interview Questions

| Question                                   | Answer                                          |
| ------------------------------------------ | ----------------------------------------------- |
| What is missing data?                      | Data that is unavailable or empty in a dataset. |
| How is missing data represented in Pandas? | `NaN`, `None`, or `pd.NA`.                      |
| Which function detects missing values?     | `isnull()` or `isna()`.                         |
| Which function removes missing values?     | `dropna()`.                                     |
| Which function replaces missing values?    | `fillna()`.                                     |

---

# Quick Cheat Sheet

| Operation                | Function               |
| ------------------------ | ---------------------- |
| Check missing values     | `df.isnull()`          |
| Count missing values     | `df.isnull().sum()`    |
| Check non-missing values | `df.notnull()`         |
| Remove missing rows      | `df.dropna()`          |
| Fill with 0              | `df.fillna(0)`         |
| Fill with mean           | `df.fillna(df.mean())` |

---

# Key Points to Remember

* **Missing data** means some values are unavailable.
* Pandas represents missing values using **`NaN`**, **`None`**, or **`pd.NA`**.
* Use:

  * `isnull()` / `isna()` → Detect missing values.
  * `notnull()` / `notna()` → Detect available values.
  * `dropna()` → Remove missing data.
  * `fillna()` → Replace missing data.
* Handling missing values is an essential step in **data cleaning** before performing analysis or training machine learning models.

# Merging, Joining, and Concatenation in Pandas

**Merging**, **Joining**, and **Concatenation** are used to **combine two or more DataFrames** into a single DataFrame.

The main difference is **how** they combine the data.

| Method          | Combines Based On | Similar To           |
| --------------- | ----------------- | -------------------- |
| **Merge**       | Common column(s)  | SQL Join             |
| **Join**        | Index (default)   | SQL Join using Index |
| **Concatenate** | Rows or Columns   | Stacking tables      |

---

# 1. Merging (`pd.merge()`)

## What is Merge?

**Merge** combines two DataFrames based on one or more **common columns**.

It works like an **SQL JOIN**.

### Syntax

```python
pd.merge(df1, df2, on="column_name")
```

### Example

```python
import pandas as pd

df1 = pd.DataFrame({
    "ID":[1,2,3],
    "Name":["John","Alice","Bob"]
})

df2 = pd.DataFrame({
    "ID":[1,2,3],
    "Marks":[85,90,78]
})

result = pd.merge(df1, df2, on="ID")

print(result)
```

### Output

```text
   ID   Name  Marks
0   1   John     85
1   2  Alice     90
2   3    Bob     78
```

### Explanation

Both DataFrames are combined using the common column **ID**.

---

## Types of Merge

| Merge Type | Description                          |
| ---------- | ------------------------------------ |
| `inner`    | Returns only matching rows (Default) |
| `left`     | All rows from the left DataFrame     |
| `right`    | All rows from the right DataFrame    |
| `outer`    | All rows from both DataFrames        |

Example

```python
pd.merge(df1, df2, on="ID", how="left")
```

---

# 2. Joining (`join()`)

## What is Join?

**Join** combines DataFrames using their **index** by default.

### Syntax

```python
df1.join(df2)
```

### Example

```python
import pandas as pd

df1 = pd.DataFrame({
    "Name":["John","Alice","Bob"]
})

df2 = pd.DataFrame({
    "Marks":[85,90,78]
})

result = df1.join(df2)

print(result)
```

### Output

```text
    Name  Marks
0   John     85
1  Alice     90
2    Bob     78
```

### Explanation

The DataFrames are joined using the **row index**.

---

# 3. Concatenation (`pd.concat()`)

## What is Concatenation?

**Concatenation** combines DataFrames by **stacking** them either:

* Vertically (rows)
* Horizontally (columns)

### Syntax

```python
pd.concat([df1, df2])
```

---

## Vertical Concatenation (`axis=0`)

```python
import pandas as pd

df1 = pd.DataFrame({
    "A":[1,2]
})

df2 = pd.DataFrame({
    "A":[3,4]
})

result = pd.concat([df1,df2])

print(result)
```

### Output

```text
   A
0  1
1  2
0  3
1  4
```

---

## Horizontal Concatenation (`axis=1`)

```python
result = pd.concat([df1,df2], axis=1)
```

### Output

```text
   A  A
0  1  3
1  2  4
```

---

# Difference Between Merge, Join, and Concat

| Feature    | Merge         | Join             | Concat          |
| ---------- | ------------- | ---------------- | --------------- |
| Function   | `pd.merge()`  | `join()`         | `pd.concat()`   |
| Based On   | Common column | Index (default)  | Rows or Columns |
| Similar To | SQL JOIN      | SQL JOIN (Index) | Stack Tables    |
| Axis       | Columns       | Index            | Rows/Columns    |

---

# Most Common Parameters

| Function   | Parameter | Purpose                                          |
| ---------- | --------- | ------------------------------------------------ |
| `merge()`  | `on`      | Common column                                    |
| `merge()`  | `how`     | Type of join (`inner`, `left`, `right`, `outer`) |
| `concat()` | `axis=0`  | Stack rows                                       |
| `concat()` | `axis=1`  | Stack columns                                    |

---

# Interview Questions

| Question                               | Answer                                        |
| -------------------------------------- | --------------------------------------------- |
| What is Merge?                         | Combines DataFrames using common columns.     |
| What is Join?                          | Combines DataFrames using indexes.            |
| What is Concatenation?                 | Stacks DataFrames vertically or horizontally. |
| Which function is similar to SQL JOIN? | `pd.merge()`                                  |
| Which function stacks DataFrames?      | `pd.concat()`                                 |

---

# Quick Cheat Sheet

| Operation              | Function            |
| ---------------------- | ------------------- |
| Merge by common column | `pd.merge()`        |
| Join by index          | `df.join()`         |
| Stack rows             | `pd.concat(axis=0)` |
| Stack columns          | `pd.concat(axis=1)` |

---

# Easy Way to Remember

| Function   | Memory Trick             |
| ---------- | ------------------------ |
| **Merge**  | **Match Columns**        |
| **Join**   | **Join Indexes**         |
| **Concat** | **Combine/Stack Tables** |

---

# Key Points to Remember

* **`pd.merge()`** → Use when two DataFrames have a **common column**.
* **`join()`** → Use when DataFrames share the **same index**.
* **`pd.concat()`** → Use to **stack DataFrames** vertically (`axis=0`) or horizontally (`axis=1`).
* `merge()` is the most commonly used function in **Data Analysis**, **Machine Learning**, and **SQL-related interview questions**.

# GroupBy and Aggregation in Pandas

## What is GroupBy?

**GroupBy** is a Pandas operation used to **group rows that have the same value in one or more columns** and then perform calculations (aggregations) on each group.

It is similar to the **`GROUP BY`** clause in SQL.

---

# Syntax

```python
df.groupby("column_name")
```

---

# Example Dataset

```python
import pandas as pd

data = {
    "Department": ["IT", "HR", "IT", "HR", "Sales"],
    "Employee": ["John", "Alice", "Bob", "David", "Eva"],
    "Salary": [50000, 40000, 60000, 45000, 55000]
}

df = pd.DataFrame(data)

print(df)
```

### Output

```text
  Department Employee  Salary
0         IT     John   50000
1         HR    Alice   40000
2         IT      Bob   60000
3         HR    David   45000
4      Sales      Eva   55000
```

---

# Group By Department

```python
df.groupby("Department")
```

This creates groups but does not display results until an aggregation function is applied.

---

# What is Aggregation?

**Aggregation** means performing calculations on each group, such as:

* Sum
* Mean
* Count
* Maximum
* Minimum

---

# Common Aggregation Functions

| Function   | Purpose            |
| ---------- | ------------------ |
| `sum()`    | Sum of values      |
| `mean()`   | Average            |
| `count()`  | Count of values    |
| `max()`    | Maximum value      |
| `min()`    | Minimum value      |
| `median()` | Median             |
| `std()`    | Standard deviation |
| `var()`    | Variance           |

---

# Example 1: Sum

```python
df.groupby("Department")["Salary"].sum()
```

### Output

```text
Department
HR        85000
IT       110000
Sales     55000
```

---

# Example 2: Average Salary

```python
df.groupby("Department")["Salary"].mean()
```

### Output

```text
Department
HR       42500
IT       55000
Sales    55000
```

---

# Example 3: Maximum Salary

```python
df.groupby("Department")["Salary"].max()
```

### Output

```text
Department
HR       45000
IT       60000
Sales    55000
```

---

# Example 4: Count Employees

```python
df.groupby("Department")["Employee"].count()
```

### Output

```text
Department
HR       2
IT       2
Sales    1
```

---

# Multiple Aggregations

Use `agg()` to perform multiple calculations at once.

```python
df.groupby("Department")["Salary"].agg(["sum","mean","max","min"])
```

### Output

```text
             sum     mean    max    min
Department
HR         85000  42500.0  45000  40000
IT        110000  55000.0  60000  50000
Sales      55000  55000.0  55000  55000
```

---

# Group By Multiple Columns

```python
df.groupby(["Department","Employee"])["Salary"].sum()
```

This groups data using both **Department** and **Employee**.

---

# Difference Between GroupBy and Aggregation

| GroupBy                   | Aggregation                        |
| ------------------------- | ---------------------------------- |
| Creates groups            | Performs calculations on groups    |
| Similar to SQL `GROUP BY` | Similar to SQL aggregate functions |
| Returns grouped object    | Returns summarized results         |

---

# Most Important GroupBy Functions

| Function  | Example             |
| --------- | ------------------- |
| `sum()`   | `groupby().sum()`   |
| `mean()`  | `groupby().mean()`  |
| `count()` | `groupby().count()` |
| `max()`   | `groupby().max()`   |
| `min()`   | `groupby().min()`   |
| `agg()`   | `groupby().agg()`   |

---

# Interview Questions

| Question                                       | Answer                                         |
| ---------------------------------------------- | ---------------------------------------------- |
| What is GroupBy?                               | Groups rows with the same values for analysis. |
| What is Aggregation?                           | Performs calculations on grouped data.         |
| Which function performs multiple aggregations? | `agg()`                                        |
| Which SQL clause is similar to GroupBy?        | `GROUP BY`                                     |
| Can GroupBy use multiple columns?              | Yes.                                           |

---

# Quick Cheat Sheet

| Operation             | Syntax                                                         |
| --------------------- | -------------------------------------------------------------- |
| Group by one column   | `df.groupby("Department")`                                     |
| Sum                   | `df.groupby("Department")["Salary"].sum()`                     |
| Mean                  | `df.groupby("Department")["Salary"].mean()`                    |
| Count                 | `df.groupby("Department")["Employee"].count()`                 |
| Maximum               | `df.groupby("Department")["Salary"].max()`                     |
| Multiple aggregations | `df.groupby("Department")["Salary"].agg(["sum","mean","max"])` |

---

# Key Points to Remember

* **GroupBy** groups rows based on common values.
* **Aggregation** performs calculations on those groups.
* GroupBy is similar to SQL's **`GROUP BY`** clause.
* Common aggregation functions:

  * `sum()`
  * `mean()`
  * `count()`
  * `max()`
  * `min()`
  * `agg()`
* `agg()` is useful when you want multiple statistics in a single operation.

### Easy Way to Remember

* **GroupBy = Divide the data into groups**
* **Aggregation = Calculate statistics for each group**


## What is a Pivot Table?

A **Pivot Table** is a powerful Pandas feature used to **summarize, organize, and analyze data** by grouping it into rows and columns and applying an aggregation function (such as `sum`, `mean`, or `count`).

It is similar to **Pivot Tables in Microsoft Excel**.

---

# Why Use Pivot Tables?

Pivot tables help you:

* Summarize large datasets.
* Calculate totals, averages, counts, etc.
* Compare data across categories.
* Create reports for data analysis.

---

# Syntax

```python id="zyl3v2"
pd.pivot_table(
    data,
    values="column_name",
    index="row_column",
    columns="column_name",
    aggfunc="mean"
)
```

### Parameters

| Parameter | Purpose                                             |
| --------- | --------------------------------------------------- |
| `data`    | Input DataFrame                                     |
| `values`  | Column to aggregate                                 |
| `index`   | Row labels                                          |
| `columns` | Column labels                                       |
| `aggfunc` | Aggregation function (`sum`, `mean`, `count`, etc.) |

---

# Example Dataset

```python id="p4y07k"
import pandas as pd

data = {
    "Department": ["IT","IT","HR","HR","Sales","Sales"],
    "Gender": ["Male","Female","Male","Female","Male","Female"],
    "Salary": [50000,60000,40000,45000,55000,52000]
}

df = pd.DataFrame(data)

print(df)
```

### Output

```text id="01f4jw"
  Department  Gender  Salary
0         IT    Male   50000
1         IT  Female   60000
2         HR    Male   40000
3         HR  Female   45000
4      Sales    Male   55000
5      Sales  Female   52000
```

---

# Example 1: Average Salary by Department

```python id="c73pi7"
pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc="mean"
)
```

### Output

```text id="jifkgv"
            Salary
Department
HR         42500
IT         55000
Sales      53500
```

---

# Example 2: Department vs Gender

```python id="xj6c3z"
pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean"
)
```

### Output

```text id="c96sq5"
Gender       Female   Male
Department
HR            45000  40000
IT            60000  50000
Sales         52000  55000
```

### Explanation

* **Rows** → Department
* **Columns** → Gender
* **Values** → Average Salary

---

# Example 3: Sum of Salary

```python id="k4w9ml"
pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc="sum"
)
```

### Output

```text id="1by3gt"
            Salary
Department
HR          85000
IT         110000
Sales      107000
```

---

# Common Aggregation Functions

| Function  | Purpose |
| --------- | ------- |
| `"sum"`   | Total   |
| `"mean"`  | Average |
| `"count"` | Count   |
| `"max"`   | Maximum |
| `"min"`   | Minimum |

---

# Difference Between GroupBy and Pivot Table

| GroupBy                             | Pivot Table                       |
| ----------------------------------- | --------------------------------- |
| Groups data                         | Summarizes data in a table format |
| More flexible for custom operations | Easier for reports and summaries  |
| Uses `groupby()`                    | Uses `pivot_table()`              |
| Usually returns grouped results     | Returns a formatted summary table |

---

# Most Important Parameters

| Parameter | Example        |
| --------- | -------------- |
| `values`  | `"Salary"`     |
| `index`   | `"Department"` |
| `columns` | `"Gender"`     |
| `aggfunc` | `"mean"`       |

---

# Interview Questions

| Question                                            | Answer                                                       |
| --------------------------------------------------- | ------------------------------------------------------------ |
| What is a Pivot Table?                              | A tool used to summarize and analyze data in a table format. |
| Which function creates a Pivot Table?               | `pd.pivot_table()`                                           |
| Which parameter specifies row labels?               | `index`                                                      |
| Which parameter specifies column labels?            | `columns`                                                    |
| Which parameter specifies the aggregation function? | `aggfunc`                                                    |

---

# Quick Cheat Sheet

| Operation          | Syntax             |
| ------------------ | ------------------ |
| Create Pivot Table | `pd.pivot_table()` |
| Average            | `aggfunc="mean"`   |
| Sum                | `aggfunc="sum"`    |
| Count              | `aggfunc="count"`  |
| Row labels         | `index="Column"`   |
| Column labels      | `columns="Column"` |
| Values             | `values="Column"`  |

---

# Key Points to Remember

* **Pivot Table** is used to **summarize and analyze large datasets**.
* It is similar to **Excel Pivot Tables**.
* It is created using **`pd.pivot_table()`**.
* Main parameters:

  * `values` → Data to summarize
  * `index` → Row labels
  * `columns` → Column labels
  * `aggfunc` → Aggregation function
* Common aggregation functions:

  * `mean`
  * `sum`
  * `count`
  * `max`
  * `min`

### Easy Way to Remember

* **GroupBy** → **Group + Calculate**
* **Pivot Table** → **Group + Calculate + Display as a Summary Table**

# Operations in Pandas

## What are Operations in Pandas?

**Operations in Pandas** are actions performed on **Series** and **DataFrames** to manipulate, analyze, transform, and summarize data.

These operations help in cleaning data, performing calculations, filtering records, sorting, grouping, and preparing data for Machine Learning.

---

# Types of Operations in Pandas

| Operation Type         | Purpose                           |
| ---------------------- | --------------------------------- |
| Arithmetic Operations  | Perform mathematical calculations |
| Comparison Operations  | Compare values                    |
| Statistical Operations | Find summary statistics           |
| String Operations      | Work with text data               |
| Sorting Operations     | Sort rows or columns              |
| Filtering Operations   | Select specific rows              |
| Aggregate Operations   | Calculate summary values          |
| Apply Operations       | Apply custom functions            |

---

# 1. Arithmetic Operations

Arithmetic operations are performed **element-wise**.

```python
import pandas as pd

s = pd.Series([10,20,30])

print(s + 10)
```

### Output

```text
0    20
1    30
2    40
dtype: int64
```

### Common Arithmetic Operations

| Operation      | Example   |
| -------------- | --------- |
| Addition       | `df + 10` |
| Subtraction    | `df - 5`  |
| Multiplication | `df * 2`  |
| Division       | `df / 2`  |
| Power          | `df ** 2` |

---

# 2. Comparison Operations

Used to compare values.

```python
df["Marks"] > 80
```

### Output

```text
0    False
1     True
2    False
dtype: bool
```

### Comparison Operators

| Operator              | Example |
| --------------------- | ------- |
| Greater than          | `>`     |
| Less than             | `<`     |
| Equal                 | `==`    |
| Not Equal             | `!=`    |
| Greater than or Equal | `>=`    |
| Less than or Equal    | `<=`    |

---

# 3. Statistical Operations

Used to calculate summary statistics.

| Function   | Purpose                  |
| ---------- | ------------------------ |
| `sum()`    | Sum                      |
| `mean()`   | Average                  |
| `median()` | Median                   |
| `max()`    | Maximum                  |
| `min()`    | Minimum                  |
| `std()`    | Standard deviation       |
| `var()`    | Variance                 |
| `count()`  | Count non-missing values |

Example

```python
df["Marks"].mean()
```

---

# 4. String Operations

Used for text columns.

```python
df["Name"].str.upper()
```

### Common String Methods

| Method           | Purpose              |
| ---------------- | -------------------- |
| `str.upper()`    | Convert to uppercase |
| `str.lower()`    | Convert to lowercase |
| `str.title()`    | Title case           |
| `str.replace()`  | Replace text         |
| `str.contains()` | Check substring      |

---

# 5. Sorting Operations

Sort data by values or index.

```python
df.sort_values("Marks")
```

```python
df.sort_index()
```

### Functions

| Function        | Purpose               |
| --------------- | --------------------- |
| `sort_values()` | Sort by column values |
| `sort_index()`  | Sort by index         |

---

# 6. Filtering Operations

Select rows based on a condition.

```python
df[df["Marks"] > 80]
```

### Example

```python
df[df["Age"] >= 18]
```

---

# 7. Aggregate Operations

Used to summarize data.

```python
df["Marks"].agg(["sum","mean","max"])
```

### Output

```text
sum      250
mean    83.33
max       95
```

---

# 8. Apply Operations

Apply a custom function to rows or columns.

```python
df["Marks"].apply(lambda x: x + 5)
```

### Example

Increase every student's marks by 5.

---

# Commonly Used Operations

| Function         | Purpose                 |
| ---------------- | ----------------------- |
| `head()`         | First 5 rows            |
| `tail()`         | Last 5 rows             |
| `info()`         | Dataset information     |
| `describe()`     | Statistical summary     |
| `value_counts()` | Count unique values     |
| `unique()`       | Unique values           |
| `nunique()`      | Number of unique values |

---

# Interview Questions

| Question                                  | Answer                                                                   |
| ----------------------------------------- | ------------------------------------------------------------------------ |
| What are Pandas operations?               | Operations used to manipulate and analyze data in Series and DataFrames. |
| Which function calculates the average?    | `mean()`                                                                 |
| Which function sorts data?                | `sort_values()`                                                          |
| Which function applies a custom function? | `apply()`                                                                |
| Which function returns unique values?     | `unique()`                                                               |

---

# Quick Cheat Sheet

| Category    | Functions                                       |
| ----------- | ----------------------------------------------- |
| Arithmetic  | `+`, `-`, `*`, `/`, `**`                        |
| Comparison  | `>`, `<`, `==`, `!=`, `>=`, `<=`                |
| Statistics  | `sum()`, `mean()`, `median()`, `max()`, `min()` |
| Strings     | `str.upper()`, `str.lower()`, `str.replace()`   |
| Sorting     | `sort_values()`, `sort_index()`                 |
| Filtering   | `df[condition]`                                 |
| Aggregation | `agg()`                                         |
| Apply       | `apply()`                                       |
| Information | `head()`, `tail()`, `info()`, `describe()`      |

---

# Key Points to Remember

* **Operations in Pandas** are used to manipulate, analyze, and transform data.
* Arithmetic and comparison operations work **element-wise**.
* Statistical functions help summarize data.
* String operations work on text columns using the **`.str`** accessor.
* Filtering selects rows that satisfy a condition.
* `apply()` lets you execute custom functions on Series or DataFrames.
* These operations are fundamental for **data cleaning**, **exploratory data analysis (EDA)**, and **machine learning preprocessing**.
