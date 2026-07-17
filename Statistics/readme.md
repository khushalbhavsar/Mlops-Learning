# What is Statistics?

**Statistics** is the branch of mathematics that deals with the **collection, organization, analysis, interpretation, and presentation of data** to draw meaningful conclusions and support decision-making.

It helps transform **raw data into useful information**.

---

# Simple Definition

> **Statistics is the science of collecting, organizing, analyzing, interpreting, and presenting data to make informed decisions.**

---

# Why Do We Use Statistics?

Statistics helps us to:

* Collect and organize data.
* Summarize large datasets.
* Identify patterns and trends.
* Make predictions.
* Support decision-making.
* Solve real-world problems using data.

---

# Real-Life Example

Suppose a teacher wants to know the performance of a class.

### Raw Marks

```text
65, 72, 81, 75, 90, 68, 77, 84
```

Using statistics, the teacher can calculate:

* Average (Mean)
* Highest score
* Lowest score
* Median
* Standard Deviation

This helps the teacher understand the overall performance of the class.

---

# Statistics Process

```text
Collect Data
      ↓
Organize Data
      ↓
Present Data
      ↓
Analyze Data
      ↓
Interpret Results
      ↓
Make Decisions
```

---

# Types of Statistics

There are **two main types** of statistics.

| Type                       | Purpose                                                  |
| -------------------------- | -------------------------------------------------------- |
| **Descriptive Statistics** | Summarizes and describes the data                        |
| **Inferential Statistics** | Draws conclusions and makes predictions from sample data |

---

# 1. Descriptive Statistics

Descriptive statistics summarize and organize data.

It answers questions like:

* What is the average?
* What is the highest value?
* What is the lowest value?
* How is the data distributed?

### Common Measures

| Measure            | Purpose                                      |
| ------------------ | -------------------------------------------- |
| Mean               | Average                                      |
| Median             | Middle value                                 |
| Mode               | Most frequent value                          |
| Range              | Difference between highest and lowest values |
| Variance           | Spread of data                               |
| Standard Deviation | Average spread of data                       |

### Example

Dataset:

```text
10, 20, 30, 40, 50
```

Mean = **30**

Median = **30**

Range = **40**

---

# 2. Inferential Statistics

Inferential statistics use a **sample** to make conclusions about a **population**.

It answers questions like:

* Will customers buy a product?
* Who will win an election?
* Will a patient respond to a treatment?

### Example

A company surveys **500 customers** out of **100,000 customers**.

Using inferential statistics, the company predicts the preferences of all customers.

---

# Population vs Sample

| Population                         | Sample                         |
| ---------------------------------- | ------------------------------ |
| Entire group                       | Small part of the group        |
| Example: All students in a college | Example: 100 selected students |

---

# Important Statistical Terms

| Term        | Meaning                             |
| ----------- | ----------------------------------- |
| Data        | Collection of facts or observations |
| Population  | Entire group under study            |
| Sample      | Subset of the population            |
| Variable    | Characteristic being measured       |
| Observation | Single data value                   |

---

# Applications of Statistics

Statistics is used in:

* Business Analytics
* Healthcare
* Finance
* Marketing
* Education
* Government
* Sports
* Manufacturing
* Scientific Research

---

# Statistics in Data Science

Statistics is one of the **foundations of Data Science**.

```text
Collect Data
      ↓
Clean Data
      ↓
Statistics
      ↓
Exploratory Data Analysis (EDA)
      ↓
Machine Learning
      ↓
Prediction
```

Statistics is used for:

* Data Cleaning
* Data Visualization
* Feature Engineering
* Hypothesis Testing
* Probability
* Machine Learning

---

# Python Example

```python
import pandas as pd

data = [10,20,30,40,50]

df = pd.DataFrame({"Marks": data})

print("Mean:", df["Marks"].mean())
print("Median:", df["Marks"].median())
print("Standard Deviation:", df["Marks"].std())
```

---

# Advantages of Statistics

* Simplifies complex data.
* Helps make informed decisions.
* Identifies trends and patterns.
* Supports forecasting.
* Essential for research and data analysis.

---

# Limitations of Statistics

* Results depend on data quality.
* Incorrect interpretation can lead to wrong conclusions.
* Cannot replace expert judgment.
* Biased samples can produce misleading results.

---

# Interview Questions

| Question                                              | Answer                                                                                   |
| ----------------------------------------------------- | ---------------------------------------------------------------------------------------- |
| What is Statistics?                                   | The science of collecting, organizing, analyzing, interpreting, and presenting data.     |
| What are the two types of Statistics?                 | Descriptive Statistics and Inferential Statistics.                                       |
| What is the difference between Population and Sample? | Population is the entire group, while a Sample is a subset of that group.                |
| Why is Statistics important in Data Science?          | It helps understand data, identify patterns, and build accurate machine learning models. |
| Name three statistical measures.                      | Mean, Median, and Standard Deviation.                                                    |

---

# Quick Cheat Sheet

| Concept                | Description                    |
| ---------------------- | ------------------------------ |
| Statistics             | Science of analyzing data      |
| Descriptive Statistics | Summarizes data                |
| Inferential Statistics | Makes predictions from samples |
| Population             | Entire dataset                 |
| Sample                 | Part of the dataset            |
| Mean                   | Average                        |
| Median                 | Middle value                   |
| Mode                   | Most frequent value            |

---

# Key Points to Remember

* **Statistics** is the science of **collecting, organizing, analyzing, interpreting, and presenting data**.
* It helps convert **raw data into meaningful information**.
* There are **two main branches**:

  * **Descriptive Statistics** → Summarizes and describes data.
  * **Inferential Statistics** → Makes predictions and conclusions using sample data.
* Statistics is a fundamental part of **Data Science**, **Machine Learning**, **Business Analytics**, **Finance**, **Healthcare**, and **Scientific Research**.

### Easy Way to Remember

| Term                       | Remember As                   |
| -------------------------- | ----------------------------- |
| **Statistics**             | 📊 Study of data              |
| **Descriptive Statistics** | 📋 Describe the data          |
| **Inferential Statistics** | 🔮 Predict and make decisions |
| **Population**             | 🌍 Entire group               |
| **Sample**                 | 🧩 Small part of the group    |

# What is a One-Way Table?

A **One-Way Table** (also called a **Frequency Table**) is a table that shows the **frequency (count)** of each category or value of **one variable**.

It summarizes data by displaying **how many times each category appears** in a dataset.

---

# Simple Definition

> **A One-Way Table is a table that displays the frequency (count) of each category for a single variable.**

---

# Why Do We Use a One-Way Table?

A One-Way Table helps us to:

* Organize raw data.
* Count the frequency of each category.
* Summarize large datasets.
* Understand the distribution of one variable.
* Prepare data for graphs such as bar graphs and pie charts.

---

# Example 1: Student Departments

Suppose we have the following data:

| Student | Department |
| ------- | ---------- |
| Rahul   | IT         |
| Priya   | HR         |
| Amit    | IT         |
| Neha    | Sales      |
| Rohit   | IT         |
| Pooja   | HR         |
| Karan   | Sales      |
| Riya    | IT         |

### One-Way Table

| Department | Frequency |
| ---------- | --------: |
| IT         |         4 |
| HR         |         2 |
| Sales      |         2 |
| **Total**  |     **8** |

### Interpretation

* **IT** appears **4** times.
* **HR** appears **2** times.
* **Sales** appears **2** times.

This table summarizes the data using **one variable (Department)**.

---

# Example 2: Favorite Fruit

Raw Data:

```text
Apple, Banana, Apple, Mango, Apple,
Banana, Apple, Mango, Banana, Apple
```

### One-Way Table

| Fruit     | Frequency |
| --------- | --------: |
| Apple     |         5 |
| Banana    |         3 |
| Mango     |         2 |
| **Total** |    **10** |

This table shows how many people prefer each fruit.

---

# Components of a One-Way Table

| Component  | Description                              |
| ---------- | ---------------------------------------- |
| Variable   | The single characteristic being analyzed |
| Categories | Different values of the variable         |
| Frequency  | Number of times each category appears    |
| Total      | Total number of observations             |

---

# Characteristics of a One-Way Table

* Contains **only one variable**.
* Shows the **frequency** of each category.
* Easy to understand and interpret.
* Used for **categorical** or **discrete** data.
* Often used before creating a **Bar Graph** or **Pie Chart**.

---

# How to Create a One-Way Table

```text
Collect Data
      ↓
Identify One Variable
      ↓
Count Each Category
      ↓
Arrange Categories and Frequencies
      ↓
Create the One-Way Table
```

---

# One-Way Table vs Two-Way Table

| One-Way Table     | Two-Way Table                            |
| ----------------- | ---------------------------------------- |
| Uses one variable | Uses two variables                       |
| Shows frequency   | Shows relationship between two variables |
| Simple summary    | Comparative summary                      |

### One-Way Table

| Department | Frequency |
| ---------- | --------: |
| IT         |         4 |
| HR         |         2 |
| Sales      |         2 |

### Two-Way Table

| Department | Male | Female |
| ---------- | ---: | -----: |
| IT         |    3 |      1 |
| HR         |    0 |      2 |
| Sales      |    1 |      1 |

---

# Python Example (Pandas)

### Using `value_counts()`

```python
import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Sales", "IT", "HR", "Sales", "IT"]
})

print(df["Department"].value_counts())
```

### Output

```text
IT       4
HR       2
Sales    2
```

---

### Convert to a One-Way Table

```python
freq_table = df["Department"].value_counts().reset_index()
freq_table.columns = ["Department", "Frequency"]

print(freq_table)
```

---

# Applications

One-Way Tables are used in:

* Survey analysis
* Student performance analysis
* Customer segmentation
* Product sales analysis
* Market research
* Election results
* Exploratory Data Analysis (EDA)

---

# Advantages

* Easy to create and understand.
* Organizes raw data effectively.
* Summarizes large datasets.
* Helps identify the most and least frequent categories.
* Forms the basis for graphs and charts.

---

# Limitations

* Analyzes only one variable.
* Does not show relationships between variables.
* Less useful for complex datasets involving multiple variables.

---

# Interview Questions

| Question                                                | Answer                                         |
| ------------------------------------------------------- | ---------------------------------------------- |
| What is a One-Way Table?                                | A table showing the frequency of one variable. |
| What is another name for a One-Way Table?               | Frequency Table.                               |
| How many variables does a One-Way Table contain?        | One variable.                                  |
| Which Pandas function creates a One-Way Table?          | `value_counts()`                               |
| Which graphs are commonly created from a One-Way Table? | Bar Graph and Pie Chart.                       |

---

# Quick Cheat Sheet

| Task                 | Pandas Function                |
| -------------------- | ------------------------------ |
| Count frequencies    | `value_counts()`               |
| Get percentages      | `value_counts(normalize=True)` |
| Convert to DataFrame | `value_counts().reset_index()` |

---

# Key Points to Remember

