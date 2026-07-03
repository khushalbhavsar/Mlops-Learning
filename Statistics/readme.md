# What is Statistics?

**Statistics** is the branch of mathematics that deals with **collecting, organizing, analyzing, interpreting, and presenting data** to draw meaningful conclusions and make informed decisions.

It helps us understand patterns, trends, and relationships in data.

---

# Simple Definition

> **Statistics is the science of collecting, analyzing, interpreting, and presenting data.**

---

# Why is Statistics Important?

Statistics helps us to:

* Analyze large datasets
* Find patterns and trends
* Make predictions
* Support decision-making
* Build Machine Learning models
* Perform data analysis

---

# Real-Life Example

Suppose a class has the following marks:

```text
70, 75, 80, 85, 90
```

Using statistics, we can answer questions like:

* What is the **average** mark?
* What is the **highest** mark?
* What is the **lowest** mark?
* How much do the marks vary?

---

# Types of Statistics

## 1. Descriptive Statistics

Descriptive statistics summarize and describe the main features of a dataset.

Examples:

* Mean (Average)
* Median
* Mode
* Maximum
* Minimum
* Standard Deviation
* Variance

**Example**

```text
Marks = [70, 75, 80, 85, 90]

Mean = 80
Max = 90
Min = 70
```

---

## 2. Inferential Statistics

Inferential statistics use a **sample** to make predictions or conclusions about a larger **population**.

Example:

* Survey **1,000 voters** to predict the result of an election involving **1 million voters**.

---

# Population vs Sample

| Population                        | Sample                                |
| --------------------------------- | ------------------------------------- |
| Entire group of data              | Small subset of the population        |
| Example: All students in a school | 100 students selected from the school |

---

# Common Statistical Terms

| Term        | Meaning                                             |
| ----------- | --------------------------------------------------- |
| Data        | Collection of values                                |
| Population  | Entire dataset                                      |
| Sample      | Small part of the population                        |
| Variable    | A characteristic being measured (e.g., age, salary) |
| Observation | One record or one row of data                       |

---

# Most Important Statistical Measures

| Measure            | Purpose                                 |
| ------------------ | --------------------------------------- |
| Mean               | Average value                           |
| Median             | Middle value                            |
| Mode               | Most frequent value                     |
| Maximum            | Largest value                           |
| Minimum            | Smallest value                          |
| Range              | Difference between max and min          |
| Variance           | Measures how spread out the data is     |
| Standard Deviation | Measures the average spread of the data |
| Percentile         | Position of a value relative to others  |

---

# Statistics in Pandas

Pandas provides built-in statistical functions.

```python
import pandas as pd

df["Marks"].mean()
df["Marks"].median()
df["Marks"].mode()
df["Marks"].max()
df["Marks"].min()
df["Marks"].std()
df["Marks"].var()
df["Marks"].describe()
```

---

# Applications of Statistics

* Data Science
* Machine Learning
* Artificial Intelligence
* Business Analytics
* Healthcare
* Finance
* Marketing
* Weather Forecasting

---

# Interview Questions

| Question                                         | Answer                                                                          |
| ------------------------------------------------ | ------------------------------------------------------------------------------- |
| What is Statistics?                              | The science of collecting, analyzing, interpreting, and presenting data.        |
| What are the two main types of Statistics?       | Descriptive Statistics and Inferential Statistics.                              |
| What is Population?                              | The complete set of data.                                                       |
| What is Sample?                                  | A subset of the population.                                                     |
| Why is Statistics important in Machine Learning? | It helps analyze data, identify patterns, and build accurate predictive models. |

---

# Quick Cheat Sheet

| Topic                  | Description                    |
| ---------------------- | ------------------------------ |
| Statistics             | Study of data                  |
| Descriptive Statistics | Summarizes data                |
| Inferential Statistics | Makes predictions from samples |
| Population             | Entire dataset                 |
| Sample                 | Part of the dataset            |
| Mean                   | Average                        |
| Median                 | Middle value                   |
| Mode                   | Most frequent value            |
| Variance               | Spread of data                 |
| Standard Deviation     | Average spread of data         |

---

# Key Points to Remember

