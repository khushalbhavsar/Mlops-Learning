# NumPy Practice Sheet

These questions are arranged from **Beginner → Intermediate → Advanced** and cover almost every important NumPy concept used in **Data Science, Machine Learning, MLOps, and interviews**.

---

# Level 1: Array Creation (1–8)

1. Create a 1D NumPy array containing numbers from 1 to 10.
2. Create a 3×3 array filled with zeros.
3. Create a 4×4 array filled with ones.
4. Create an identity matrix of size 5×5.
5. Create an array using `arange()` from 10 to 50 with a step of 5.
6. Create 10 equally spaced numbers between 0 and 1 using `linspace()`.
7. Generate a 3×3 array of random integers between 1 and 100.
8. Create a 2×3 array filled with the value 7.

---

# Level 2: Array Attributes (9–13)

9. Find the `shape`, `size`, `ndim`, and `dtype` of a given array.
10. Find the memory occupied by an array using `nbytes`.
11. Find the size of each element using `itemsize`.
12. Check whether an array is 1D or 2D.
13. Create a float array and check its data type.

---

# Level 3: Indexing & Slicing (14–20)

14. Print the first and last element of an array.
15. Print all even-index elements from an array.
16. Reverse an array using slicing.
17. Print the second row of a 2D array.
18. Print the third column of a 2D array.
19. Extract the middle 3 elements from a 1D array.
20. Extract a 2×2 submatrix from a 4×4 matrix.

---

# Level 4: Boolean Indexing (21–24)

21. Print all elements greater than 50.
22. Print all even numbers from an array.
23. Replace all negative numbers with 0 using Boolean indexing.
24. Print elements that are greater than 20 and less than 60.

---

# Level 5: Reshaping & Resizing (25–28)

25. Convert a 1D array of 12 elements into a 3×4 matrix.
26. Convert a 3×4 matrix into a 1D array using `flatten()`.
27. Transpose a 3×3 matrix.
28. Reshape an array using `-1`.

---

# Level 6: Array Operations (29–33)

29. Add two arrays element-wise.
30. Multiply two arrays element-wise.
31. Find the dot product of two arrays.
32. Add 10 to every element using broadcasting.
33. Find the square root of every element in an array.

---

# Level 7: Statistics (34–36)

34. Find the sum, mean, median, maximum, and minimum of an array.
35. Find the index of the maximum and minimum values.
36. Calculate the standard deviation and variance of an array.

---

# Level 8: Array Manipulation (37–40)

37. Concatenate two arrays.
38. Stack two arrays vertically and horizontally.
39. Split an array into four equal parts.
40. Insert the value `100` at index `3` and then delete the element at index `5`.

---

# Bonus Interview Questions (Advanced)

41. Find all unique values in an array.
42. Sort an array in ascending order.
43. Find the indices of the sorted array using `argsort()`.
44. Count the frequency of each unique element.
45. Create a checkerboard (chessboard) pattern of size 8×8 using NumPy.
46. Find duplicate elements in an array.
47. Replace all odd numbers with `-1`.
48. Swap the first and last rows of a matrix.
49. Swap the first and last columns of a matrix.
50. Normalize an array to the range **0–1** using:

```python
(arr - arr.min()) / (arr.max() - arr.min())
```

---

# Mini Projects (Real Interview Style)

### Project 1: Student Marks Analysis

Given marks of 20 students:

- Find the average marks.
- Find the highest and lowest marks.
- Count students scoring above 80.
- Print students scoring below the average.
- Replace marks below 35 with `"Fail"` (or mark them separately).

---

### Project 2: Sales Data Analysis

Given monthly sales data:

- Find total yearly sales.
- Find the month with the highest sales.
- Find the month with the lowest sales.
- Calculate average monthly sales.
- Increase all sales by 10%.

---

### Project 3: Image Processing

Treat a 5×5 array as a grayscale image:

- Increase brightness by 50.
- Clip values between 0 and 255.
- Flip the image horizontally.
- Flip the image vertically.
- Transpose the image.

---

### Project 4: Matrix Calculator

Create two 3×3 matrices and perform:

- Addition
- Subtraction
- Element-wise multiplication
- Matrix multiplication (`np.dot()` or `@`)
- Transpose
- Determinant
- Inverse (if possible)

---

## Topics Covered

| Topic                | Questions |
| -------------------- | --------: |
| Array Creation       |         8 |
| Array Attributes     |         5 |
| Indexing & Slicing   |         7 |
| Boolean Indexing     |         4 |
| Reshaping & Resizing |         4 |
| Array Operations     |         5 |
| Statistics           |         3 |
| Array Manipulation   |         4 |
| Advanced NumPy       |        10 |
| Real-world Projects  |         4 |

This practice sheet gives you **50 coding questions plus 4 mini projects**, covering the core NumPy concepts commonly tested in interviews and used in data science and machine learning workflows.