* **One-Way Table = One Variable + Frequency (Count)**.
* It is also called a **Frequency Table**.
* It summarizes **one categorical or discrete variable**.
* Each row represents a **category**, and the frequency column shows **how many times that category appears**.
* It is commonly used before creating **Bar Graphs**, **Pie Charts**, and performing **Exploratory Data Analysis (EDA)**.

### Easy Way to Remember

| Table             | Meaning                                 |
| ----------------- | --------------------------------------- |
| **One-Way Table** | 📋 One Variable + Count                 |
| **Two-Way Table** | 📊 Two Variables + Relationship + Count |


# What is a Bar Graph?

A **Bar Graph** (also called a **Bar Chart**) is a graphical representation of **categorical data** using **rectangular bars** of equal width. The **height (or length)** of each bar represents the **frequency (count)** or **value** of a category.

It is one of the most commonly used graphs in **Statistics**, **Data Science**, **Machine Learning**, and **Business Analytics** because it makes comparisons between categories easy.

---

# Simple Definition

> **A Bar Graph is a graph that uses rectangular bars to compare the frequency or value of different categories.**

---

# Why Do We Use a Bar Graph?

A Bar Graph helps us to:

* Compare different categories.
* Display frequencies or values clearly.
* Identify the highest and lowest values.
* Summarize categorical data.
* Present data in an easy-to-understand visual form.

---

# How is a Bar Graph Created?

```text
Raw Data
    ↓
Count each category
    ↓
Create a Frequency Table
    ↓
Draw X-axis and Y-axis
    ↓
Draw Bars According to Frequency
    ↓
Bar Graph
```

---

# Example

Suppose a survey records students' favorite programming language.

### Step 1: Frequency Table

| Programming Language | Number of Students |
| -------------------- | -----------------: |
| Python               |                 50 |
| Java                 |                 30 |
| C++                  |                 25 |
| JavaScript           |                 40 |

### Step 2: Bar Graph

### Interpretation

* **Python** is the most popular language.
* **C++** is the least popular language.
* The graph makes comparison much easier than reading the table.

---

# Components of a Bar Graph

| Component     | Description                         |
| ------------- | ----------------------------------- |
| X-axis        | Displays the categories             |
| Y-axis        | Displays the frequency or value     |
| Bars          | Represent each category             |
| Height of Bar | Represents the frequency or value   |
| Title         | Describes what the graph represents |

---

# Characteristics of a Bar Graph

* Used for **categorical (qualitative)** data.
* Bars have **equal width**.
* There is **equal spacing** between bars.
* Height (or length) of each bar represents the value or frequency.
* Can be drawn vertically or horizontally.

---

# Types of Bar Graphs

## 1. Vertical Bar Graph

Bars are drawn vertically.

```text
Frequency
 ^
 |         █
 |         █
 |    █    █
 |    █    █
 | █  █    █
 +-------------------->
   A   B    C
```

---

## 2. Horizontal Bar Graph

Bars are drawn horizontally.

```text
A  █████
B  ████████
C  ██████████
```

---

## 3. Grouped Bar Graph

Used to compare two or more datasets for the same categories.

Example:

| Department | Boys | Girls |
| ---------- | ---: | ----: |
| IT         |   30 |    25 |
| CSE        |   35 |    40 |

---

## 4. Stacked Bar Graph

Shows the total value while dividing each bar into different parts.

Example:

```text
IT   ███▓▓
CSE  █████▓▓▓
```

---

# Bar Graph vs Histogram

| Bar Graph                     | Histogram                          |
| ----------------------------- | ---------------------------------- |
| Used for categorical data     | Used for continuous numerical data |
| Bars have spaces between them | Bars touch each other              |
| Compares categories           | Shows the distribution of data     |

---

# Python Example (Matplotlib)

```python
import matplotlib.pyplot as plt

languages = ["Python", "Java", "C++", "JavaScript"]
students = [50, 30, 25, 40]

plt.bar(languages, students)

plt.title("Favorite Programming Language")
plt.xlabel("Programming Language")
plt.ylabel("Number of Students")

plt.show()
```

---

# Python Example (Seaborn)

```python
import seaborn as sns
import matplotlib.pyplot as plt

languages = ["Python", "Java", "C++", "JavaScript"]
students = [50, 30, 25, 40]

sns.barplot(x=languages, y=students)

plt.title("Favorite Programming Language")
plt.show()
```

---

# Applications

Bar Graphs are used in:

* Student performance analysis
* Product sales comparison
* Customer surveys
* Population comparison
* Election results
* Business reports
* Exploratory Data Analysis (EDA)

---

# Advantages

* Easy to understand and interpret.
* Makes category comparison simple.
* Clearly shows the highest and lowest values.
* Suitable for reports and presentations.

---

# Limitations

* Not suitable for continuous numerical data.
* Difficult to read if there are too many categories.
* Does not show trends over time (use a Line Graph instead).

---

# Interview Questions

| Question                                           | Answer                                                          |
| -------------------------------------------------- | --------------------------------------------------------------- |
| What is a Bar Graph?                               | A graph that uses rectangular bars to compare categorical data. |
| Which type of data is represented by a Bar Graph?  | Categorical data.                                               |
| Which graph is used for continuous numerical data? | Histogram.                                                      |
| Which Matplotlib function creates a Bar Graph?     | `plt.bar()`                                                     |
| Which Seaborn function creates a Bar Graph?        | `sns.barplot()`                                                 |

---

# Quick Cheat Sheet

| Feature    | Description             |
| ---------- | ----------------------- |
| Purpose    | Compare categories      |
| Data Type  | Categorical             |
| Bars       | Equal width with spaces |
| X-axis     | Categories              |
| Y-axis     | Frequency or Value      |
| Matplotlib | `plt.bar()`             |
| Seaborn    | `sns.barplot()`         |

---

# Key Points to Remember

* A **Bar Graph** compares **categorical data** using rectangular bars.
* The **height (or length)** of each bar represents the **frequency or value**.
* Bars are **equal in width** and **separated by spaces**.
* Common types are:

  * Vertical Bar Graph
  * Horizontal Bar Graph
  * Grouped Bar Graph
  * Stacked Bar Graph
* It is widely used in **Statistics**, **Data Science**, **Business Analytics**, and **Machine Learning** for comparing categories.

### Easy Way to Remember

| Graph          | Remember As                             |
| -------------- | --------------------------------------- |
| **Bar Graph**  | 📊 Compare categories                   |
| **Histogram**  | 📶 Show distribution of continuous data |
| **Pie Chart**  | 🥧 Show percentages                     |
| **Line Graph** | 📈 Show trends over time                |

# What is a Pie Chart?

A **Pie Chart** is a circular graph that represents **parts of a whole**. It is divided into **slices (sectors)**, where each slice represents the **proportion or percentage** of a category relative to the total.

The **entire pie represents 100%** of the data.

---

# Simple Definition

> **A Pie Chart is a circular chart divided into slices, where each slice represents the percentage or proportion of a category out of the whole.**

---

# Why Do We Use a Pie Chart?

A Pie Chart helps us to:

* Show percentages or proportions.
* Compare the contribution of different categories.
* Visualize parts of a whole.
* Identify the largest and smallest categories.
* Present survey or categorical data clearly.

---

# How is a Pie Chart Created?

```text
Raw Data
    ↓
Count each category
    ↓
Create a Frequency Table
    ↓
Calculate Percentage of Each Category
    ↓
Draw Circular Sectors
    ↓
Pie Chart
```

---

# Example

Suppose a survey asks students about their favorite programming language.

### Step 1: Frequency Table

| Programming Language | Students |
| -------------------- | -------: |
| Python               |       50 |
| Java                 |       30 |
| C++                  |       10 |
| JavaScript           |       10 |
| **Total**            |  **100** |

### Step 2: Percentage Table

| Programming Language | Students | Percentage |
| -------------------- | -------: | ---------: |
| Python               |       50 |        50% |
| Java                 |       30 |        30% |
| C++                  |       10 |        10% |
| JavaScript           |       10 |        10% |

### Step 3: Pie Chart

### Interpretation

* **Python** occupies **50%** of the pie, making it the most preferred language.
* **Java** accounts for **30%**.
* **C++** and **JavaScript** each represent **10%**.

---

# Components of a Pie Chart

| Component      | Description                           |
| -------------- | ------------------------------------- |
| Circle         | Represents the whole dataset (100%)   |
| Slice (Sector) | Represents one category               |
| Percentage     | Shows the proportion of each category |
| Labels         | Identify each category                |
| Legend         | Explains the slices (optional)        |
| Title          | Describes the chart                   |

---

# Characteristics of a Pie Chart

* Circular in shape.
* Represents **parts of a whole**.
* Total of all slices equals **100%**.
* Each slice size is proportional to its value.
* Best suited for a **small number of categories**.

---

# Formula for Percentage

[
\text{Percentage} = \frac{\text{Category Frequency}}{\text{Total Frequency}} \times 100
]

### Example

If **Python = 50 students** and **Total = 100 students**,

[
\text{Percentage} = \frac{50}{100} \times 100 = 50%
]

---

# Pie Chart vs Bar Graph

| Pie Chart                         | Bar Graph                     |
| --------------------------------- | ----------------------------- |
| Shows percentage or proportion    | Shows frequency or value      |
| Circular graph                    | Rectangular bars              |
| Best for part-to-whole comparison | Best for comparing categories |
| Total always equals 100%          | No such restriction           |

---

# Creating a Pie Chart in Python

### Using Matplotlib

```python
import matplotlib.pyplot as plt

languages = ["Python", "Java", "C++", "JavaScript"]
students = [50, 30, 10, 10]

plt.pie(students,
        labels=languages,
        autopct="%1.1f%%")

plt.title("Favorite Programming Language")

plt.show()
```

---

### Using Plotly

```python
import plotly.express as px
import pandas as pd

df = pd.DataFrame({
    "Language": ["Python", "Java", "C++", "JavaScript"],
    "Students": [50, 30, 10, 10]
})

fig = px.pie(df,
             names="Language",
             values="Students")

fig.show()
```

---

# Applications

Pie Charts are commonly used in:

* Survey analysis
* Market share analysis
* Election results
* Budget allocation
* Customer segmentation
* Product sales distribution
* Business reports

---

# Advantages

* Easy to understand.
* Clearly shows percentages.
* Highlights the largest and smallest categories.
* Good for presentations and reports.

---

# Limitations

* Not suitable for many categories.
* Difficult to compare slices with similar sizes.
* Not suitable for showing trends over time.
* Less effective than bar graphs for precise comparisons.

---

# Interview Questions

| Question                                               | Answer                                                          |
| ------------------------------------------------------ | --------------------------------------------------------------- |
| What is a Pie Chart?                                   | A circular chart that represents parts of a whole using slices. |
| What does the whole pie represent?                     | 100% of the data.                                               |
| Which type of data is best represented by a Pie Chart? | Categorical data showing proportions or percentages.            |
| Which Matplotlib function creates a Pie Chart?         | `plt.pie()`                                                     |
| When should you use a Pie Chart?                       | To show the percentage contribution of categories to a whole.   |