* **Statistics** is the science of **collecting, organizing, analyzing, interpreting, and presenting data**.
* It has **two main branches**:

  * **Descriptive Statistics** → Summarizes data.
  * **Inferential Statistics** → Draws conclusions from samples.
* Statistics is a fundamental concept in **Data Science**, **Machine Learning**, **Artificial Intelligence**, and **Data Analysis**.
* Common statistical measures include:

  * Mean
  * Median
  * Mode
  * Maximum
  * Minimum
  * Variance
  * Standard Deviation

### Easy Way to Remember

**Statistics = Collect → Organize → Analyze → Interpret → Present Data**

# One-Way Table (Frequency Table) in Statistics

## What is a One-Way Table?

A **One-Way Table** (also called a **Frequency Table**) is a statistical table that displays the **frequency (count)** of each unique value for **one categorical variable**.

It is called a **One-Way Table** because it summarizes **only one variable (one column)**.

---

# Example Dataset

Suppose we have the following student departments:

| Student | Department |
| ------- | ---------- |
| Rahul   | IT         |
| Priya   | HR         |
| Amit    | IT         |
| Neha    | Sales      |
| Rohit   | IT         |
| Pooja   | HR         |

---

# One-Way Table

| Department | Frequency |
| ---------- | --------: |
| IT         |         3 |
| HR         |         2 |
| Sales      |         1 |
| **Total**  |     **6** |

### Explanation

* **IT** appears **3** times.
* **HR** appears **2** times.
* **Sales** appears **1** time.

This table summarizes **only one variable**: **Department**.

---

# Creating a One-Way Table in Pandas

## Using `value_counts()`

```python
import pandas as pd

df = pd.DataFrame({
    "Department": ["IT", "HR", "IT", "Sales", "IT", "HR"]
})

print(df["Department"].value_counts())
```

### Output

```text
Department
IT       3
HR       2
Sales    1
Name: count, dtype: int64
```

---

# Using `crosstab()`

```python
pd.crosstab(index=df["Department"], columns="Frequency")
```

### Output

| Department | Frequency |
| ---------- | --------: |
| HR         |         2 |
| IT         |         3 |
| Sales      |         1 |

---

# Using `groupby()`

```python
df.groupby("Department").size()
```

### Output

```text
Department
HR       2
IT       3
Sales    1
dtype: int64
```

---

# Real-World Example

Suppose an e-commerce company wants to know how many orders came from each city.

| City   | Orders |
| ------ | ------ |
| Pune   | 5      |
| Mumbai | 3      |
| Delhi  | 2      |

This is a **One-Way Table** because it summarizes **only one variable (City)**.

---

# One-Way Table vs Two-Way Table

| One-Way Table                   | Two-Way Table                             |
| ------------------------------- | ----------------------------------------- |
| Uses one variable               | Uses two variables                        |
| Shows frequency of one category | Shows relationship between two categories |
| Example: Department count       | Example: Department × Gender              |

### One-Way Table

| Department | Count |
| ---------- | ----: |
| IT         |     3 |
| HR         |     2 |
| Sales      |     1 |

### Two-Way Table

| Department | Male | Female |
| ---------- | ---: | -----: |
| IT         |    2 |      1 |
| HR         |    1 |      1 |
| Sales      |    0 |      1 |

---

# Applications

* Count students by department.
* Count employees by department.
* Count products by category.
* Count customers by city.
* Count orders by payment method.

---

# Interview Questions

| Question                                  | Answer                                                      |
| ----------------------------------------- | ----------------------------------------------------------- |
| What is a One-Way Table?                  | A frequency table that summarizes one categorical variable. |
| Why is it called a One-Way Table?         | Because it analyzes only one variable (one column).         |
| Which Pandas function is commonly used?   | `value_counts()`                                            |
| Can `groupby()` create a One-Way Table?   | Yes, using `groupby().size()`.                              |
| What is another name for a One-Way Table? | Frequency Table.                                            |

---

# Quick Cheat Sheet

| Task                     | Pandas Function    |
| ------------------------ | ------------------ |
| Count category frequency | `value_counts()`   |
| Frequency using GroupBy  | `groupby().size()` |
| Frequency table          | `pd.crosstab()`    |

---

# Key Points to Remember

