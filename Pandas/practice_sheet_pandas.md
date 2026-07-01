# Pandas Practice Sheet

These questions cover important Pandas topics from beginner to advanced level and are useful for data science, machine learning, MLOps, and interview preparation.

## Level 1: Series (1-8)

1. Create a Pandas Series from a list.
2. Create a Series with custom indexes.
3. Create a Series from a dictionary.
4. Print the first and last element of a Series.
5. Find the `dtype`, `size`, `shape`, and `index` of a Series.
6. Calculate the sum, mean, maximum, and minimum of a Series.
7. Sort a Series by values.
8. Sort a Series by index.

## Level 2: DataFrame Creation (9-16)

9. Create a DataFrame from a dictionary.
10. Create a DataFrame from a list of lists.
11. Create a DataFrame from a list of dictionaries.
12. Create a DataFrame with custom indexes.
13. Print the first 5 rows using `head()`.
14. Print the last 3 rows using `tail()`.
15. Display dataset information using `info()`.
16. Display statistical summary using `describe()`.

## Level 3: DataFrame Attributes (17-22)

17. Find the `shape` of a DataFrame.
18. Find the column names.
19. Find the row indexes.
20. Find the data types of all columns.
21. Find the total number of elements.
22. Convert a DataFrame into a NumPy array using `values`.

## Level 4: Selecting Data (23-30)

23. Select a single column.
24. Select multiple columns.
25. Select the first row using `iloc`.
26. Select the first row using `loc`.
27. Select rows from index 2 to 5.
28. Select rows where `Age > 25`.
29. Select rows where `Salary > 50000`.
30. Select rows where `Department == "IT"`.

## Level 5: Missing Data (31-36)

31. Detect missing values using `isnull()`.
32. Count missing values in each column.
33. Remove rows containing missing values.
34. Fill missing values with `0`.
35. Fill missing values using the column mean.
36. Replace missing city names with `"Unknown"`.

## Level 6: Sorting and Filtering (37-41)

37. Sort the DataFrame by salary in ascending order.
38. Sort by age in descending order.
39. Filter employees whose salary is greater than 60,000.
40. Filter students scoring between 70 and 90.
41. Display employees from the HR department.

## Level 7: Operations (42-47)

42. Add 10 to every value in the `Marks` column.
43. Create a new column `Bonus` as 10% of `Salary`.
44. Convert all names to uppercase.
45. Replace `"Male"` with `"M"` and `"Female"` with `"F"`.
46. Find all unique departments.
47. Count the number of employees in each department.

## Level 8: GroupBy and Aggregation (48-52)

48. Find the average salary of each department.
49. Find the maximum salary in each department.
50. Count employees in each department.
51. Find the sum of salaries for each department.
52. Use `agg()` to calculate `sum`, `mean`, `max`, and `min` for salaries.

## Level 9: Merge, Join, and Concatenation (53-56)

53. Merge two DataFrames using a common `ID` column.
54. Join two DataFrames using their indexes.
55. Concatenate two DataFrames vertically.
56. Concatenate two DataFrames horizontally.

## Level 10: Pivot Table (57-60)

57. Create a pivot table showing the average salary by department.
58. Create a pivot table showing total sales by city.
59. Create a pivot table with department as rows and gender as columns.
60. Create a pivot table using `sum` as the aggregation function.

## Bonus Interview Questions (61-70)

61. Rename a column.
62. Drop a column.
63. Drop a row.
64. Change the data type of a column using `astype()`.
65. Find duplicate rows.
66. Remove duplicate rows.
67. Reset the DataFrame index.
68. Set a column as the index.
69. Save a DataFrame to a CSV file.
70. Read a CSV file into a DataFrame.

## Mini Projects

### Project 1: Student Marks Analysis

Create a DataFrame with the following columns:

| Column | Description |
| --- | --- |
| `Roll No` | Student roll number |
| `Name` | Student name |
| `Math` | Math marks |
| `Science` | Science marks |
| `English` | English marks |

Perform the following tasks:

1. Find the average marks of each student.
2. Find the topper.
3. Find students scoring below 35 in any subject.
4. Add a `Total` column.
5. Add a `Percentage` column.
6. Assign grades: A, B, C, D, or Fail.
7. Sort students by percentage.
8. Count students in each grade.

### Project 2: Employee Data Analysis

Create a DataFrame with the following columns:

| Column | Description |
| --- | --- |
| `Employee ID` | Unique employee ID |
| `Name` | Employee name |
| `Department` | Employee department |
| `Salary` | Employee salary |
| `Experience` | Years of experience |

Perform the following tasks:

1. Find the average salary by department.
2. Find the highest-paid employee.
3. Add a `Bonus` column equal to 15% of salary.
4. Find employees with more than 5 years of experience.
5. Sort by salary from highest to lowest.
6. Create a pivot table for department-wise salary.
7. Count employees in each department.

### Project 3: Sales Data Analysis

Create a DataFrame with the following columns:

| Column | Description |
| --- | --- |
| `Product` | Product name |
| `Category` | Product category |
| `City` | Sales city |
| `Sales` | Sales amount |
| `Quantity` | Quantity sold |

Perform the following tasks:

1. Find total sales.
2. Find the best-selling product.
3. Find sales by city.
4. Find category-wise sales.
5. Create a pivot table.
6. Find average sales.
7. Find the highest-selling city.
8. Sort products by sales.

### Project 4: Cricket Statistics

Create a DataFrame with the following columns:

| Column | Description |
| --- | --- |
| `Player` | Player name |
| `Team` | Team name |
| `Runs` | Total runs |
| `Matches` | Matches played |
| `Average` | Batting average |

Perform the following tasks:

1. Find the highest run scorer.
2. Find players averaging above 50.
3. Find team-wise total runs.
4. Count players in each team.
5. Sort by runs.
6. Create a pivot table for team-wise average runs.

## Topics Covered

| Topic | Questions |
| --- | ---: |
| Series | 8 |
| DataFrame | 8 |
| Attributes | 6 |
| Selection (`loc`, `iloc`) | 8 |
| Missing Data | 6 |
| Sorting and Filtering | 5 |
| Operations | 6 |
| GroupBy and Aggregation | 5 |
| Merge, Join, and Concatenation | 4 |
| Pivot Table | 4 |
| Advanced | 10 |
| Real-world Projects | 4 |

## Interview Coverage

This practice sheet covers the core Pandas concepts commonly asked in interviews:

- Series and DataFrame
- DataFrame creation
- Indexing with `loc` and `iloc`
- Filtering and sorting
- Missing data handling
- Arithmetic and string operations
- GroupBy and aggregation
- Merge, join, and concatenation
- Pivot tables
- File handling with `read_csv()` and `to_csv()`
- Duplicate handling
- Data type conversion
- Real-world data analysis projects

Completing these 70 practice questions and 4 mini projects will give you a strong foundation in Pandas for data analysis, machine learning preprocessing, and technical interviews.