---

# Quick Cheat Sheet

| Feature    | Description                     |
| ---------- | ------------------------------- |
| Purpose    | Show proportions or percentages |
| Data Type  | Categorical                     |
| Shape      | Circular                        |
| Total      | 100%                            |
| Best For   | Part-to-whole comparison        |
| Matplotlib | `plt.pie()`                     |
| Plotly     | `px.pie()`                      |

---

# Key Points to Remember

* A **Pie Chart** is a **circular graph** divided into slices.
* Each slice represents the **percentage or proportion** of a category.
* The **entire pie always represents 100%**.
* Pie Charts are best for **showing parts of a whole**.
* They work best when there are **few categories (typically 3–6)**.
* Common Python functions:

  * **Matplotlib:** `plt.pie()`
  * **Plotly:** `px.pie()`

---

# Easy Way to Remember

| Graph          | Remember As                              |
| -------------- | ---------------------------------------- |
| **Pie Chart**  | 🥧 Shows percentages of a whole          |
| **Bar Graph**  | 📊 Compares categories                   |
| **Line Graph** | 📈 Shows trends over time                |
| **Histogram**  | 📶 Shows distribution of continuous data |

# What is a Line Graph?

A **Line Graph** (also called a **Line Chart**) is a graph that displays data using **points connected by straight lines**. It is mainly used to show **changes or trends over time** or across an ordered sequence.

Each point represents a data value, and the connecting lines make it easy to observe increases, decreases, or patterns.

---

# Simple Definition

> **A Line Graph is a graph that connects data points with straight lines to show changes or trends over time.**

---

# Why Do We Use a Line Graph?

A Line Graph helps us to:

* Show trends over time.
* Compare changes in data.
* Identify increases and decreases.
* Predict future trends.
* Analyze continuous data.

---

# How is a Line Graph Created?

```text
Collect Data
      ↓
Arrange Data in Order
      ↓
Draw X-axis and Y-axis
      ↓
Plot Data Points
      ↓
Connect Points with Lines
      ↓
Line Graph
```

---

# Example

Suppose a company records monthly sales.

### Step 1: Data Table

| Month    | Sales |
| -------- | ----: |
| January  |   100 |
| February |   120 |
| March    |   140 |
| April    |   130 |
| May      |   160 |
| June     |   180 |

### Step 2: Line Graph

### Interpretation

* Sales increased from **January to March**.
* Sales decreased slightly in **April**.
* Sales increased again in **May** and **June**.
* The graph clearly shows the **overall upward trend**.

---

# Components of a Line Graph

| Component   | Description                            |
| ----------- | -------------------------------------- |
| X-axis      | Represents time or ordered categories  |
| Y-axis      | Represents numerical values            |
| Data Points | Individual observations                |
| Line        | Connects data points to show the trend |
| Title       | Describes the graph                    |

---

# Characteristics of a Line Graph

* Uses **points connected by straight lines**.
* Best for **continuous or time-series data**.
* Clearly shows increasing or decreasing trends.
* Easy to compare multiple datasets using multiple lines.

---

# Types of Line Graphs

## 1. Simple Line Graph

Shows the trend of **one dataset**.

Example:

```text
Sales
 ^
 |                 ●
 |              ●
 |           ●
 |      ●
 |   ●
 +------------------------>
   Jan Feb Mar Apr May
```

---

## 2. Multiple Line Graph

Compares **two or more datasets** on the same graph.

Example:

* Sales of Product A
* Sales of Product B

Both are shown using different lines.

---

# Line Graph vs Bar Graph

| Line Graph                   | Bar Graph                                 |
| ---------------------------- | ----------------------------------------- |
| Shows trends over time       | Compares categories                       |
| Uses connected points        | Uses rectangular bars                     |
| Best for continuous data     | Best for categorical data                 |
| Highlights changes over time | Highlights differences between categories |

---

# Creating a Line Graph in Python

### Using Matplotlib

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [100, 120, 140, 130, 160, 180]

plt.plot(months, sales, marker="o")

plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")

plt.show()
```

---

### Using Seaborn

```python
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [100, 120, 140, 130, 160, 180]
})

sns.lineplot(data=df, x="Month", y="Sales")

plt.title("Monthly Sales")
plt.show()
```

---

# Applications

Line Graphs are widely used in:

* Stock market analysis
* Weather forecasting
* Sales analysis
* Population growth
* Temperature changes
* Website traffic analysis
* Business reports
* Data Science and Machine Learning

---

# Advantages

* Clearly shows trends over time.
* Easy to identify increases and decreases.
* Useful for forecasting future values.
* Suitable for comparing multiple datasets.

---

# Limitations

* Not suitable for categorical comparisons.
* Can become cluttered with too many lines.
* Less effective when data points are unordered.

---

# Interview Questions

| Question                                                | Answer                                                                          |
| ------------------------------------------------------- | ------------------------------------------------------------------------------- |
| What is a Line Graph?                                   | A graph that connects data points with straight lines to show trends over time. |
| Which type of data is best represented by a Line Graph? | Continuous or time-series data.                                                 |
| Which Matplotlib function creates a Line Graph?         | `plt.plot()`                                                                    |
| Which Seaborn function creates a Line Graph?            | `sns.lineplot()`                                                                |
| When should you use a Line Graph?                       | To show trends or changes over time.                                            |

---

# Quick Cheat Sheet

| Feature    | Description                |
| ---------- | -------------------------- |
| Purpose    | Show trends over time      |
| Data Type  | Continuous or time-series  |
| Shape      | Connected data points      |
| X-axis     | Time or ordered categories |
| Y-axis     | Numerical values           |
| Matplotlib | `plt.plot()`               |
| Seaborn    | `sns.lineplot()`           |

---

# Key Points to Remember

* A **Line Graph** uses **points connected by straight lines**.
* It is mainly used to **show trends or changes over time**.
* The **X-axis** usually represents **time or an ordered sequence**.
* The **Y-axis** represents **numerical values**.
* It is ideal for analyzing **continuous data** and **time-series data**.
* Common Python functions:

  * **Matplotlib:** `plt.plot()`
  * **Seaborn:** `sns.lineplot()`

---

# Easy Way to Remember

| Graph          | Remember As                                  |
| -------------- | -------------------------------------------- |
| **Line Graph** | 📈 Shows trends and changes over time        |
| **Bar Graph**  | 📊 Compares categories                       |
| **Pie Chart**  | 🥧 Shows percentage of a whole               |
| **Histogram**  | 📶 Shows the distribution of continuous data |

# What is an Ogive?

An **Ogive** (pronounced **"Oh-jive"**) is a graph that represents the **cumulative frequency** of a dataset. It is also known as a **Cumulative Frequency Curve**.

Instead of showing the frequency of each class, an ogive shows the **running total (cumulative frequency)** of observations.

---

# Simple Definition

> **An Ogive is a graph of cumulative frequencies that shows the running total of observations up to each class interval.**

---

# Why Do We Use an Ogive?

An Ogive helps us to:

* Find the cumulative frequency.
* Determine the **Median**.
* Find **Quartiles (Q1, Q2, Q3)**.
* Find **Percentiles**.
* Compare two cumulative frequency distributions.
* Understand how data accumulates over class intervals.

---

# Types of Ogives

There are **two types** of Ogives.

| Type                | Description                                                                |
| ------------------- | -------------------------------------------------------------------------- |
| **Less Than Ogive** | Shows cumulative frequency less than or equal to the upper class limit.    |
| **More Than Ogive** | Shows cumulative frequency greater than or equal to the lower class limit. |

---

# Example Data

Suppose the marks of 40 students are grouped as follows:

| Marks     | Frequency |
| --------- | --------: |
| 0–10      |         3 |
| 10–20     |         5 |
| 20–30     |         8 |
| 30–40     |        10 |
| 40–50     |         7 |
| 50–60     |         5 |
| 60–70     |         2 |
| **Total** |    **40** |

---

# 1. Less Than Ogive

## Step 1: Calculate Cumulative Frequency

| Marks (Less Than) | Frequency | Cumulative Frequency |
| ----------------: | --------: | -------------------: |
|               <10 |         3 |                    3 |
|               <20 |         5 |                    8 |
|               <30 |         8 |                   16 |
|               <40 |        10 |                   26 |
|               <50 |         7 |                   33 |
|               <60 |         5 |                   38 |
|               <70 |         2 |                   40 |

### Interpretation

* Less than 10 marks → **3 students**
* Less than 20 marks → **8 students**
* Less than 30 marks → **16 students**
* Less than 70 marks → **40 students**

---

# 2. More Than Ogive

## Step 1: Calculate Cumulative Frequency

| Marks (More Than) | Cumulative Frequency |
| ----------------: | -------------------: |
|                >0 |                   40 |
|               >10 |                   37 |
|               >20 |                   32 |
|               >30 |                   24 |
|               >40 |                   14 |
|               >50 |                    7 |
|               >60 |                    2 |

### Interpretation

* More than 30 marks → **24 students**
* More than 50 marks → **7 students**

---

# How to Draw an Ogive

```text
Create Frequency Distribution
            ↓
Calculate Cumulative Frequency
            ↓
Draw X-axis (Class Boundaries)
            ↓
Draw Y-axis (Cumulative Frequency)
            ↓
Plot the Points
            ↓
Join the Points with a Smooth Curve
            ↓
Ogive
```

---

# Shape of an Ogive

### Less Than Ogive

```text
Cumulative Frequency
 ^
 |                           ●
 |                      ●
 |                 ●
 |            ●
 |       ●
 |   ●
 +---------------------------------->
    10 20 30 40 50 60 70
          Marks
```

The curve **increases continuously** because cumulative frequency always increases.

---

### More Than Ogive

```text
Cumulative Frequency
 ^
 |●
 |   ●
 |      ●
 |          ●
 |              ●
 |                  ●
 +---------------------------------->
   0 10 20 30 40 50 60
        Marks
```

The curve **decreases continuously** because cumulative frequency becomes smaller.

---

# Uses of an Ogive

Ogives are used to find:

* Median
* Quartiles (Q1, Q2, Q3)
* Percentiles
* Deciles
* Cumulative frequencies
* Comparison of cumulative distributions

---

# Less Than Ogive vs More Than Ogive

| Less Than Ogive                | More Than Ogive                 |
| ------------------------------ | ------------------------------- |
| Uses upper class limits        | Uses lower class limits         |
| Increasing curve               | Decreasing curve                |
| Starts from the smallest value | Starts from the total frequency |
| Ends at the total frequency    | Ends near zero                  |

---

# Ogive vs Histogram

| Ogive                             | Histogram                               |
| --------------------------------- | --------------------------------------- |
| Shows cumulative frequency        | Shows frequency                         |
| Smooth curve                      | Rectangular bars                        |
| Used to find median and quartiles | Used to show data distribution          |
| Displays running totals           | Displays frequencies of class intervals |

---

# Creating an Ogive in Python

```python
import matplotlib.pyplot as plt