* **One-Way Table = Frequency Table**
* It analyzes **only one categorical variable**.
* It shows **how many times each category appears**.
* Most commonly created in Pandas using:

  * `value_counts()`
  * `groupby().size()`
  * `pd.crosstab()`

### Easy Way to Remember

* **One-Way Table = One Column → Count Frequency**
* **Two-Way Table = Two Columns → Compare Relationship**

# What is a Bar Graph?

A **Bar Graph** is a graphical representation of **categorical data** using **rectangular bars**, where the height (or length) of each bar represents the **frequency (count)** of each category. It is used to compare different categories and quickly identify the most and least frequent values. The PDF explains that creating a bar graph starts by building a **frequency table** and then drawing bars whose heights correspond to those frequencies. 

---

# Simple Definition

> **A Bar Graph is a chart that uses rectangular bars to show the frequency or count of different categories.**

---

# Why Do We Use a Bar Graph?

A bar graph helps us:

* Compare different categories.
* Find the most frequent category.
* Find the least frequent category.
* Visualize categorical data clearly.

---

# Example Dataset

Suppose we surveyed people's favorite fruits.

| Person | Fruit  |
| ------ | ------ |
| A      | Apple  |
| B      | Banana |
| C      | Apple  |
| D      | Apple  |
| E      | Banana |
| F      | Banana |
| G      | Apple  |
| H      | Kiwi   |
| I      | Kiwi   |
| J      | Apple  |
| K      | Mango  |
| L      | Mango  |
| M      | Apple  |
| N      | Banana |

---

# Step 1: Create a Frequency Table

Count how many times each fruit appears.

| Fruit  | Count |
| ------ | ----: |
| Apple  |     6 |
| Banana |     4 |
| Kiwi   |     2 |
| Mango  |     2 |

The PDF first converts the raw data into this frequency table before drawing the graph. 

---

# Step 2: Draw the Bar Graph

![alt text](<Favorite Fruits.png>)

---

# How to Read the Graph

* **Apple** has the highest count (**6**).
* **Banana** has **4**.
* **Kiwi** and **Mango** each have **2**.

From the graph, it is easy to answer:

* ✅ Most liked fruit → **Apple**
* ✅ Least liked fruits → **Kiwi** and **Mango**

The PDF highlights that these questions are difficult to answer from raw data but become easy once the data is visualized as a bar graph. 

---

# Components of a Bar Graph

| Component     | Description                                |
| ------------- | ------------------------------------------ |
| X-axis        | Categories (e.g., Fruit, Department, City) |
| Y-axis        | Frequency or Count                         |
| Bars          | Represent each category                    |
| Height of Bar | Represents the value or count              |
| Title         | Describes the graph                        |

---

# Characteristics of a Bar Graph

* Bars have **equal width**.
* There is **space between bars**.
* Used for **categorical (qualitative)** data.
* Can be drawn vertically or horizontally.

---

# When to Use a Bar Graph

Use a bar graph when comparing **categories**, such as:

* Favorite fruits
* Number of students in each department
* Sales by product
* Employees by department
* Population by country

---

# When Not to Use a Bar Graph

Do **not** use a bar graph when you want to show:

* Trends over time → **Use a Line Graph**
* Continuous numerical distributions → **Use a Histogram**
* Percentage composition of a whole → **Use a Pie Chart**

---

# Bar Graph vs Histogram

| Bar Graph           | Histogram                 |
| ------------------- | ------------------------- |
| Categorical data    | Continuous numerical data |
| Bars have gaps      | Bars touch each other     |
| Compares categories | Shows data distribution   |
| Example: Fruits     | Example: Student marks    |

---

# Bar Graph in Python (Matplotlib)

```python
import matplotlib.pyplot as plt

fruits = ["Apple", "Banana", "Kiwi", "Mango"]
count = [6, 4, 2, 2]

plt.bar(fruits, count)
plt.title("Favorite Fruits")
plt.xlabel("Fruit")
plt.ylabel("Count")
plt.show()
```

---

# Bar Graph in Pandas

```python
import pandas as pd

df = pd.DataFrame({
    "Fruit": ["Apple", "Banana", "Kiwi", "Mango"],
    "Count": [6, 4, 2, 2]
})

df.plot(x="Fruit", y="Count", kind="bar")
```

---

# Applications in Data Science

