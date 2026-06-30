# Pandas Learning Notes

Pandas is an open-source Python library used for data manipulation, data analysis, and data cleaning. It is commonly used in data science, machine learning, artificial intelligence, data engineering, and MLOps.

The name **Pandas** comes from **Panel Data**, a term used in statistics and econometrics for multidimensional structured datasets.

## Table of Contents

- [Introduction](#introduction)
- [Installation and Import](#installation-and-import)
- [Main Data Structures](#main-data-structures)
- [Series](#series)
- [DataFrame](#dataframe)
- [Missing Data](#missing-data)
- [Merging, Joining, and Concatenation](#merging-joining-and-concatenation)
- [GroupBy and Aggregation](#groupby-and-aggregation)
- [Pivot Tables](#pivot-tables)
- [Common Operations](#common-operations)
- [Quick Reference](#quick-reference)
- [Interview Questions](#interview-questions)

## Introduction

Pandas helps you:

- Read data from CSV, Excel, JSON, SQL, and other formats.
- Clean missing, duplicate, or incorrect data.
- Filter, sort, and transform datasets.
- Perform statistical analysis.
- Merge, join, and reshape datasets.
- Prepare data for machine learning models.

### Features

| Feature | Purpose |
| --- | --- |
| Data manipulation | Add, remove, filter, sort, and transform data |
| Missing value handling | Detect, remove, or fill missing data |
| File support | Read and write CSV, Excel, JSON, SQL, and more |
| Grouping and aggregation | Summarize data by categories |
| Time-series support | Work with date and time based data |
| NumPy integration | Efficient numerical operations |

### Applications

- Data cleaning
- Data analysis
- Data visualization with Matplotlib or Seaborn
- Machine learning preprocessing
- Financial analysis
- Business intelligence
- Data engineering

## Installation and Import

Install Pandas:

```bash
pip install pandas
```

Import Pandas:

```python
import pandas as pd
```

`pd` is the standard alias used for Pandas.

### Simple Example

```python
import pandas as pd

data = {
    "Name": ["John", "Alice", "Bob"],
    "Age": [25, 30, 28]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
    Name  Age
0   John   25
1  Alice   30
2    Bob   28
```

## Main Data Structures

Pandas has two primary data structures:

| Data Structure | Description |
| --- | --- |
| `Series` | A one-dimensional labeled array, like a single column |
| `DataFrame` | A two-dimensional labeled table with rows and columns |

### Series Example

```text
0    10
1    20
2    30
dtype: int64
```

### DataFrame Example

```text
    Name  Age
0   John   25
1  Alice   30
2    Bob   28
```

### NumPy vs Pandas

| NumPy | Pandas |
| --- | --- |
| Works mainly with arrays | Works mainly with tables |
| Best for numerical computation | Best for data analysis |
| Usually stores one data type per array | Can store different data types in different columns |
| Uses position-based access | Supports labels and position-based access |
| Foundation library | Built on top of NumPy |

## Series

A **Series** is a one-dimensional labeled array that can store values of any data type, such as integers, floats, strings, or Python objects.

Think of a Series as a single column of a table.

### Syntax

```python
pd.Series(data, index=None)
```

### Create a Series from a List

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40])

print(s)
```

Output:

```text
0    10
1    20
2    30
3    40
dtype: int64
```

### Create a Series with a Custom Index

```python
import pandas as pd

s = pd.Series([10, 20, 30], index=["A", "B", "C"])

print(s)
```

Output:

```text
A    10
B    20
C    30
dtype: int64
```

### Create a Series from a Dictionary

```python
import pandas as pd

data = {
    "Math": 90,
    "Science": 85,
    "English": 88
}

s = pd.Series(data)

print(s)
```

Output:

```text
Math       90
Science    85
English    88
dtype: int64
```

Dictionary keys become index labels, and dictionary values become Series values.

### Access Series Values

```python
print(s.iloc[0])      # Access by position
print(s.loc["Math"])  # Access by label
```

### Series Attributes

| Attribute | Purpose |
| --- | --- |
| `s.index` | Returns index labels |
| `s.values` | Returns values as a NumPy array |
| `s.dtype` | Returns the data type |
| `s.size` | Returns the number of elements |
| `s.shape` | Returns the shape |

### Common Series Methods

| Method | Purpose |
| --- | --- |
| `s.head()` | First 5 values |
| `s.tail()` | Last 5 values |
| `s.sum()` | Sum of values |
| `s.mean()` | Average value |
| `s.max()` | Maximum value |
| `s.min()` | Minimum value |
| `s.sort_values()` | Sort by values |
| `s.sort_index()` | Sort by index labels |

### Series vs NumPy Array

| NumPy Array | Pandas Series |
| --- | --- |
| Has no labels | Has index labels |
| Uses positions only | Uses positions and labels |
| Mainly numerical | Supports many data types |
| Faster for pure numerical operations | Better for labeled analysis |

## DataFrame

A **DataFrame** is a two-dimensional labeled data structure that stores data in rows and columns, similar to an Excel spreadsheet or a SQL table.

A DataFrame can store different data types in different columns.

### Syntax

```python
pd.DataFrame(data, index=None, columns=None)
```

### Create a DataFrame from a Dictionary

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

Output:

```text
    Name  Age      City
0   John   25  New York
1  Alice   30    London
2    Bob   28     Paris
```

### Create a DataFrame with a Custom Index

```python
import pandas as pd

data = {
    "Name": ["John", "Alice"],
    "Age": [25, 30]
}

df = pd.DataFrame(data, index=["A", "B"])

print(df)
```

Output:

```text
    Name  Age
A   John   25
B  Alice   30
```

### Create a DataFrame from a List of Lists

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

### Create a DataFrame from a List of Dictionaries

```python
import pandas as pd

data = [
    {"Name": "John", "Age": 25},
    {"Name": "Alice", "Age": 30},
    {"Name": "Bob", "Age": 28}
]

df = pd.DataFrame(data)

print(df)
```

### Access DataFrame Data

Access one column:

```python
print(df["Name"])
```

Access multiple columns:

```python
print(df[["Name", "Age"]])
```

Access rows and cells:

```python
print(df.loc[0])          # Row by label
print(df.iloc[0])         # Row by position
print(df.loc[0, "Name"])  # Single value by label
```

### DataFrame Attributes

| Attribute | Purpose |
| --- | --- |
| `df.shape` | Returns `(rows, columns)` |
| `df.size` | Returns the total number of elements |
| `df.ndim` | Returns the number of dimensions |
| `df.columns` | Returns column names |
| `df.index` | Returns row labels |
| `df.dtypes` | Returns data type of each column |
| `df.values` | Returns data as a NumPy array |

### Common DataFrame Methods

| Method | Purpose |
| --- | --- |
| `df.head()` | First 5 rows |
| `df.tail()` | Last 5 rows |
| `df.info()` | Dataset information |
| `df.describe()` | Statistical summary |
| `df.sort_values()` | Sort rows by a column |
| `df.sort_index()` | Sort by index labels |
| `df.drop()` | Remove rows or columns |
| `df.rename()` | Rename columns |
| `df.copy()` | Create a copy |

### Series vs DataFrame

| Series | DataFrame |
| --- | --- |
| One-dimensional | Two-dimensional |
| Like one column | Like a full table |
| Has one index | Has row and column labels |
| Created with `pd.Series()` | Created with `pd.DataFrame()` |

## Missing Data

**Missing data** means values are not available or are empty in a dataset.

Pandas commonly represents missing values as:

- `NaN`
- `None`
- `pd.NA`

### Example Dataset

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

Output:

```text
    Name   Age      City
0   John  25.0  New York
1  Alice   NaN    London
2    Bob  28.0      None
3  David  30.0     Paris
```

### Why Handle Missing Data?

Missing values can:

- Produce incorrect analysis.
- Reduce machine learning model accuracy.
- Cause errors during calculations.
- Affect statistical results.

### Missing Data Functions

| Function | Purpose | Example |
| --- | --- | --- |
| `isnull()` | Detect missing values | `df.isnull()` |
| `notnull()` | Detect non-missing values | `df.notnull()` |
| `isna()` | Same as `isnull()` | `df.isna()` |
| `notna()` | Same as `notnull()` | `df.notna()` |
| `dropna()` | Remove missing values | `df.dropna()` |
| `fillna()` | Replace missing values | `df.fillna(0)` |

### Detect Missing Values

```python
print(df.isnull())
```

Output:

```text
    Name    Age   City
0  False  False  False
1  False   True  False
2  False  False   True
3  False  False  False
```

### Count Missing Values

```python
print(df.isnull().sum())
```

Output:

```text
Name    0
Age     1
City    1
dtype: int64
```

### Remove Missing Values

```python
clean_df = df.dropna()
print(clean_df)
```

Output:

```text
    Name   Age      City
0   John  25.0  New York
3  David  30.0     Paris
```

### Fill Missing Values

Fill all missing values with `0`:

```python
df.fillna(0)
```

Fill a numeric column with its mean:

```python
df["Age"] = df["Age"].fillna(df["Age"].mean())
```

Fill a text column with a specific value:

```python
df["City"] = df["City"].fillna("Unknown")
```

### `dropna()` vs `fillna()`

| Function | Purpose |
| --- | --- |
| `dropna()` | Removes rows or columns containing missing values |
| `fillna()` | Replaces missing values with a specified value |

## Merging, Joining, and Concatenation

Pandas provides three common ways to combine datasets.

| Method | Best Used When |
| --- | --- |
| `pd.merge()` | DataFrames share one or more common columns |
| `df.join()` | DataFrames should be combined by index |
| `pd.concat()` | DataFrames should be stacked by rows or columns |

### Merge with `pd.merge()`

`merge()` combines DataFrames using common columns. It is similar to SQL joins.

```python
import pandas as pd

students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["John", "Alice", "Bob"]
})

marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [85, 90, 78]
})

result = pd.merge(students, marks, on="ID", how="inner")

print(result)
```

Output:

```text
   ID   Name  Marks
0   1   John     85
1   2  Alice     90
2   3    Bob     78
```

Common merge types:

| Merge Type | Description |
| --- | --- |
| `inner` | Keeps matching rows only |
| `left` | Keeps all rows from the left DataFrame |
| `right` | Keeps all rows from the right DataFrame |
| `outer` | Keeps all rows from both DataFrames |

### Join with `join()`

`join()` combines DataFrames using index labels.

```python
left = students.set_index("ID")
right = marks.set_index("ID")

result = left.join(right)

print(result)
```

Output:

```text
     Name  Marks
ID
1    John     85
2   Alice     90
3     Bob     78
```

### Concatenate with `pd.concat()`

`concat()` stacks DataFrames vertically or horizontally.

Stack rows:

```python
df1 = pd.DataFrame({"Name": ["John"], "Marks": [85]})
df2 = pd.DataFrame({"Name": ["Alice"], "Marks": [90]})

result = pd.concat([df1, df2], axis=0, ignore_index=True)

print(result)
```

Output:

```text
    Name  Marks
0   John     85
1  Alice     90
```

Stack columns:

```python
result = pd.concat([df1, df2], axis=1)
```

### Merge vs Join vs Concat

| Function | Combines By | Common Use |
| --- | --- | --- |
| `pd.merge()` | Common columns | SQL-style joins |
| `df.join()` | Index labels | Index-based joins |
| `pd.concat()` | Axis | Stacking rows or columns |

## GroupBy and Aggregation

**GroupBy** groups rows that have the same value in one or more columns. **Aggregation** performs calculations on each group.

This is similar to the `GROUP BY` clause in SQL.

### Example Dataset

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

Output:

```text
  Department Employee  Salary
0         IT     John   50000
1         HR    Alice   40000
2         IT      Bob   60000
3         HR    David   45000
4      Sales      Eva   55000
```

### Basic Syntax

```python
df.groupby("Department")
```

This creates groups. To display results, apply an aggregation function.

### Common Aggregation Functions

| Function | Purpose |
| --- | --- |
| `sum()` | Sum of values |
| `mean()` | Average |
| `count()` | Count values |
| `max()` | Maximum value |
| `min()` | Minimum value |
| `median()` | Median |
| `std()` | Standard deviation |
| `var()` | Variance |

### GroupBy Examples

Sum salaries by department:

```python
df.groupby("Department")["Salary"].sum()
```

Output:

```text
Department
HR        85000
IT       110000
Sales     55000
Name: Salary, dtype: int64
```

Average salary by department:

```python
df.groupby("Department")["Salary"].mean()
```

Count employees by department:

```python
df.groupby("Department")["Employee"].count()
```

Multiple aggregations:

```python
df.groupby("Department")["Salary"].agg(["sum", "mean", "max", "min"])
```

Output:

```text
               sum     mean    max    min
Department
HR           85000  42500.0  45000  40000
IT          110000  55000.0  60000  50000
Sales        55000  55000.0  55000  55000
```

Group by multiple columns:

```python
df.groupby(["Department", "Employee"])["Salary"].sum()
```

## Pivot Tables

A **Pivot Table** summarizes, organizes, and analyzes data by grouping it into rows and columns and applying an aggregation function.

It is similar to Pivot Tables in Microsoft Excel.

### Syntax

```python
pd.pivot_table(
    data,
    values="column_name",
    index="row_column",
    columns="column_name",
    aggfunc="mean"
)
```

### Parameters

| Parameter | Purpose |
| --- | --- |
| `data` | Input DataFrame |
| `values` | Column to aggregate |
| `index` | Row labels |
| `columns` | Column labels |
| `aggfunc` | Aggregation function such as `sum`, `mean`, or `count` |

### Example Dataset

```python
import pandas as pd

data = {
    "Department": ["IT", "IT", "HR", "HR", "Sales", "Sales"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female"],
    "Salary": [50000, 60000, 40000, 45000, 55000, 52000]
}

df = pd.DataFrame(data)

print(df)
```

Output:

```text
  Department  Gender  Salary
0         IT    Male   50000
1         IT  Female   60000
2         HR    Male   40000
3         HR  Female   45000
4      Sales    Male   55000
5      Sales  Female   52000
```

### Average Salary by Department

```python
pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    aggfunc="mean"
)
```

Output:

```text
             Salary
Department
HR          42500.0
IT          55000.0
Sales       53500.0
```

### Department vs Gender

```python
pd.pivot_table(
    df,
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean"
)
```

Output:

```text
Gender       Female   Male
Department
HR            45000  40000
IT            60000  50000
Sales         52000  55000
```

### GroupBy vs Pivot Table

| GroupBy | Pivot Table |
| --- | --- |
| Groups data and returns grouped results | Summarizes data in a table format |
| More flexible for custom operations | Easier for reports and comparisons |
| Uses `groupby()` | Uses `pivot_table()` |

## Common Operations

Operations in Pandas are actions performed on Series and DataFrames to manipulate, analyze, transform, and summarize data.

### Operation Types

| Operation Type | Purpose |
| --- | --- |
| Arithmetic | Perform mathematical calculations |
| Comparison | Compare values |
| Statistical | Find summary statistics |
| String | Work with text data |
| Sorting | Sort rows or columns |
| Filtering | Select rows by condition |
| Aggregation | Calculate summary values |
| Apply | Apply custom functions |

### Arithmetic Operations

Arithmetic operations are performed element by element.

```python
import pandas as pd

s = pd.Series([10, 20, 30])

print(s + 10)
```

Output:

```text
0    20
1    30
2    40
dtype: int64
```

### Comparison and Filtering

```python
df["Marks"] > 80
```

```python
df[df["Marks"] > 80]
```

Common comparison operators:

| Operator | Meaning |
| --- | --- |
| `>` | Greater than |
| `<` | Less than |
| `==` | Equal |
| `!=` | Not equal |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

### Statistical Operations

| Function | Purpose |
| --- | --- |
| `sum()` | Sum |
| `mean()` | Average |
| `median()` | Median |
| `max()` | Maximum |
| `min()` | Minimum |
| `std()` | Standard deviation |
| `var()` | Variance |
| `count()` | Count non-missing values |

Example:

```python
df["Marks"].mean()
```

### String Operations

Use the `.str` accessor for text columns.

```python
df["Name"].str.upper()
```

| Method | Purpose |
| --- | --- |
| `str.upper()` | Convert to uppercase |
| `str.lower()` | Convert to lowercase |
| `str.title()` | Convert to title case |
| `str.replace()` | Replace text |
| `str.contains()` | Check for substring |

### Sorting

```python
df.sort_values("Marks")
df.sort_index()
```

### Aggregation

```python
df["Marks"].agg(["sum", "mean", "max"])
```

Output:

```text
sum     250.00
mean     83.33
max      95.00
Name: Marks, dtype: float64
```

### Apply Custom Functions

```python
df["Marks"].apply(lambda x: x + 5)
```

## Quick Reference

### Common Pandas Objects and Functions

| Object or Function | Purpose |
| --- | --- |
| `pd.Series()` | Create a Series |
| `pd.DataFrame()` | Create a DataFrame |
| `pd.read_csv()` | Read a CSV file |
| `pd.read_excel()` | Read an Excel file |
| `df.head()` | View the first 5 rows |
| `df.tail()` | View the last 5 rows |
| `df.info()` | Display dataset information |
| `df.describe()` | Display statistical summary |
| `df.isnull().sum()` | Count missing values |
| `df.dropna()` | Remove missing values |
| `df.fillna()` | Fill missing values |
| `pd.merge()` | Merge DataFrames by columns |
| `df.join()` | Join DataFrames by index |
| `pd.concat()` | Stack DataFrames |
| `df.groupby()` | Group rows for analysis |
| `pd.pivot_table()` | Create a pivot table |

### Common Operation Cheat Sheet

| Category | Common Syntax |
| --- | --- |
| Arithmetic | `+`, `-`, `*`, `/`, `**` |
| Comparison | `>`, `<`, `==`, `!=`, `>=`, `<=` |
| Filtering | `df[condition]` |
| Sorting | `df.sort_values("Column")` |
| Aggregation | `df["Column"].agg(["sum", "mean"])` |
| Grouping | `df.groupby("Column")["Value"].sum()` |
| Missing values | `df.isnull()`, `df.dropna()`, `df.fillna()` |
| Text columns | `df["Column"].str.upper()` |

### Key Points

- Pandas is used for data manipulation and analysis.
- Pandas is built on top of NumPy.
- The two main data structures are Series and DataFrame.
- A Series is like one labeled column.
- A DataFrame is like a full table with rows and columns.
- Missing data should be handled before analysis or model training.
- Use `merge()`, `join()`, and `concat()` to combine datasets.
- Use `groupby()` and `pivot_table()` to summarize data.
- Use `apply()` when you need a custom operation.

## Interview Questions

| Question | Answer |
| --- | --- |
| What is Pandas? | A Python library for data manipulation and analysis. |
| What are the two main Pandas data structures? | Series and DataFrame. |
| Is Pandas built on NumPy? | Yes. |
| What is a Series? | A one-dimensional labeled array. |
| What is a DataFrame? | A two-dimensional labeled table with rows and columns. |
| Can a DataFrame contain different data types? | Yes, different columns can store different data types. |
| What is the standard Pandas alias? | `pd` |
| Which function reads a CSV file? | `pd.read_csv()` |
| Which function detects missing values? | `isnull()` or `isna()` |
| Which function removes missing values? | `dropna()` |
| Which function replaces missing values? | `fillna()` |
| What does `shape` return? | The number of rows and columns. |
| Which function is similar to SQL JOIN? | `pd.merge()` |
| Which function stacks DataFrames? | `pd.concat()` |
| Which function groups rows for analysis? | `groupby()` |
| Which function creates a pivot table? | `pd.pivot_table()` |
| Which function applies a custom function? | `apply()` |