marks = [10, 20, 30, 40, 50, 60, 70]
cum_freq = [3, 8, 16, 26, 33, 38, 40]

plt.plot(marks, cum_freq, marker="o")

plt.title("Less Than Ogive")
plt.xlabel("Marks")
plt.ylabel("Cumulative Frequency")

plt.grid(True)
plt.show()
```

---

# Applications

Ogives are widely used in:

* Statistics
* Education
* Business Analytics
* Quality Control
* Survey Analysis
* Medical Research
* Data Science

---

# Advantages

* Shows cumulative distribution clearly.
* Helps determine median and quartiles graphically.
* Useful for comparing datasets.
* Easy to identify cumulative trends.

---

# Limitations

* Does not show the frequency of each class directly.
* Less effective for comparing many datasets on one graph.
* Requires cumulative frequency calculations before plotting.

---

# Interview Questions

| Question                            | Answer                                                                       |
| ----------------------------------- | ---------------------------------------------------------------------------- |
| What is an Ogive?                   | A graph of cumulative frequencies, also called a cumulative frequency curve. |
| How many types of Ogives are there? | Two: Less Than Ogive and More Than Ogive.                                    |
| What is a Less Than Ogive?          | A graph showing cumulative frequencies up to the upper class limits.         |
| What is a More Than Ogive?          | A graph showing cumulative frequencies from the lower class limits downward. |
| What can we find using an Ogive?    | Median, Quartiles, Percentiles, and cumulative frequencies.                  |

---

# Quick Cheat Sheet

| Feature    | Description                      |
| ---------- | -------------------------------- |
| Purpose    | Show cumulative frequency        |
| Graph Type | Line (smooth curve)              |
| X-axis     | Class boundaries or class limits |
| Y-axis     | Cumulative frequency             |
| Types      | Less Than Ogive, More Than Ogive |
| Used For   | Median, Quartiles, Percentiles   |

---

# Key Points to Remember

* **Ogive** is a **Cumulative Frequency Curve**.
* It shows the **running total (cumulative frequency)** rather than individual frequencies.
* There are **two types**:

  * **Less Than Ogive** → Increasing curve.
  * **More Than Ogive** → Decreasing curve.
* Ogives are commonly used to determine:

  * **Median**
  * **Quartiles (Q1, Q2, Q3)**
  * **Percentiles**
  * **Deciles**
* An Ogive is created by plotting **cumulative frequencies** and joining the points with a smooth line.

---

# Easy Way to Remember

| Graph          | Remember As                   |
| -------------- | ----------------------------- |
| **Ogive**      | 📈 Cumulative Frequency Curve |
| **Histogram**  | 📊 Frequency Distribution     |
| **Bar Graph**  | 📋 Compare Categories         |
| **Line Graph** | 📈 Show Trends Over Time      |

# What is a Two-Way Table?

A **Two-Way Table** (also called a **Contingency Table** or **Cross Tabulation**) is a table that shows the **relationship between two categorical variables**. It displays the **frequency (count)** of observations for every combination of the two variables.

It helps compare how one variable is distributed across the categories of another variable.

---

# Simple Definition

> **A Two-Way Table is a table that displays the frequency of observations based on two categorical variables.**

---

# Why Do We Use a Two-Way Table?

A Two-Way Table helps us to:

* Compare two categorical variables.
* Study the relationship between variables.
* Calculate row totals and column totals.
* Analyze survey data.
* Perform statistical analysis.
* Prepare data for probability and hypothesis testing.

---

# How is a Two-Way Table Created?

```text
Collect Data
      ↓
Choose Two Variables
      ↓
Count Each Combination
      ↓
Arrange Counts in Rows and Columns
      ↓
Calculate Row & Column Totals
      ↓
Two-Way Table
```

---

# Example

Suppose a survey records the **Gender** and **Preferred Programming Language** of students.

### Raw Data

| Student | Gender | Language |
| ------- | ------ | -------- |
| A       | Male   | Python   |
| B       | Female | Java     |
| C       | Male   | Python   |
| D       | Female | Python   |
| E       | Male   | Java     |
| F       | Female | Java     |
| G       | Male   | Python   |
| H       | Female | Python   |

---

# Two-Way Table

| Gender    | Python |  Java | Total |
| --------- | -----: | ----: | ----: |
| Male      |      3 |     1 |     4 |
| Female    |      2 |     2 |     4 |
| **Total** |  **5** | **3** | **8** |

---

# Interpretation

* Total **Male students** = **4**
* Total **Female students** = **4**
* Total students who prefer **Python** = **5**
* Total students who prefer **Java** = **3**
* Most **Male students** prefer **Python**.
* Female students are equally divided between **Python** and **Java**.

---

# Components of a Two-Way Table

| Component       | Description                                |
| --------------- | ------------------------------------------ |
| Row Variable    | First categorical variable                 |
| Column Variable | Second categorical variable                |
| Cell Frequency  | Number of observations in each combination |
| Row Total       | Sum of each row                            |
| Column Total    | Sum of each column                         |
| Grand Total     | Total number of observations               |

---

# Characteristics of a Two-Way Table

* Contains **two categorical variables**.
* Displays frequencies for each combination.
* Includes row totals and column totals.
* Helps compare categories.
* Easy to interpret relationships.

---

# Example 2: Department and Gender

| Department |   Male | Female |   Total |
| ---------- | -----: | -----: | ------: |
| IT         |     30 |     20 |      50 |
| CSE        |     25 |     35 |      60 |
| ECE        |     20 |     15 |      35 |
| **Total**  | **75** | **70** | **145** |

### Interpretation

* IT has **50** students.
* CSE has the highest number of students (**60**).
* Total male students = **75**.
* Total female students = **70**.

---

# One-Way Table vs Two-Way Table

| One-Way Table                   | Two-Way Table                            |
| ------------------------------- | ---------------------------------------- |
| Uses one variable               | Uses two variables                       |
| Shows frequency of one variable | Shows relationship between two variables |
| Simple frequency table          | Cross-tabulation table                   |
| No row or column totals         | Includes row totals and column totals    |

---

# Creating a Two-Way Table in Pandas

### Using `pd.crosstab()`

```python
import pandas as pd

df = pd.DataFrame({
    "Gender": ["Male","Female","Male","Female","Male","Female","Male","Female"],
    "Language": ["Python","Java","Python","Python","Java","Java","Python","Python"]
})

table = pd.crosstab(df["Gender"], df["Language"])

print(table)
```

### Output

```text
Language  Java  Python
Gender
Female      2      2
Male        1      3
```

---

### Add Row and Column Totals

```python
pd.crosstab(df["Gender"], df["Language"], margins=True)
```

### Output

```text
Language  Java  Python  All
Gender
Female      2      2      4
Male        1      3      4
All         3      5      8
```

---

# Applications

Two-Way Tables are used in:

* Survey analysis
* Market research
* Customer segmentation
* Educational statistics
* Medical research
* Election analysis
* Exploratory Data Analysis (EDA)

---

# Advantages

* Shows the relationship between two variables.
* Easy to compare categories.
* Includes row and column totals.
* Useful for probability and statistical tests.
* Helps summarize large datasets.

---

# Limitations

* Limited to two variables.
* Large tables can become difficult to interpret.
* Does not measure the strength of the relationship (additional statistical tests are needed).

---

# Interview Questions

| Question                                         | Answer                                                                       |
| ------------------------------------------------ | ---------------------------------------------------------------------------- |
| What is a Two-Way Table?                         | A table showing the frequency of observations for two categorical variables. |
| What is another name for a Two-Way Table?        | Contingency Table or Cross Tabulation.                                       |
| How many variables does a Two-Way Table contain? | Two variables.                                                               |
| Which Pandas function creates a Two-Way Table?   | `pd.crosstab()`                                                              |
| What is the purpose of row and column totals?    | To summarize the total frequencies for each category.                        |

---

# Quick Cheat Sheet

| Task                     | Pandas Function  |
| ------------------------ | ---------------- |
| Create Two-Way Table     | `pd.crosstab()`  |
| Add Row & Column Totals  | `margins=True`   |
| Normalize to Percentages | `normalize=True` |

---

# Key Points to Remember

* **Two-Way Table = Two Variables + Frequency**.
* It is also called a **Contingency Table** or **Cross Tabulation**.
* Used to study the **relationship between two categorical variables**.
* Each cell shows the **frequency** for a combination of categories.
* Includes **row totals**, **column totals**, and a **grand total**.
* Common Pandas function:

  * `pd.crosstab()`

---

# Easy Way to Remember

| Table                | Remember As                                 |
| -------------------- | ------------------------------------------- |
| **One-Way Table**    | 📋 One Variable + Frequency                 |
| **Two-Way Table**    | 📊 Two Variables + Relationship + Frequency |
| **Cross Tabulation** | 🔄 Compare two categorical variables        |

# What is a Relative Frequency Table?

A **Relative Frequency Table** is a table that shows the **proportion or percentage** of observations in each category instead of just the frequency (count).

It tells us **how much of the total data each category represents**.

---

# Simple Definition

> **A Relative Frequency Table is a table that shows the proportion or percentage of each category relative to the total number of observations.**

---

# Why Do We Use a Relative Frequency Table?

A Relative Frequency Table helps us to:

* Compare categories using percentages.
* Understand the proportion of each category.
* Analyze data regardless of sample size.
* Prepare data for Pie Charts and Probability.
* Compare different datasets easily.

---

# Formula

### Relative Frequency

[
\boxed{\text{Relative Frequency}=\frac{\text{Frequency}}{\text{Total Frequency}}}
]

### Percentage

[
\boxed{\text{Percentage}=\frac{\text{Frequency}}{\text{Total Frequency}}\times100}
]

---

# How is a Relative Frequency Table Created?

```text
Collect Data
      ↓
Create Frequency Table
      ↓
Find Total Frequency
      ↓
Divide Each Frequency by Total
      ↓
(Optional) Multiply by 100
      ↓