* Customer purchase analysis
* Product sales comparison
* Department-wise employee count
* Country population comparison
* Website traffic by source
* Survey result visualization

---

# Interview Questions

| Question                                        | Answer                                                                                |
| ----------------------------------------------- | ------------------------------------------------------------------------------------- |
| What is a Bar Graph?                            | A chart that uses rectangular bars to represent the frequency or count of categories. |
| What type of data is used?                      | Categorical (qualitative) data.                                                       |
| What does the height of a bar represent?        | Frequency, count, or value.                                                           |
| Which graph is best for trends?                 | Line Graph.                                                                           |
| Which graph is best for categorical comparison? | Bar Graph.                                                                            |

---

# Quick Cheat Sheet

| Feature   | Description                        |
| --------- | ---------------------------------- |
| Purpose   | Compare categories                 |
| Data Type | Categorical                        |
| X-axis    | Categories                         |
| Y-axis    | Frequency/Count                    |
| Bars      | Separated by gaps                  |
| Best For  | Comparing values across categories |

---

# Key Points to Remember

* **Bar Graph = Compare Categories**
* Create a **frequency table first**, then draw bars based on the counts.
* The **taller the bar, the higher the frequency**.
* Best used for **categorical data**, not continuous numerical data.
* Widely used in **Statistics, Data Science, Business Analytics, and Machine Learning** for comparing groups.


Favorite Fruits

Bar graph created from the frequency table.

fruit	count
Apple	6
Banana	4
Kiwi	2
Mango	2

# What is a Pie Chart?

A **Pie Chart** is a circular graph that represents data as **sectors (slices)** of a circle. Each slice represents a category, and its size is proportional to that category's value or percentage of the total. A pie chart is mainly used to show **how each category contributes to the whole**. 

---

# Simple Definition

> **A Pie Chart is a circular graph that shows the percentage or proportion of each category in a dataset.**

---

# Why Do We Use a Pie Chart?

A pie chart helps us:

* Show percentage distribution.
* Compare parts of a whole.
* Identify the largest and smallest categories.
* Visualize proportional data.

---

# Example Dataset

Suppose a class has 100 students.

| Department | Students |
| ---------- | -------: |
| IT         |       40 |
| HR         |       25 |
| Sales      |       20 |
| Finance    |       15 |
| **Total**  |  **100** |

---

# Percentage Calculation

Formula:

[
\text{Percentage}=\frac{\text{Category Value}}{\text{Total}} \times 100
]

| Department | Students | Percentage |
| ---------- | -------: | ---------: |
| IT         |       40 |        40% |
| HR         |       25 |        25% |
| Sales      |       20 |        20% |
| Finance    |       15 |        15% |

---

# Pie Chart

![alt text](<Students by Department.png>)

---

# How to Read the Pie Chart

* **IT** occupies the largest portion (**40%**).
* **HR** represents **25%**.
* **Sales** represents **20%**.
* **Finance** represents **15%**.

The entire circle represents **100%** of the data.

---

# Formula for Central Angle

To draw a pie chart manually, convert each category into an angle.

[
\boxed{\text{Angle}=\frac{\text{Category Value}}{\text{Total}} \times 360^\circ}
]

### Example

For IT:

[
\frac{40}{100}\times360=144^\circ
]

| Department | Percentage |    Angle |
| ---------- | ---------: | -------: |
| IT         |        40% |     144° |
| HR         |        25% |      90° |
| Sales      |        20% |      72° |
| Finance    |        15% |      54° |
| **Total**  |   **100%** | **360°** |

---

# Characteristics of a Pie Chart

* Circular in shape.
* Represents **100%** of the data.
* Each slice shows one category.
* Slice size is proportional to its value.
* Best for displaying percentages.

---

# When to Use a Pie Chart

Use a pie chart when you want to show:

* Market share of companies
* Department-wise employee percentage
* Product sales percentage
* Budget allocation
* Survey results
* Election vote share

---

# When Not to Use a Pie Chart

Avoid pie charts when:

* There are many categories (more than 5–6).
* You need precise comparisons between values.
* You want to show trends over time.

Instead use:

* **Bar Graph** → Category comparison
* **Line Graph** → Trends over time
* **Histogram** → Continuous data distribution

---

# Pie Chart vs Bar Graph

