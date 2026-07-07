# Matplotlib, Seaborn, Plotly, and Cufflinks Notes

This repository contains beginner-friendly notes and notebooks for Python data
visualization. The topics are arranged from basic chart selection to Matplotlib,
Seaborn, Plotly, Cufflinks, and an IPL capstone project.

## Repository Contents

| File | Topic |
| --- | --- |
| `1_Matplotlib.ipynb` | Matplotlib basics, subplots, object-oriented plotting, saving plots, and images |
| `2_Distributionplot.ipynb` | Seaborn distribution plots |
| `3_Categoricalplots.ipynb` | Seaborn categorical plots |
| `4_Matrixplot.ipynb` | Heatmaps, clustermaps, and correlation matrices |
| `5_regression.ipynb` | Regression plots with Seaborn |
| `6_plotlyandcufflinks.ipynb` | Interactive plotting with Plotly and Cufflinks |
| `IPL_Capstone_Project.ipynb` | IPL data visualization project |
| `IPL.csv` | Dataset used in the capstone project |

## Table of Contents

1. [Data Visualization Basics](#data-visualization-basics)
2. [Library Overview](#library-overview)
3. [Matplotlib](#matplotlib)
4. [Seaborn Distribution Plots](#seaborn-distribution-plots)
5. [Seaborn Categorical Plots](#seaborn-categorical-plots)
6. [Seaborn Matrix Plots](#seaborn-matrix-plots)
7. [Seaborn Regression Plots](#seaborn-regression-plots)
8. [Plotly and Cufflinks](#plotly-and-cufflinks)
9. [Quick Reference](#quick-reference)
10. [Interview Questions](#interview-questions)

## Data Visualization Basics

Data visualization is the graphical representation of data using charts,
graphs, maps, and other visual elements. It helps convert raw data into a form
that is easier to understand, analyze, and communicate.

### Why Data Visualization Is Used

- Understand large datasets quickly.
- Identify patterns, trends, and relationships.
- Detect outliers and unusual values.
- Compare categories or groups.
- Communicate insights clearly.
- Support data-driven decisions.

### Basic Workflow

```text
Collect Data
Clean Data
Analyze Data
Visualize Data
Find Insights
Make Decisions
```

### Choosing the Right Chart

| Requirement | Recommended Chart |
| --- | --- |
| Compare categories | Bar chart |
| Show trend over time | Line chart |
| Show percentage share | Pie chart |
| Show distribution | Histogram or KDE plot |
| Show relationship between two numeric variables | Scatter plot |
| Detect spread and outliers | Box plot |
| Show correlation matrix | Heatmap |

## Library Overview

| Library | Best For | Main Strength |
| --- | --- | --- |
| Matplotlib | Basic and fully customized charts | Low-level control |
| Seaborn | Statistical visualizations and EDA | Clean defaults with less code |
| Plotly | Interactive charts and dashboards | Hover, zoom, pan, and web output |
| Cufflinks | Quick interactive Pandas plots | Direct `df.iplot()` syntax |

### When to Use Which Library

| Use Case | Best Choice |
| --- | --- |
| Basic static chart | Matplotlib |
| Statistical EDA | Seaborn |
| Correlation heatmap | Seaborn |
| Interactive dashboard | Plotly |
| Quick interactive DataFrame chart | Cufflinks |
| Maximum customization | Matplotlib or Plotly |

## Matplotlib

Matplotlib is the foundational Python visualization library. It is commonly
imported as:

```python
import matplotlib.pyplot as plt
```

### Common Plot Types

| Chart | Function | Use |
| --- | --- | --- |
| Line plot | `plt.plot()` | Trends |
| Bar chart | `plt.bar()` | Category comparison |
| Horizontal bar chart | `plt.barh()` | Category comparison with long labels |
| Scatter plot | `plt.scatter()` | Relationship between variables |
| Histogram | `plt.hist()` | Distribution |
| Pie chart | `plt.pie()` | Proportions |
| Box plot | `plt.boxplot()` | Spread and outliers |
| Area plot | `plt.fill_between()` | Cumulative or filled trends |

### Basic Example

```python
import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr"]
sales = [120, 150, 180, 170]

plt.plot(months, sales, marker="o")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
```

### Useful Functions

| Function | Purpose |
| --- | --- |
| `plt.title()` | Add chart title |
| `plt.xlabel()` | Add x-axis label |
| `plt.ylabel()` | Add y-axis label |
| `plt.legend()` | Show legend |
| `plt.grid()` | Show grid lines |
| `plt.xlim()` | Set x-axis limit |
| `plt.ylim()` | Set y-axis limit |
| `plt.savefig()` | Save the plot |

### Subplots

Subplots allow multiple charts in one figure.

```python
import matplotlib.pyplot as plt

plt.subplot(1, 2, 1)
plt.plot([1, 2, 3], [2, 4, 6])
plt.title("Plot 1")

plt.subplot(1, 2, 2)
plt.plot([1, 2, 3], [3, 2, 5])
plt.title("Plot 2")

plt.tight_layout()
plt.show()
```

### Object-Oriented API

The object-oriented API is recommended for professional work because it gives
better control over figures and axes.

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title("Sales")
ax.set_xlabel("Month")
ax.set_ylabel("Sales")
plt.show()
```

| Object | Meaning |
| --- | --- |
| `Figure` | Complete canvas/window |
| `Axes` | Individual plotting area |

### Saving Plots

```python
plt.savefig("plot.png", dpi=300, bbox_inches="tight")
```

Common file formats include PNG, JPG, SVG, and PDF.

### Working With Images

```python
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("image.png")
plt.imshow(img)
plt.axis("off")
plt.show()
```

## Seaborn Distribution Plots

Distribution plots show how values are spread across a dataset. They are useful
for checking shape, skewness, concentration, and outliers.

```python
import seaborn as sns
import matplotlib.pyplot as plt
```

### Main Distribution Functions

| Plot | Function | Use |
| --- | --- | --- |
| Histogram | `sns.histplot()` | Frequency distribution |
| KDE plot | `sns.kdeplot()` | Smooth density curve |
| Joint plot | `sns.jointplot()` | Relationship plus distributions |
| Pair plot | `sns.pairplot()` | Pairwise relationships |
| Rug plot | `sns.rugplot()` | Individual observations on an axis |
| Displot | `sns.displot()` | Figure-level distribution plot |

Note: `sns.distplot()` is older syntax. Prefer `histplot()`, `kdeplot()`, or
`displot()` in new code.

### Examples

```python
tips = sns.load_dataset("tips")

sns.histplot(data=tips, x="total_bill", kde=True)
plt.show()
```

```python
sns.jointplot(data=tips, x="total_bill", y="tip", kind="scatter")
plt.show()
```

```python
sns.pairplot(tips, hue="sex")
plt.show()
```

### Common Parameters

| Parameter | Purpose |
| --- | --- |
| `x` | Column for x-axis |
| `y` | Column for y-axis |
| `data` | DataFrame |
| `hue` | Grouping variable |
| `kde=True` | Add density curve |
| `bins` | Number of histogram bins |
| `kind` | Plot type in figure-level functions |

## Seaborn Categorical Plots

Categorical plots compare numeric values across groups or show how categories
are distributed.

### Main Categorical Functions

| Plot | Function | Use |
| --- | --- | --- |
| Box plot | `sns.boxplot()` | Spread, median, quartiles, and outliers |
| Violin plot | `sns.violinplot()` | Distribution shape by category |
| Strip plot | `sns.stripplot()` | Individual data points |
| Swarm plot | `sns.swarmplot()` | Individual points without overlap |
| Bar plot | `sns.barplot()` | Estimated mean by category |
| Count plot | `sns.countplot()` | Count of category values |
| Cat plot | `sns.catplot()` | Figure-level categorical plotting |

### Box Plot

```python
sns.boxplot(data=tips, x="day", y="total_bill")
plt.show()
```

Box plots show median, quartiles, spread, and possible outliers.

### Violin Plot

```python
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex")
plt.show()
```

Violin plots combine box plot information with distribution shape.

### Strip Plot and Swarm Plot

```python
sns.stripplot(data=tips, x="day", y="total_bill", jitter=True)
plt.show()
```

```python
sns.swarmplot(data=tips, x="day", y="total_bill")
plt.show()
```

Use strip plots for many points and swarm plots when overlap must be avoided.

### Bar Plot and Count Plot

```python
sns.barplot(data=tips, x="day", y="total_bill")
plt.show()
```

```python
sns.countplot(data=tips, x="day")
plt.show()
```

Use `barplot()` for numeric summaries and `countplot()` for category counts.

## Seaborn Matrix Plots

Matrix plots display data in a grid format. They are mainly used for
correlation matrices, missing value patterns, confusion matrices, and clustered
relationships.

### Heatmap

```python
corr = tips.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.show()
```

| Parameter | Purpose |
| --- | --- |
| `annot=True` | Show values inside cells |
| `cmap` | Color map |
| `linewidths` | Add borders between cells |
| `square=True` | Force square cells |
| `vmin`, `vmax` | Fix color scale range |

### Clustermap

```python
sns.clustermap(corr, annot=True, cmap="coolwarm")
plt.show()
```

A clustermap is a heatmap with hierarchical clustering. It groups similar rows
and columns together.

### Correlation Values

| Value | Meaning |
| --- | --- |
| `1` | Perfect positive correlation |
| `0` | No linear correlation |
| `-1` | Perfect negative correlation |

## Seaborn Regression Plots

Regression plots show the relationship between two numeric variables and add a
best-fit trend line.

### `regplot()`

```python
sns.regplot(data=tips, x="total_bill", y="tip")
plt.show()
```

### Important Parameters

| Parameter | Purpose |
| --- | --- |
| `x` | Independent variable |
| `y` | Dependent variable |
| `data` | DataFrame |
| `ci=None` | Remove confidence interval |
| `scatter=False` | Show only regression line |
| `scatter_kws` | Customize points |
| `line_kws` | Customize line |

### Custom Example

```python
sns.regplot(
    data=tips,
    x="total_bill",
    y="tip",
    ci=None,
    scatter_kws={"s": 60},
    line_kws={"color": "red"}
)
plt.show()
```

### Regression Plot vs Scatter Plot

| Scatter Plot | Regression Plot |
| --- | --- |
| Shows individual points | Shows points plus trend line |
| Good for observing relationship | Good for analyzing trend |
| No fitted line by default | Includes best-fit regression line |

## Plotly and Cufflinks

Plotly creates interactive charts. Cufflinks connects Pandas with Plotly so
interactive plots can be created directly from DataFrames.

### Plotly

```python
import plotly.express as px

df = px.data.iris()

fig = px.scatter(
    df,
    x="sepal_length",
    y="petal_length",
    color="species"
)
fig.show()
```

### Common Plotly Express Functions

| Chart | Function |
| --- | --- |
| Line plot | `px.line()` |
| Scatter plot | `px.scatter()` |
| Bar chart | `px.bar()` |
| Histogram | `px.histogram()` |
| Pie chart | `px.pie()` |
| Box plot | `px.box()` |
| Violin plot | `px.violin()` |
| Heatmap/image | `px.imshow()` |

### Cufflinks

```python
import pandas as pd
import cufflinks as cf

cf.go_offline()

df = pd.DataFrame({
    "Sales": [100, 150, 200, 250]
})

df.iplot(kind="line")
```

### Plotly vs Cufflinks

| Feature | Plotly | Cufflinks |
| --- | --- | --- |
| Main purpose | Interactive visualization library | Pandas wrapper for Plotly |
| Main syntax | `px.scatter(...)` or `go.Figure(...)` | `df.iplot(...)` |
| Best for | Custom interactive charts | Quick DataFrame charts |
| Interactivity | Yes | Yes |

## Quick Reference

### Chart Selection

| Goal | Chart |
| --- | --- |
| Trend | Line plot |
| Comparison | Bar chart |
| Distribution | Histogram, KDE plot |
| Relationship | Scatter plot, regression plot |
| Outliers | Box plot |
| Category counts | Count plot |
| Correlation | Heatmap |
| Interactive analysis | Plotly or Cufflinks |

### Common Imports

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import cufflinks as cf
```

### Most Used Functions

| Library | Functions |
| --- | --- |
| Matplotlib | `plot()`, `bar()`, `hist()`, `scatter()`, `pie()`, `savefig()` |
| Seaborn | `histplot()`, `boxplot()`, `barplot()`, `heatmap()`, `regplot()` |
| Plotly | `px.line()`, `px.scatter()`, `px.bar()`, `px.histogram()` |
| Cufflinks | `df.iplot()` |

## Interview Questions

| Question | Short Answer |
| --- | --- |
| What is data visualization? | Representing data graphically to understand and communicate insights. |
| Why is data visualization important? | It reveals patterns, trends, relationships, and outliers quickly. |
| Which chart is best for trends over time? | Line chart. |
| Which chart is best for comparing categories? | Bar chart. |
| Which chart is best for distribution? | Histogram or KDE plot. |
| Which chart is useful for outliers? | Box plot. |
| What is Matplotlib? | A Python library for static and customizable visualizations. |
| What is Seaborn? | A statistical visualization library built on Matplotlib. |
| What is Plotly? | A library for interactive charts and dashboards. |
| What is Cufflinks? | A library that connects Pandas DataFrames with Plotly. |
| What does `sns.heatmap()` show? | A color-coded matrix, commonly used for correlations. |
| What does `sns.regplot()` show? | A scatter plot with a fitted regression line. |

## Key Points

- Use Matplotlib when you need full control.
- Use Seaborn for statistical analysis and clean default charts.
- Use Plotly when interactivity is important.
- Use Cufflinks for quick interactive charts directly from Pandas.
- Choose charts based on the question you want the data to answer.