Relative Frequency Table
```

---

# Example

Suppose a survey asks students about their favorite programming language.

### Step 1: Frequency Table

| Language   | Frequency |
| ---------- | --------: |
| Python     |        50 |
| Java       |        30 |
| C++        |        15 |
| JavaScript |         5 |
| **Total**  |   **100** |

---

### Step 2: Calculate Relative Frequency

[
\text{Python}=\frac{50}{100}=0.50
]

[
\text{Java}=\frac{30}{100}=0.30
]

[
\text{C++}=\frac{15}{100}=0.15
]

[
\text{JavaScript}=\frac{5}{100}=0.05
]

---

### Relative Frequency Table

| Language   | Frequency | Relative Frequency | Percentage |
| ---------- | --------: | -----------------: | ---------: |
| Python     |        50 |               0.50 |        50% |
| Java       |        30 |               0.30 |        30% |
| C++        |        15 |               0.15 |        15% |
| JavaScript |         5 |               0.05 |         5% |
| **Total**  |   **100** |           **1.00** |   **100%** |

---

# Interpretation

* **50%** of students prefer **Python**.
* **30%** prefer **Java**.
* **15%** prefer **C++**.
* **5%** prefer **JavaScript**.

The sum of all **relative frequencies = 1.00**.

The sum of all **percentages = 100%**.

---

# Components of a Relative Frequency Table

| Component          | Description                |
| ------------------ | -------------------------- |
| Category           | Different groups or values |
| Frequency          | Number of observations     |
| Relative Frequency | Proportion of the total    |
| Percentage         | Relative frequency × 100   |
| Total              | Total observations         |

---

# Characteristics of a Relative Frequency Table

* Based on a **Frequency Table**.
* Shows **proportions instead of counts**.
* Relative frequencies always sum to **1.00**.
* Percentages always sum to **100%**.
* Useful for comparing datasets of different sizes.

---

# Frequency Table vs Relative Frequency Table

| Frequency Table                | Relative Frequency Table         |
| ------------------------------ | -------------------------------- |
| Shows counts                   | Shows proportions or percentages |
| Total = Number of observations | Total = 1.00 or 100%             |
| Used to count data             | Used to compare data             |

### Example

| Fruit  | Frequency | Relative Frequency |
| ------ | --------: | -----------------: |
| Apple  |        20 |               0.40 |
| Banana |        15 |               0.30 |
| Mango  |        10 |               0.20 |
| Orange |         5 |               0.10 |

---

# Creating a Relative Frequency Table in Pandas

### Using `value_counts(normalize=True)`

```python
import pandas as pd

df = pd.DataFrame({
    "Language": [
        "Python","Java","Python","C++",
        "Python","Java","Python","Java"
    ]
})

print(df["Language"].value_counts(normalize=True))
```

### Output

```text
Python    0.50
Java      0.375
C++       0.125
```

---

### Convert to Percentage

```python
(df["Language"].value_counts(normalize=True) * 100).round(2)
```

### Output

```text
Python    50.00
Java      37.50
C++       12.50
```

---

# Applications

Relative Frequency Tables are used in:

* Statistics
* Probability
* Survey analysis
* Market research
* Business analytics
* Data Science
* Machine Learning
* Exploratory Data Analysis (EDA)

---

# Advantages

* Easy to compare categories.
* Independent of sample size.
* Shows percentages clearly.
* Useful for Pie Charts and Probability.
* Helps compare multiple datasets.

---

# Limitations

* Does not show the actual number of observations.
* May hide small differences in counts.
* Requires the total frequency to calculate proportions.

---

# Interview Questions

| Question                                               | Answer                                                                               |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| What is a Relative Frequency Table?                    | A table showing the proportion or percentage of each category relative to the total. |
| How is relative frequency calculated?                  | Frequency ÷ Total Frequency.                                                         |
| What is the sum of all relative frequencies?           | 1.00                                                                                 |
| What is the sum of all percentages?                    | 100%                                                                                 |
| Which Pandas function calculates relative frequencies? | `value_counts(normalize=True)`                                                       |

---

# Quick Cheat Sheet

| Task                 | Formula / Function                   |
| -------------------- | ------------------------------------ |
| Relative Frequency   | `Frequency ÷ Total`                  |
| Percentage           | `(Frequency ÷ Total) × 100`          |
| Pandas               | `value_counts(normalize=True)`       |
| Percentage in Pandas | `value_counts(normalize=True) * 100` |

---

# Key Points to Remember

* A **Relative Frequency Table** shows the **proportion or percentage** of each category.
* It is created by dividing each **frequency by the total number of observations**.
* The **sum of all relative frequencies = 1.00**.
* The **sum of all percentages = 100%**.
* It is widely used in **Statistics**, **Probability**, **Data Science**, **Machine Learning**, and **Business Analytics**.

---

# Easy Way to Remember

| Table                        | Remember As                                                |
| ---------------------------- | ---------------------------------------------------------- |
| **Frequency Table**          | 📋 Shows the **count** of each category                    |
| **Relative Frequency Table** | 📊 Shows the **proportion or percentage** of each category |
| **Percentage**               | 💯 Relative Frequency × 100                                |


# What is Joint Distribution?

A **Joint Distribution** is a statistical table or distribution that shows the **probability or frequency of two variables occurring together**.

It helps us understand the **relationship between two variables** by showing how often each combination of values occurs.

---

# Simple Definition

> **Joint Distribution is the distribution of two variables together, showing the frequency or probability of every possible combination of their values.**

---

# Why Do We Use Joint Distribution?

Joint Distribution helps us to:

* Study the relationship between two variables.
* Calculate joint probabilities.
* Compare two categorical variables.
* Analyze survey data.
* Find conditional and marginal probabilities.
* Perform statistical analysis.

---

# Example

Suppose a survey records the **Gender** and **Preferred Programming Language** of 100 students.

### Joint Distribution Table

| Gender    | Python |   Java |    C++ |   Total |
| --------- | -----: | -----: | -----: | ------: |
| Male      |     30 |     15 |      5 |      50 |
| Female    |     20 |     20 |     10 |      50 |
| **Total** | **50** | **35** | **15** | **100** |

---

# Interpretation

* **30 Male students** prefer **Python**.
* **20 Female students** prefer **Python**.
* **15 Male students** prefer **Java**.
* Total students = **100**.

Each cell represents the **joint frequency** of two variables.

Example:

* (Male, Python) = **30**
* (Female, Java) = **20**

---

# Joint Probability Distribution

To convert the frequency table into a **Joint Probability Distribution**, divide each frequency by the total number of observations.

### Formula

[
\boxed{\text{Joint Probability}=\frac{\text{Joint Frequency}}{\text{Total Observations}}}
]

---

### Example

For **Male and Python**:

[
P(\text{Male and Python})=\frac{30}{100}=0.30
]

For **Female and Java**:

[
P(\text{Female and Java})=\frac{20}{100}=0.20
]

---

# Joint Probability Table

| Gender    |   Python |     Java |      C++ |    Total |
| --------- | -------: | -------: | -------: | -------: |
| Male      |     0.30 |     0.15 |     0.05 |     0.50 |
| Female    |     0.20 |     0.20 |     0.10 |     0.50 |
| **Total** | **0.50** | **0.35** | **0.15** | **1.00** |

---

# Components of a Joint Distribution

| Component         | Description                      |
| ----------------- | -------------------------------- |
| Variable 1        | First variable (e.g., Gender)    |
| Variable 2        | Second variable (e.g., Language) |
| Joint Frequency   | Count of each combination        |
| Joint Probability | Probability of each combination  |
| Marginal Totals   | Row and column totals            |

---

# Characteristics of Joint Distribution

* Involves **two variables**.
* Shows every possible combination of values.
* Can be represented using **frequencies** or **probabilities**.
* The sum of all joint probabilities is **1**.
* Used to analyze relationships between variables.

---

# Joint Distribution vs Relative Frequency Table

| Joint Distribution              | Relative Frequency Table         |
| ------------------------------- | -------------------------------- |
| Uses two variables              | Usually uses one variable        |
| Shows combinations of variables | Shows proportion of one variable |
| Used for joint probability      | Used for relative frequency      |

---

# Joint Distribution vs Two-Way Table

| Two-Way Table       | Joint Distribution                 |
| ------------------- | ---------------------------------- |
| Shows frequencies   | Shows frequencies or probabilities |
| Count-based         | Count or probability based         |
| Used for comparison | Used for probability analysis      |

---

# Creating a Joint Distribution in Pandas

### Joint Frequency Table

```python
import pandas as pd

df = pd.DataFrame({
    "Gender": ["Male","Female","Male","Female",
               "Male","Female","Male","Female"],
    "Language": ["Python","Java","Python","Python",
                 "Java","Java","Python","C++"]
})

joint_freq = pd.crosstab(df["Gender"], df["Language"])

print(joint_freq)
```

### Output

```text
Language  C++  Java  Python
Gender
Female      1     2       1
Male        0     1       3
```

---

### Joint Probability Table

```python
joint_prob = pd.crosstab(
    df["Gender"],
    df["Language"],
    normalize=True
)

print(joint_prob)
```

### Output

```text
Language    C++   Java  Python
Gender
Female    0.125  0.25   0.125
Male      0.000  0.125  0.375
```

---

# Applications

Joint Distribution is used in:

* Statistics
* Probability
* Survey analysis
* Market research
* Medical research
* Data Science
* Machine Learning
* Risk analysis

---

# Advantages

* Shows the relationship between two variables.
* Helps calculate joint probabilities.
* Useful for probability and statistical analysis.
* Easy to compare combinations of categories.

---

# Limitations

* Limited to two variables (for simple joint distributions).
* Large datasets can produce large tables.
* Interpretation becomes difficult with many categories.

---

# Interview Questions

| Question                                               | Answer                                                                                     |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| What is Joint Distribution?                            | The distribution showing the frequency or probability of two variables occurring together. |
| How is joint probability calculated?                   | Joint Frequency ÷ Total Observations.                                                      |
| What is the sum of all joint probabilities?            | 1.00                                                                                       |
| Which Pandas function creates a joint frequency table? | `pd.crosstab()`                                                                            |
| Which parameter creates a joint probability table?     | `normalize=True`                                                                           |

---

# Quick Cheat Sheet

| Concept                     | Description                            |
| --------------------------- | -------------------------------------- |
| Joint Distribution          | Distribution of two variables together |
| Joint Frequency             | Count of each combination              |
| Joint Probability           | Joint Frequency ÷ Total                |
| Total Probability           | 1.00                                   |
| Pandas Function             | `pd.crosstab()`                        |
| Joint Probability in Pandas | `pd.crosstab(..., normalize=True)`     |

---

# Key Points to Remember

* **Joint Distribution** shows the **frequency or probability of two variables occurring together**.
* It helps analyze the **relationship between two variables**.
* Each cell represents a **joint frequency** or **joint probability**.
* **Joint Probability = Joint Frequency ÷ Total Observations**.
* The **sum of all joint probabilities is always 1**.
* Commonly created in Pandas using:

  * `pd.crosstab()` for frequencies.
  * `pd.crosstab(..., normalize=True)` for probabilities.

---

# Easy Way to Remember

| Term                   | Remember As                                     |
| ---------------------- | ----------------------------------------------- |
| **Joint Distribution** | 📊 Two Variables Together                       |
| **Joint Frequency**    | 🔢 Count of each combination                    |
| **Joint Probability**  | 🎯 Probability of two events occurring together |
| **Two-Way Table**      | 📋 Frequency table for two variables            |


# What is a Histogram?

A **Histogram** is a graphical representation of the **frequency distribution of continuous numerical data**. It uses **adjacent rectangular bars** (with **no gaps between them**) to show how many data values fall within different intervals called **class intervals** or **bins**.

It helps us understand the **distribution, shape, spread, and pattern** of numerical data.

---

# Simple Definition

> **A Histogram is a graph that shows the frequency distribution of continuous numerical data using adjacent bars.**

---

# Why Do We Use a Histogram?

A Histogram helps us to:

* Understand the distribution of data.
* Identify the shape of the data.
* Detect outliers.
* Find the range of data.
* Observe skewness.
* Compare different datasets.

---

# How is a Histogram Created?

```text
Collect Numerical Data
        ↓