| Pie Chart                | Bar Graph                  |
| ------------------------ | -------------------------- |
| Shows parts of a whole   | Compares categories        |
| Uses percentages         | Uses frequencies or values |
| Circular graph           | Rectangular bars           |
| Total always equals 100% | No requirement for total   |
| Best for proportions     | Best for comparisons       |

---

# Pie Chart in Python (Matplotlib)

```python
import matplotlib.pyplot as plt

departments = ["IT", "HR", "Sales", "Finance"]
students = [40, 25, 20, 15]

plt.pie(students, labels=departments, autopct="%1.1f%%")
plt.title("Students by Department")
plt.show()
```

---

# Pie Chart in Pandas

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Department": ["IT", "HR", "Sales", "Finance"],
    "Students": [40, 25, 20, 15]
})

df.plot(
    kind="pie",
    y="Students",
    labels=df["Department"],
    autopct="%1.1f%%",
    legend=False
)

plt.show()
```

---

# Applications in Data Science

* Customer segmentation
* Product market share
* Budget analysis
* Website traffic sources
* Survey response percentages
* Population distribution

---

# Interview Questions

| Question                                        | Answer                                                                     |
| ----------------------------------------------- | -------------------------------------------------------------------------- |
| What is a Pie Chart?                            | A circular graph that shows the proportion or percentage of each category. |
| What does the whole circle represent?           | 100% of the data (360°).                                                   |
| Which formula is used to calculate the angle?   | `(Category Value / Total) × 360°`                                          |
| When should a Pie Chart be used?                | To show parts of a whole or percentage distribution.                       |
| Which graph is better for comparing categories? | Bar Graph.                                                                 |

---

# Quick Cheat Sheet

| Feature       | Description                  |
| ------------- | ---------------------------- |
| Purpose       | Show percentage distribution |
| Shape         | Circle                       |
| Total         | 100% (360°)                  |
| Best For      | Parts of a whole             |
| Formula       | `(Value / Total) × 100`      |
| Angle Formula | `(Value / Total) × 360°`     |

---

# Key Points to Remember

* **Pie Chart = Parts of a Whole**
* The **entire circle represents 100% (360°)**.
* Each slice represents a **category's proportion**.
* Best for showing **percentages**, not detailed comparisons.
* Widely used in **Statistics, Data Science, Business Analytics, and Reporting** to visualize how a total is divided among categories.


Students by Department

Percentage distribution of students across departments.

department	students
IT	40
HR	25
Sales	20
Finance	15

# What is a Line Graph?

A **Line Graph** is a graph that displays data points connected by **straight lines**. It is mainly used to show **changes or trends over time** or over an ordered sequence.

Each point on the graph represents a value, and the line connecting the points helps visualize how the data increases, decreases, or remains constant.

---

# Simple Definition

> **A Line Graph is a graph that connects data points with straight lines to show trends or changes over time.**

---

# Why Do We Use a Line Graph?

A line graph helps us to:

* Show trends over time.
* Compare changes between different time periods.
* Identify increasing or decreasing patterns.
* Predict future trends based on past data.

---

# Example Dataset

Suppose a company records monthly sales.

| Month | Sales |
| ----- | ----: |
| Jan   |   120 |
| Feb   |   150 |
| Mar   |   180 |
| Apr   |   170 |
| May   |   210 |
| Jun   |   250 |

---

# Line Graph

![alt text](<Monthly Sales Trend.png>)

---

# How to Read the Line Graph

* Sales increased from **January (120)** to **March (180)**.
* Sales decreased slightly in **April (170)**.
* Sales increased again in **May (210)** and **June (250)**.

This graph clearly shows the **sales trend over time**.

---

# Components of a Line Graph

| Component   | Description                                       |
| ----------- | ------------------------------------------------- |
| X-axis      | Time or ordered categories (Month, Year, Day)     |
| Y-axis      | Numerical values (Sales, Population, Temperature) |
| Data Points | Individual observations                           |
| Line        | Connects the data points                          |
| Title       | Describes the graph                               |

---

# Characteristics of a Line Graph

* Data points are connected by straight lines.
* Best used for **continuous data**.
* Shows increasing or decreasing trends.
* X-axis usually represents **time**.
* Easy to compare multiple datasets using multiple lines.

---

# When to Use a Line Graph

Use a line graph for:

* Monthly sales
* Daily temperature
* Stock market prices
* Population growth
* Website traffic
* Rainfall over months
* Company revenue over years

---

# When Not to Use a Line Graph

Avoid using a line graph for:

* Comparing unrelated categories (use a **Bar Graph**).
* Showing percentage distribution (use a **Pie Chart**).
* Showing frequency distribution of continuous data (use a **Histogram**).

---

# Line Graph vs Bar Graph

| Line Graph                     | Bar Graph                    |
| ------------------------------ | ---------------------------- |
| Shows trends over time         | Compares categories          |
| Data points connected by lines | Data shown using bars        |
| Best for continuous data       | Best for categorical data    |
| X-axis usually represents time | X-axis represents categories |

---

# Line Graph vs Pie Chart

| Line Graph              | Pie Chart              |
| ----------------------- | ---------------------- |
| Shows changes over time | Shows parts of a whole |
| Uses lines              | Uses slices            |
| Continuous data         | Percentage data        |

---

# Python Example (Matplotlib)

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [120, 150, 180, 170, 210, 250]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()
```

---

# Pandas Example

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [120, 150, 180, 170, 210, 250]
})

df.plot(x="Month", y="Sales", kind="line", marker="o")
plt.show()
```

---

# Applications in Data Science

* Stock price analysis
* Sales forecasting
* Weather forecasting
* Website traffic analysis
* Population growth analysis
* COVID-19 case trends
* Machine learning model performance over epochs

---

# Interview Questions

| Question                                     | Answer                                                                          |
| -------------------------------------------- | ------------------------------------------------------------------------------- |
| What is a Line Graph?                        | A graph that connects data points with straight lines to show trends over time. |
| Which type of data is best for a Line Graph? | Continuous or time-series data.                                                 |
| What does the X-axis usually represent?      | Time or an ordered sequence.                                                    |
| What does the Y-axis represent?              | Numerical values.                                                               |
| Which graph is best for showing trends?      | Line Graph.                                                                     |

---

# Quick Cheat Sheet

| Feature   | Description                      |
| --------- | -------------------------------- |
| Purpose   | Show trends or changes over time |
| Data Type | Continuous or time-series        |
| X-axis    | Time (Month, Year, Day)          |
| Y-axis    | Numerical values                 |
| Best For  | Trend analysis and forecasting   |

---

# Key Points to Remember

* **Line Graph = Trend Over Time**
* Data points are connected using **straight lines**.
* Best used for **continuous or time-based data**.
* Helps identify **increasing, decreasing, and stable trends**.
* Widely used in **Statistics, Data Science, Business Analytics, Finance, and Machine Learning** to visualize trends and make predictions.


Monthly Sales Trend

Sales of a company over six months.

month	sales
Jan	120
Feb	150
Mar	180
Apr	170
May	210
Jun	250


# What is an Ogive?

An **Ogive** (pronounced *Oh-jive*) is a **cumulative frequency graph**. It is created by plotting the **cumulative frequency** against the **class boundaries** and joining the points with straight lines.

An ogive helps us understand **how data accumulates** across different class intervals.

---

# Simple Definition

> **An Ogive is a graph of cumulative frequencies used to show how frequencies accumulate over class intervals.**

---

# Why Do We Use an Ogive?

An ogive helps us to:

* Find the cumulative frequency.
* Determine the **Median**.
* Find **Quartiles (Q1, Q2, Q3)**.
* Find **Percentiles**.
* Compare two distributions.
* Understand how data accumulates.

---

# Types of Ogive

There are **two types** of ogive:

| Type                | Description                                                         |
| ------------------- | ------------------------------------------------------------------- |
| **Less Than Ogive** | Uses cumulative frequencies up to the upper class boundary.         |
| **More Than Ogive** | Uses cumulative frequencies from the lower class boundary downward. |

---

# Example Dataset

Suppose the marks of students are grouped as follows:

| Marks | Frequency |
| ----- | --------: |
| 0–10  |         5 |
| 10–20 |         8 |
| 20–30 |        12 |
| 30–40 |        10 |
| 40–50 |         5 |

---

# Step 1: Find Cumulative Frequency

## Less Than Cumulative Frequency

| Marks | Frequency | Cumulative Frequency |
| ----- | --------: | -------------------: |
| 0–10  |         5 |                    5 |
| 10–20 |         8 |                   13 |
| 20–30 |        12 |                   25 |
| 30–40 |        10 |                   35 |
| 40–50 |         5 |                   40 |

---

# Step 2: Draw the Ogive

Plot the points:

```text
(10,5)
(20,13)
(30,25)
(40,35)
(50,40)
```

Join these points with straight lines to obtain the **Less Than Ogive**.

---

# How to Read an Ogive

Suppose the graph shows:

* At **30 marks**, cumulative frequency = **25**.

This means:

> **25 students scored less than or equal to 30 marks.**

---

# Components of an Ogive

| Component | Description                          |
| --------- | ------------------------------------ |
| X-axis    | Upper (or lower) class boundaries    |
| Y-axis    | Cumulative Frequency                 |
| Points    | Cumulative frequencies               |
| Line      | Connects cumulative frequency points |

---

# Characteristics of an Ogive

* Uses **cumulative frequency**.
* Points are joined by straight lines.
* Always increases in a **Less Than Ogive**.
* Used to determine median and quartiles.
* Suitable for grouped continuous data.

---

# Less Than vs More Than Ogive

| Less Than Ogive                              | More Than Ogive                              |
| -------------------------------------------- | -------------------------------------------- |
| Uses upper class boundaries                  | Uses lower class boundaries                  |
| Starts from the smallest value               | Starts from the largest cumulative frequency |
| Graph rises upward                           | Graph slopes downward                        |
| Used to find cumulative values below a point | Used to find cumulative values above a point |

---

# Applications

Ogives are used to:

* Find the **Median**
* Find **Quartiles**
* Find **Percentiles**
* Compare two datasets
* Analyze exam results
* Analyze income distribution
* Analyze age distribution

---

# Python Example (Matplotlib)

```python
import matplotlib.pyplot as plt