Divide Data into Class Intervals (Bins)
        ↓
Count Frequency in Each Interval
        ↓
Draw X-axis (Class Intervals)
        ↓
Draw Y-axis (Frequency)
        ↓
Draw Adjacent Bars (No Gaps)
        ↓
Histogram
```

---

# Example

Suppose the marks of 30 students are grouped into class intervals.

### Frequency Distribution Table

| Marks | Frequency |
| ----- | --------: |
| 0–10  |         2 |
| 10–20 |         4 |
| 20–30 |         6 |
| 30–40 |         8 |
| 40–50 |         5 |
| 50–60 |         3 |
| 60–70 |         2 |

---

### Histogram

```text
Frequency
 8 |            █
 7 |            █
 6 |         █  █
 5 |         █  █  █
 4 |      █  █  █  █
 3 |      █  █  █  █  █
 2 |   █  █  █  █  █  █  █
 1 |   █  █  █  █  █  █  █
   +----------------------------------->
     0-10 10-20 20-30 30-40 40-50 50-60 60-70
             Marks (Class Intervals)
```

### Interpretation

* The highest frequency is in the **30–40** interval.
* Most students scored between **20 and 50**.
* Very few students scored below **10** or above **60**.

---

# Components of a Histogram

| Component  | Description                 |
| ---------- | --------------------------- |
| X-axis     | Class intervals (Bins)      |
| Y-axis     | Frequency                   |
| Bars       | Represent frequencies       |
| Bar Height | Indicates frequency         |
| Bins       | Intervals of numerical data |

---

# Characteristics of a Histogram

* Used for **continuous numerical data**.
* Bars **touch each other** (no gaps).
* Displays the frequency distribution.
* Width of each bar represents the class interval.
* Height represents the frequency.

---

# Histogram vs Bar Graph

| Histogram                          | Bar Graph                     |
| ---------------------------------- | ----------------------------- |
| Used for continuous numerical data | Used for categorical data     |
| Bars touch each other              | Bars have spaces between them |
| X-axis shows class intervals       | X-axis shows categories       |
| Shows data distribution            | Compares categories           |

---

# Shape of a Histogram

## 1. Symmetric Distribution (Normal Distribution)

```text
      █
    ████
  ███████
██████████
  ███████
    ████
      █
```

* Left and right sides are nearly equal.
* Mean ≈ Median ≈ Mode.

---

## 2. Right-Skewed Distribution

```text
████████
██████
████
██
█
```

* Long tail on the **right**.
* Most values are small.

---

## 3. Left-Skewed Distribution

```text
      █
     ██
   ████
 ██████
████████
```

* Long tail on the **left**.
* Most values are large.

---

## 4. Uniform Distribution

```text
████
████
████
████
████
```

* Frequencies are approximately equal.

---

# Creating a Histogram in Python

### Using Matplotlib

```python
import matplotlib.pyplot as plt

marks = [45,50,55,60,65,70,75,80,85,90,
         50,55,60,65,70,75,80,85,90,95]

plt.hist(marks, bins=5)

plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()
```

---

### Using Seaborn

```python
import seaborn as sns
import matplotlib.pyplot as plt

marks = [45,50,55,60,65,70,75,80,85,90,
         50,55,60,65,70,75,80,85,90,95]

sns.histplot(marks, bins=5)

plt.title("Histogram of Marks")
plt.show()
```

---

### Histogram with Density Curve

```python
sns.histplot(marks, bins=5, kde=True)
```

This displays both the **Histogram** and the **Density Curve**.

---

# Applications

Histograms are widely used in:

* Statistics
* Data Science
* Machine Learning
* Quality Control
* Business Analytics
* Medical Research
* Finance
* Manufacturing

---

# Advantages

* Easy to understand data distribution.
* Helps detect outliers.
* Shows skewness and spread.
* Useful for identifying patterns.
* Supports Exploratory Data Analysis (EDA).

---

# Limitations

* Not suitable for categorical data.
* Different bin sizes may change the appearance.
* Exact values cannot be determined from the graph.

---

# Interview Questions

| Question                                       | Answer                                                                   |
| ---------------------------------------------- | ------------------------------------------------------------------------ |
| What is a Histogram?                           | A graph showing the frequency distribution of continuous numerical data. |
| Which type of data is used in a Histogram?     | Continuous numerical data.                                               |
| Why do Histogram bars touch each other?        | Because the class intervals are continuous.                              |
| Which Matplotlib function creates a Histogram? | `plt.hist()`                                                             |
| Which Seaborn function creates a Histogram?    | `sns.histplot()`                                                         |

---

# Quick Cheat Sheet

| Feature    | Description                 |
| ---------- | --------------------------- |
| Purpose    | Show frequency distribution |
| Data Type  | Continuous numerical data   |
| X-axis     | Class intervals (Bins)      |
| Y-axis     | Frequency                   |
| Bars       | Touch each other            |
| Matplotlib | `plt.hist()`                |
| Seaborn    | `sns.histplot()`            |

---

# Key Points to Remember

* A **Histogram** represents the **frequency distribution of continuous numerical data**.
* The **X-axis** shows **class intervals (bins)**.
* The **Y-axis** shows the **frequency**.
* **Bars touch each other**, indicating continuous data.
* It helps identify:

  * Distribution shape
  * Skewness
  * Outliers
  * Spread
  * Central tendency
* Common Python functions:

  * **Matplotlib:** `plt.hist()`
  * **Seaborn:** `sns.histplot()`

---

# Easy Way to Remember

| Graph          | Remember As                                            |
| -------------- | ------------------------------------------------------ |
| **Histogram**  | 📶 Shows the distribution of continuous numerical data |
| **Bar Graph**  | 📊 Compares categorical data                           |
| **Line Graph** | 📈 Shows trends over time                              |
| **Pie Chart**  | 🥧 Shows percentages of a whole                        |

# What is Measures of Central Tendency?

**Measures of Central Tendency** are statistical measures that identify the **central or typical value** of a dataset. They describe the point around which the data values are concentrated.

These measures help summarize a large dataset using a **single representative value**.

---

# Simple Definition

> **Measures of Central Tendency are statistical measures used to find the central or average value of a dataset.**

---

# Why Do We Use Measures of Central Tendency?

Measures of Central Tendency help us to:

* Summarize large datasets.
* Find the typical or central value.
* Compare different datasets.
* Understand the overall distribution of data.
* Support statistical analysis and decision-making.

---

# Types of Measures of Central Tendency

There are **three main measures**:

| Measure    | Meaning                               |
| ---------- | ------------------------------------- |
| **Mean**   | Arithmetic average of all values      |
| **Median** | Middle value after arranging the data |
| **Mode**   | Most frequently occurring value       |

---

# Overview

```text
Measures of Central Tendency
            │
   ┌────────┼────────┐
   │        │        │
 Mean     Median    Mode
Average   Middle   Most Frequent
```

---

# 1. Mean

## What is Mean?

The **Mean** is the **sum of all observations divided by the total number of observations**.

It is the most commonly used measure of central tendency.

### Formula

[
\boxed{\text{Mean}=\frac{\sum X}{N}}
]

Where:

* **ΣX** = Sum of all observations
* **N** = Total number of observations

---

### Example

Dataset:

```text
10, 20, 30, 40, 50
```

Calculation:

[
\text{Mean}=\frac{10+20+30+40+50}{5}
=\frac{150}{5}=30
]

**Mean = 30**

---

# 2. Median

## What is Median?

The **Median** is the **middle value** of a dataset after arranging the data in ascending or descending order.

### Steps

1. Arrange the data.
2. Find the middle value.

---

### Example 1 (Odd Number of Values)

Dataset:

```text
5, 10, 15, 20, 25
```

Middle value = **15**

**Median = 15**

---

### Example 2 (Even Number of Values)

Dataset:

```text
10, 20, 30, 40
```

Middle two values = **20** and **30**

[
\text{Median}=\frac{20+30}{2}=25
]

**Median = 25**

---

# 3. Mode

## What is Mode?

The **Mode** is the value that appears **most frequently** in a dataset.

---

### Example

Dataset:

```text
2, 3, 3, 4, 5, 5, 5, 6
```

The number **5** appears **3 times**, which is more than any other value.

**Mode = 5**

---

# Types of Mode

| Type           | Description         |
| -------------- | ------------------- |
| **Unimodal**   | One mode            |
| **Bimodal**    | Two modes           |
| **Multimodal** | More than two modes |
| **No Mode**    | No value repeats    |

---

# Example Comparison

Dataset:

```text
10, 20, 20, 30, 40
```

| Measure | Value |
| ------- | ----: |
| Mean    |    24 |
| Median  |    20 |
| Mode    |    20 |

---

# Comparison of Mean, Median and Mode

| Feature                       | Mean    | Median       | Mode                |
| ----------------------------- | ------- | ------------ | ------------------- |
| Definition                    | Average | Middle value | Most frequent value |
| Uses All Values               | ✅ Yes   | ❌ No         | ❌ No                |
| Affected by Outliers          | ✅ Yes   | ❌ No         | ❌ No                |
| Suitable for Numerical Data   | ✅ Yes   | ✅ Yes        | ✅ Yes               |
| Suitable for Categorical Data | ❌ No    | ❌ No         | ✅ Yes               |

---

# When to Use Which Measure?

| Situation                 | Best Measure |
| ------------------------- | ------------ |
| Normally distributed data | Mean         |
| Data with outliers        | Median       |
| Most common category      | Mode         |
| Categorical data          | Mode         |

---

# Python Example

```python
import numpy as np
from scipy import stats

data = [10, 20, 20, 30, 40]