upper_boundary = [10, 20, 30, 40, 50]
cum_freq = [5, 13, 25, 35, 40]

plt.plot(upper_boundary, cum_freq, marker="o")
plt.title("Less Than Ogive")
plt.xlabel("Marks")
plt.ylabel("Cumulative Frequency")
plt.grid(True)
plt.show()
```

---

# Pandas Example

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Upper Boundary": [10,20,30,40,50],
    "Cumulative Frequency": [5,13,25,35,40]
})

df.plot(
    x="Upper Boundary",
    y="Cumulative Frequency",
    kind="line",
    marker="o"
)

plt.show()
```

---

# Applications in Data Science

Although **Ogives are not commonly used in Machine Learning**, they are useful in:

* Exploratory Data Analysis (EDA)
* Understanding cumulative distributions
* Finding percentiles and quartiles
* Data visualization
* Statistical reporting

---

# Interview Questions

| Question                           | Answer                                                                  |
| ---------------------------------- | ----------------------------------------------------------------------- |
| What is an Ogive?                  | A graph of cumulative frequency.                                        |
| How many types of Ogive are there? | Two: Less Than Ogive and More Than Ogive.                               |
| What is plotted on the X-axis?     | Class boundaries (usually upper or lower).                              |
| What is plotted on the Y-axis?     | Cumulative Frequency.                                                   |
| What is an Ogive mainly used for?  | Finding the median, quartiles, percentiles, and cumulative frequencies. |

---

# Quick Cheat Sheet

| Feature    | Description                    |
| ---------- | ------------------------------ |
| Graph Type | Cumulative Frequency Graph     |
| X-axis     | Class Boundaries               |
| Y-axis     | Cumulative Frequency           |
| Types      | Less Than, More Than           |
| Best For   | Median, Quartiles, Percentiles |

---

# Key Points to Remember

* **Ogive = Cumulative Frequency Graph**
* It is constructed using **cumulative frequencies**, not simple frequencies.
* There are **two types**:

  * **Less Than Ogive**
  * **More Than Ogive**
* It is widely used to determine:

  * Median
  * Quartiles (Q1, Q2, Q3)
  * Percentiles
* Ogives are an important tool in **Statistics** for analyzing grouped data and understanding cumulative distributions.