print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Mode:", stats.mode(data, keepdims=True))
```

---

# Applications

Measures of Central Tendency are used in:

* Statistics
* Data Science
* Machine Learning
* Business Analytics
* Economics
* Finance
* Healthcare
* Education
* Market Research

---

# Advantages

### Mean

* Easy to calculate.
* Uses all observations.
* Widely used in statistics.

### Median

* Not affected by outliers.
* Suitable for skewed data.

### Mode

* Easy to identify.
* Can be used for categorical data.

---

# Limitations

### Mean

* Highly affected by extreme values (outliers).

### Median

* Does not use all observations.

### Mode

* May not exist or may have multiple values.

---

# Interview Questions

| Question                                         | Answer                                                                        |
| ------------------------------------------------ | ----------------------------------------------------------------------------- |
| What are Measures of Central Tendency?           | Statistical measures that identify the central or typical value of a dataset. |
| What are the three measures of central tendency? | Mean, Median, and Mode.                                                       |
| Which measure is affected by outliers?           | Mean.                                                                         |
| Which measure is best for skewed data?           | Median.                                                                       |
| Which measure can be used for categorical data?  | Mode.                                                                         |

---

# Quick Cheat Sheet

| Measure | Formula / Meaning               |
| ------- | ------------------------------- |
| Mean    | ΣX ÷ N                          |
| Median  | Middle value after sorting      |
| Mode    | Most frequently occurring value |

---

# Key Points to Remember

* **Measures of Central Tendency** describe the **center of a dataset**.
* The three main measures are:

  * **Mean** → Average of all values.
  * **Median** → Middle value after sorting.
  * **Mode** → Most frequently occurring value.
* **Mean** is affected by outliers.
* **Median** is preferred for skewed distributions or data with outliers.
* **Mode** is useful for identifying the most common value and is the only measure applicable to categorical data.

---

# Easy Way to Remember

| Measure              | Remember As                             |
| -------------------- | --------------------------------------- |
| **Mean**             | ➗ Average of all values                 |
| **Median**           | 📍 Middle value                         |
| **Mode**             | ⭐ Most frequent value                   |
| **Central Tendency** | 🎯 Center or typical value of a dataset |

# What is Measure of Spread?

**Measures of Spread** (also called **Measures of Dispersion**) are statistical measures that describe **how spread out or scattered the data values are around the central value**.

While measures of central tendency (Mean, Median, Mode) tell us the **center** of the data, measures of spread tell us **how much the data varies**.

---

# Simple Definition

> **Measures of Spread are statistical measures that describe how far the data values are spread from the center of the dataset.**

---

# Why Do We Use Measures of Spread?

Measures of Spread help us to:

* Understand the variability of data.
* Compare the consistency of different datasets.
* Detect outliers.
* Measure data dispersion.
* Analyze data distribution.
* Support statistical and machine learning analysis.

---

# Example

Consider two classes with the following marks.

### Class A

```text
48, 49, 50, 51, 52
```

### Class B

```text
20, 35, 50, 65, 80
```

Both classes have the **same Mean = 50**.

However,

* **Class A** marks are close to the mean.
* **Class B** marks are spread far from the mean.

Therefore, **Class B has a larger spread (dispersion)**.

---

# Types of Measures of Spread

There are **five main measures of spread**.

| Measure                           | Purpose                                         |
| --------------------------------- | ----------------------------------------------- |
| **Range**                         | Difference between the highest and lowest value |
| **Interquartile Range (IQR)**     | Spread of the middle 50% of the data            |
| **Variance**                      | Average squared deviation from the mean         |
| **Standard Deviation**            | Average distance from the mean                  |
| **Coefficient of Variation (CV)** | Relative measure of spread                      |

---

# Overview

```text
Measures of Spread
        │
 ┌──────┼───────────────┐
 │      │               │
Range  IQR      Variance & Standard Deviation
```

---

# 1. Range

## What is Range?

The **Range** is the difference between the **maximum** and **minimum** values in a dataset.

### Formula

[
\boxed{\text{Range}=\text{Maximum Value}-\text{Minimum Value}}
]

### Example

Dataset:

```text
10, 20, 30, 40, 50
```

Maximum = **50**

Minimum = **10**

[
\text{Range}=50-10=40
]

**Range = 40**

---

# 2. Interquartile Range (IQR)

## What is IQR?

The **Interquartile Range (IQR)** measures the spread of the **middle 50%** of the data.

It is the difference between:

* **Q3 (Third Quartile)**
* **Q1 (First Quartile)**

### Formula

[
\boxed{\text{IQR}=Q_3-Q_1}
]

### Example

Dataset:

```text
10, 20, 30, 40, 50, 60, 70
```

* Q1 = 20
* Q3 = 60

[
IQR=60-20=40
]

**IQR = 40**

---

# 3. Variance

## What is Variance?

**Variance** measures the **average squared difference** between each data value and the mean.

A larger variance indicates that the data is more spread out.

### Formula (Population)

[
\boxed{\sigma^2=\frac{\sum (x-\mu)^2}{N}}
]

---

# 4. Standard Deviation

## What is Standard Deviation?

The **Standard Deviation (SD)** measures the **average distance of data values from the mean**.

It is the **square root of the variance**.

### Formula

[
\boxed{\text{Standard Deviation}=\sqrt{\text{Variance}}}
]

### Interpretation

* **Small SD** → Data is close to the mean.
* **Large SD** → Data is widely spread.

---

# 5. Coefficient of Variation (CV)

## What is Coefficient of Variation?

The **Coefficient of Variation (CV)** measures the spread **relative to the mean**.

It is useful for comparing datasets with different units or different means.

### Formula

[
\boxed{\text{CV}=\frac{\text{Standard Deviation}}{\text{Mean}}\times100}
]

---

# Example Comparison

### Dataset A

```text
48, 49, 50, 51, 52
```

Mean = **50**

Standard Deviation = **Small**

### Dataset B

```text
20, 35, 50, 65, 80
```

Mean = **50**

Standard Deviation = **Large**

Although both datasets have the same mean, Dataset B has **greater variability**.

---

# Comparison of Measures of Spread

| Measure                  | Formula                   | Purpose                  |
| ------------------------ | ------------------------- | ------------------------ |
| Range                    | Max − Min                 | Overall spread           |
| IQR                      | Q3 − Q1                   | Middle 50% spread        |
| Variance                 | Average squared deviation | Measure variability      |
| Standard Deviation       | √Variance                 | Average spread from mean |
| Coefficient of Variation | (SD / Mean) × 100         | Relative variability     |

---

# Python Example

```python
import numpy as np

data = [10, 20, 30, 40, 50]

print("Range:", max(data) - min(data))
print("Variance:", np.var(data))
print("Standard Deviation:", np.std(data))
print("IQR:", np.percentile(data, 75) - np.percentile(data, 25))
```

---

# Applications

Measures of Spread are used in:

* Statistics
* Data Science
* Machine Learning
* Finance
* Healthcare
* Quality Control
* Manufacturing
* Business Analytics
* Risk Analysis

---

# Advantages

* Describes variability in data.
* Helps compare datasets.
* Detects outliers.
* Supports statistical analysis.
* Improves understanding of data distribution.

---

# Limitations

* Range is affected by extreme values.
* Variance is expressed in squared units, making interpretation less intuitive.
* Standard deviation assumes numerical data.
* Some measures are sensitive to outliers.

---

# Interview Questions

| Question                                                          | Answer                                                                                         |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| What is a Measure of Spread?                                      | A statistical measure that describes how widely data values are distributed around the center. |
| What are the main measures of spread?                             | Range, IQR, Variance, Standard Deviation, and Coefficient of Variation.                        |
| Which measure is most affected by outliers?                       | Range.                                                                                         |
| Which measure represents the spread of the middle 50% of data?    | Interquartile Range (IQR).                                                                     |
| What is the relationship between Variance and Standard Deviation? | Standard Deviation is the square root of Variance.                                             |

---

# Quick Cheat Sheet

| Measure                  | Formula                                 |
| ------------------------ | --------------------------------------- |
| Range                    | Max − Min                               |
| IQR                      | Q3 − Q1                                 |
| Variance                 | Average squared deviation from the mean |
| Standard Deviation       | √Variance                               |
| Coefficient of Variation | (SD ÷ Mean) × 100                       |

---

# Key Points to Remember

* **Measures of Spread** describe **how dispersed the data values are**.
* They complement **Measures of Central Tendency** by explaining the variability of data.
* The five main measures are:

  * **Range** → Difference between maximum and minimum values.
  * **Interquartile Range (IQR)** → Spread of the middle 50% of data.
  * **Variance** → Average squared deviation from the mean.
  * **Standard Deviation** → Average distance from the mean.
  * **Coefficient of Variation (CV)** → Relative spread compared to the mean.
* **Small spread** means data values are close together.
* **Large spread** means data values are widely dispersed.

---

# Easy Way to Remember

| Measure                      | Remember As                        |
| ---------------------------- | ---------------------------------- |
| **Range**                    | 📏 Total spread (Highest − Lowest) |
| **IQR**                      | 📦 Spread of the middle 50%        |
| **Variance**                 | 📊 Average squared variation       |
| **Standard Deviation**       | 📍 Average distance from the mean  |
| **Coefficient of Variation** | 📈 Relative variability            |

# What are Outliers?

**Outliers** are data values that are **significantly different** from the rest of the observations in a dataset. They are unusually **high** or **low** compared to most of the data.

Outliers can occur due to **measurement errors, data entry mistakes, or genuine extreme observations**.

---

# Simple Definition

> **Outliers are observations that lie far away from the majority of the data values in a dataset.**

---

# Why Do We Study Outliers?

Outliers help us to:

* Detect unusual observations.
* Identify data entry or measurement errors.
* Understand data variability.
* Improve data quality.
* Build more accurate Machine Learning models.
* Make better statistical decisions.

---

# Example

Consider the following dataset:

```text
10, 12, 13, 15, 16, 18, 20, 95
```

Here,

* Most values lie between **10 and 20**.
* **95** is much larger than the other values.

Therefore,

**95 is an Outlier.**

---

# Another Example

Dataset:

```text
55, 57, 60, 62, 61, 59, 58, 120
```

Most values are around **60**, while **120** is much larger than the rest.

**120 is an Outlier.**

---

# Types of Outliers

| Type              | Description                                                |
| ----------------- | ---------------------------------------------------------- |
| **Lower Outlier** | An unusually small value compared to the rest of the data. |
| **Upper Outlier** | An unusually large value compared to the rest of the data. |

### Example

```text
5, 10, 12, 13, 14, 15, 18, 100
```

* **5** → Lower Outlier
* **100** → Upper Outlier

---

# Causes of Outliers

Outliers may occur because of:

* Data entry mistakes
* Measurement errors
* Equipment malfunction
* Natural variation in data
* Rare or unusual events

---

# How to Detect Outliers?

The most common methods are:

| Method                    | Description                     |
| ------------------------- | ------------------------------- |
| Box Plot                  | Visual method                   |
| IQR (Interquartile Range) | Most common statistical method  |
| Z-Score                   | Measures distance from the mean |
| Scatter Plot              | Visual detection                |

---

# 1. Detecting Outliers Using IQR

### Step 1

Calculate:

* Q1 (First Quartile)
* Q3 (Third Quartile)

### Step 2

Find the Interquartile Range (IQR):

[
\boxed{\text{IQR} = Q_3 - Q_1}
]

### Step 3

Calculate the limits:

[
\boxed{\text{Lower Limit}=Q_1-1.5\times IQR}
]

[
\boxed{\text{Upper Limit}=Q_3+1.5\times IQR}
]

Any value:

* Below the **Lower Limit** → Lower Outlier
* Above the **Upper Limit** → Upper Outlier

---

# Example

Dataset:

```text
10, 12, 13, 15, 16, 18, 20, 95
```

Suppose:

* Q1 = 12.5
* Q3 = 19

Then,

[
IQR = 19 - 12.5 = 6.5
]

Upper Limit:

[
19 + (1.5 \times 6.5)=28.75
]

Since **95 > 28.75**, **95 is an Outlier**.

---

# 2. Detecting Outliers Using a Box Plot

A **Box Plot** visually displays outliers.

```text
      •  ← Outlier

|-----|======|------|
```

* The box represents the middle **50%** of the data.
* Points outside the whiskers are **outliers**.

---

# Effect of Outliers

Outliers can affect statistical measures differently.

| Measure            | Affected by Outliers? |
| ------------------ | --------------------- |
| Mean               | ✅ Yes                 |
| Median             | ❌ No (or very little) |
| Mode               | ❌ No                  |
| Range              | ✅ Yes                 |
| Standard Deviation | ✅ Yes                 |
| Variance           | ✅ Yes                 |

---

# Example

### Dataset A

```text
10, 12, 13, 15, 16
```

Mean = **13.2**

### Dataset B

```text
10, 12, 13, 15, 100
```

Mean = **30**

Only one extreme value (**100**) changes the mean significantly.

---

# Handling Outliers

Common techniques include:

* Remove incorrect outliers.
* Correct data entry errors.
* Replace with median or mean (if appropriate).
* Cap extreme values (Winsorization).
* Apply data transformations (e.g., log transformation).
* Keep them if they represent genuine observations.

---

# Python Example

### Detect Outliers Using IQR

```python
import pandas as pd

data = pd.Series([10,12,13,15,16,18,20,95])

Q1 = data.quantile(0.25)
Q3 = data.quantile(0.75)

IQR = Q3 - Q1

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

outliers = data[(data < lower) | (data > upper)]

print(outliers)
```

---

### Visualize Using Seaborn

```python
import seaborn as sns
import matplotlib.pyplot as plt

sns.boxplot(x=data)

plt.show()
```

---

# Applications

Outlier detection is used in:

* Data Cleaning
* Statistics
* Data Science
* Machine Learning
* Fraud Detection
* Medical Diagnosis
* Financial Analysis
* Quality Control
* Network Security

---

# Advantages

* Detects unusual observations.
* Improves data quality.
* Increases model accuracy.
* Helps identify errors and anomalies.

---

# Limitations

* Not every outlier is an error.
* Removing valid outliers may lose important information.
* Different detection methods may produce different results.

---

# Interview Questions

| Question                                                         | Answer                                                             |
| ---------------------------------------------------------------- | ------------------------------------------------------------------ |
| What is an Outlier?                                              | A value that is significantly different from the rest of the data. |
| Which graph is commonly used to detect outliers?                 | Box Plot.                                                          |
| Which statistical method is commonly used to detect outliers?    | IQR (Interquartile Range).                                         |
| Are outliers always errors?                                      | No, they may represent genuine extreme observations.               |
| Which measure of central tendency is least affected by outliers? | Median.                                                            |

---

# Quick Cheat Sheet

| Concept          | Description                    |
| ---------------- | ------------------------------ |
| Outlier          | An unusually high or low value |
| Lower Outlier    | Value below the lower limit    |
| Upper Outlier    | Value above the upper limit    |
| Detection Method | IQR, Box Plot, Z-Score         |
| Visualization    | Box Plot                       |

---

# Key Points to Remember

* **Outliers** are values that are **far from the rest of the dataset**.
* They can be **extremely high** or **extremely low**.
* The most common method to detect outliers is the **IQR (Interquartile Range)** method.
* A **Box Plot** is the most common graph used to visualize outliers.
* Outliers can significantly affect:

  * **Mean**
  * **Range**
  * **Variance**
  * **Standard Deviation**
* **Median** is generally more robust than the mean when outliers are present.

---

# Easy Way to Remember

| Concept           | Remember As                                   |
| ----------------- | --------------------------------------------- |
| **Outlier**       | 📍 A value far away from the rest of the data |
| **Upper Outlier** | ⬆️ Unusually high value                       |
| **Lower Outlier** | ⬇️ Unusually low value                        |
| **IQR Method**    | 📏 Detects outliers using quartiles           |
| **Box Plot**      | 📦 Best graph for identifying outliers        |

# What is the Five-Number Summary?

The **Five-Number Summary** is a statistical summary that describes the **distribution of a dataset** using **five important values**. These values provide information about the **center, spread, and overall distribution** of the data.

It is widely used in **Statistics**, **Data Science**, and **Machine Learning** for data analysis and is the basis for creating a **Box Plot**.

---

# Simple Definition

> **The Five-Number Summary is a set of five values—Minimum, First Quartile (Q1), Median (Q2), Third Quartile (Q3), and Maximum—that summarize the distribution of a dataset.**

---

# Why Do We Use the Five-Number Summary?

The Five-Number Summary helps us to:

* Understand the distribution of data.
* Measure the spread of data.
* Identify the center of the data.
* Detect outliers.
* Create Box Plots.
* Compare different datasets.

---

# The Five Numbers

| Measure                 | Meaning                               |
| ----------------------- | ------------------------------------- |
| **Minimum**             | Smallest value in the dataset         |
| **Q1 (First Quartile)** | 25% of the data lies below this value |
| **Median (Q2)**         | Middle value of the dataset           |
| **Q3 (Third Quartile)** | 75% of the data lies below this value |
| **Maximum**             | Largest value in the dataset          |

---

# Overview

```text
Five-Number Summary

Minimum → Q1 → Median → Q3 → Maximum
   │        │        │        │        │
 Smallest   25%     50%      75%    Largest
```

---

# Example

Consider the dataset:

```text
5, 7, 9, 12, 15, 18, 20, 22, 25
```

### Step 1: Arrange the Data

```text
5, 7, 9, 12, 15, 18, 20, 22, 25
```

---

### Step 2: Find the Five Numbers

| Measure     | Value |
| ----------- | ----: |
| Minimum     |     5 |
| Q1          |     8 |
| Median (Q2) |    15 |
| Q3          |    21 |
| Maximum     |    25 |

---

# Understanding Each Value

### 1. Minimum

The **smallest observation** in the dataset.

Example:

```text
5, 7, 9, 12, 15
```

Minimum = **5**

---

### 2. First Quartile (Q1)

* Divides the **lowest 25%** of the data.
* Also called the **25th percentile**.

Example:

```text
5, 7, 9, 12
```

Q1 = **8** (average of 7 and 9)

---

### 3. Median (Q2)

* Middle value of the dataset.
* Divides the data into two equal halves.
* Also called the **50th percentile**.

Example:

```text
5, 7, 9, 12, 15, 18, 20, 22, 25
```

Median = **15**

---

### 4. Third Quartile (Q3)

* Divides the **highest 25%** of the data.
* Also called the **75th percentile**.

Example:

```text
18, 20, 22, 25
```

Q3 = **21** (average of 20 and 22)

---

### 5. Maximum

The **largest observation** in the dataset.

Example:

```text
5, 7, 9, 12, 15, 18, 20, 22, 25
```

Maximum = **25**

---

# Visual Representation

```text
Minimum    Q1      Median      Q3      Maximum
   |--------|----------|----------|-----------|
   5        8         15         21          25
```

---

# Relation with Box Plot

A **Box Plot** is constructed using the Five-Number Summary.

```text
Minimum      Q1      Median      Q3      Maximum
   |-----------|========|-----------|
               Box
```

Where:

* Left whisker → Minimum
* Left edge of box → Q1
* Line inside box → Median
* Right edge of box → Q3
* Right whisker → Maximum

---

# Five-Number Summary vs Measures of Central Tendency

| Five-Number Summary       | Measures of Central Tendency   |
| ------------------------- | ------------------------------ |
| Describes distribution    | Describes center               |
| Uses five values          | Uses Mean, Median, Mode        |
| Shows spread and outliers | Shows average or typical value |

---

# Python Example

```python
import numpy as np

data = [5,7,9,12,15,18,20,22,25]

print("Minimum:", np.min(data))
print("Q1:", np.percentile(data, 25))
print("Median:", np.median(data))
print("Q3:", np.percentile(data, 75))
print("Maximum:", np.max(data))
```

---

# Using Pandas

```python
import pandas as pd

data = pd.Series([5,7,9,12,15,18,20,22,25])

print(data.describe())
```

### Output

```text
count     9
mean     14.8
std       ...
min       5
25%       8
50%      15
75%      21
max      25
```

---

# Applications

The Five-Number Summary is used in:

* Statistics
* Data Science
* Machine Learning
* Exploratory Data Analysis (EDA)
* Box Plot creation
* Outlier detection
* Business Analytics
* Medical Research

---

# Advantages

* Provides a quick summary of the dataset.
* Easy to understand.
* Helps detect outliers.
* Useful for comparing datasets.
* Forms the basis of a Box Plot.

---

# Limitations

* Does not include every data value.
* Does not describe the shape of the distribution completely.
* Does not show the mean.

---

# Interview Questions

| Question                                         | Answer                                                             |
| ------------------------------------------------ | ------------------------------------------------------------------ |
| What is the Five-Number Summary?                 | A summary of a dataset using Minimum, Q1, Median, Q3, and Maximum. |
| What are the five numbers?                       | Minimum, Q1, Median, Q3, Maximum.                                  |
| Which graph is based on the Five-Number Summary? | Box Plot.                                                          |
| What does Q1 represent?                          | The 25th percentile.                                               |
| What does Q3 represent?                          | The 75th percentile.                                               |

---

# Quick Cheat Sheet

| Measure     | Represents      |
| ----------- | --------------- |
| Minimum     | Smallest value  |
| Q1          | 25th percentile |
| Median (Q2) | 50th percentile |
| Q3          | 75th percentile |
| Maximum     | Largest value   |

---

# Key Points to Remember

* The **Five-Number Summary** describes the **distribution of a dataset** using **five values**.
* The five values are:

  * **Minimum**
  * **First Quartile (Q1)**
  * **Median (Q2)**
  * **Third Quartile (Q3)**
  * **Maximum**
* It is used to:

  * Summarize data.
  * Measure data spread.
  * Detect outliers.
  * Create **Box Plots**.
* It is an important tool in **Statistics**, **Exploratory Data Analysis (EDA)**, and **Machine Learning**.

---

# Easy Way to Remember

| Measure         | Remember As                     |
| --------------- | ------------------------------- |
| **Minimum**     | ⬇️ Smallest value               |
| **Q1**          | 📍 25% of data below this value |
| **Median (Q2)** | 🎯 Middle value (50%)           |
| **Q3**          | 📍 75% of data below this value |
| **Maximum**     | ⬆️ Largest value                |

