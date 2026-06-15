# 📦 Python Lists + 🗂️ Dictionaries (Complete Guide)

> A **complete, interview-ready guide to Python Lists + Dictionaries**  
> (Simple → Advanced, with examples you can revise before interviews) 📘

---

## 🔹 PYTHON LISTS

A **list** is an **ordered, mutable** collection of items.

### ✅ Create a List

```python
nums = [1, 2, 3]
mix = [1, "Python", 3.5, True]
```

### 🔹 Access Elements

```python
nums[0]     # 1
nums[-1]    # 3
```

### 🔹 Modify List (Mutable)

```python
nums[0] = 100
print(nums)   # [100, 2, 3]
```

### 🔹 Important List Methods (with Examples)

```python
lst = [1, 2, 3]
```

| Method      | Example             | Result          |
|-------------|---------------------|-----------------|
| `append()`  | `lst.append(4)`     | `[1,2,3,4]`     |
| `extend()`  | `lst.extend([5,6])` | `[1,2,3,4,5,6]` |
| `insert()`  | `lst.insert(1, 10)` | `[1,10,2,3]`    |
| `remove()`  | `lst.remove(10)`    | removes value   |
| `pop()`     | `lst.pop()`         | removes last    |
| `index()`   | `lst.index(2)`      | index           |
| `count()`   | `lst.count(2)`      | frequency       |
| `sort()`    | `lst.sort()`        | ascending       |
| `reverse()` | `lst.reverse()`     | reverse         |
| `clear()`   | `lst.clear()`       | empty list      |

### 🔹 List Slicing

```python
lst = [1, 2, 3, 4, 5]
lst[1:4]    # [2, 3, 4]
lst[::-1]   # reverse
```

### 🔹 List Comprehension (🔥 Important)

```python
squares = [x * x for x in range(5)]
```

### 🔹 Common List Interview Questions

- ✔ Mutable or Immutable? → **Mutable**
- ✔ Allows duplicates? → **Yes**
- ✔ Ordered? → **Yes**

---

## 🔹 PYTHON DICTIONARIES

A **dictionary** stores data as **key : value pairs**.

### ✅ Create Dictionary

```python
student = {
    "name": "Khushal",
    "age": 22,
    "skill": "Python"
}
```

### 🔹 Access Values

```python
student["name"]
student.get("age")
```

### 🔹 Modify Dictionary

```python
student["age"] = 23
student["city"] = "Pune"
```

### 🔹 Important Dictionary Methods (with Examples)

```python
d = {"a": 1, "b": 2}
```

| Method      | Example             | Result          |
|-------------|---------------------|-----------------|
| `keys()`    | `d.keys()`          | all keys        |
| `values()`  | `d.values()`        | all values      |
| `items()`   | `d.items()`         | key-value pairs |
| `get()`     | `d.get("a")`        | safe access     |
| `update()`  | `d.update({"c":3})` | add/update      |
| `pop()`     | `d.pop("a")`        | remove key      |
| `popitem()` | `d.popitem()`       | last item       |
| `clear()`   | `d.clear()`         | empty           |
| `copy()`    | `d.copy()`          | shallow copy    |

### 🔹 Looping Dictionary

```python
for key, value in student.items():
    print(key, value)
```

### 🔹 Dictionary Comprehension (🔥 Important)

```python
squares = {x: x * x for x in range(5)}
```

### 🔹 Nested Dictionary

```python
data = {
    "user": {
        "name": "A",
        "skills": ["Python", "DevOps"]
    }
}
```

---

## 🆚 LIST vs DICTIONARY (Interview Favorite)

| Feature           | List              | Dictionary     |
|-------------------|-------------------|----------------|
| Ordered           | ✅ Yes            | ✅ Yes (3.7+)  |
| Mutable           | ✅ Yes            | ✅ Yes         |
| Indexing          | By index          | By key         |
| Duplicate allowed | ✅ Yes            | ❌ Keys unique |
| Use case          | Sequence of items | Fast lookup    |

---

## ⚠️ Common Interview Traps

### ❌ KeyError

```python
student["marks"]      # error
student.get("marks")  # safe
```

### ❌ Copy vs Reference

```python
a = [1, 2]
b = a
b.append(3)
# both change

c = a.copy()
```

---

## 🎯 Interview Tips (VERY IMPORTANT)

- ✔ Use **list** when order matters
- ✔ Use **dict** for fast lookup
- ✔ Prefer `get()` over direct access
- ✔ Master **comprehensions**

---

# 🔒 Python Tuple (Complete Guide)

> A **clear, interview-ready explanation of TUPLES in Python**  
> (Simple → Advanced, with examples) 📘

---

## 🔹 What is a Tuple?

A **tuple** is an **ordered, immutable** collection of elements.

```python
t = (1, 2, 3)
```

## 🔹 Creating Tuples

```python
t1 = (1, 2, 3)
t2 = 1, 2, 3          # tuple packing
t3 = (5,)             # single-element tuple (comma is required)
t4 = tuple([1, 2, 3]) # from list
```

> ⚠️ `(5)` → NOT a tuple  
> ✅ `(5,)` → tuple

## 🔹 Accessing Tuple Elements

```python
t = ("Python", "DevOps", "Cloud")

t[0]     # 'Python'
t[-1]    # 'Cloud'
```

## 🔹 Tuple Slicing

```python
t = (1, 2, 3, 4, 5)

t[1:4]    # (2, 3, 4)
t[::-1]   # reverse
```

## 🔹 Tuple is IMMUTABLE ❌

```python
t = (1, 2, 3)
t[0] = 10   # ❌ TypeError
```

> 👉 You **cannot** add, remove, or modify elements.

## 🔹 Tuple Methods (Very Few!)

```python
t = (1, 2, 2, 3)
```

| Method    | Example      | Result |
|-----------|--------------|--------|
| `count()` | `t.count(2)` | 2      |
| `index()` | `t.index(3)` | 3      |

## 🔹 Looping Through Tuple

```python
for item in t:
    print(item)
```

## 🔹 Tuple Packing & Unpacking (🔥 Important)

### Packing

```python
t = 10, 20, 30
```

### Unpacking

```python
a, b, c = t
```

### Extended Unpacking

```python
a, *b, c = (1, 2, 3, 4, 5)
# a=1, b=[2,3,4], c=5
```

## 🔹 Nested Tuple

```python
t = (1, (2, 3), (4, 5))
```

## 🔹 Convert Tuple ↔ List

```python
lst = list(t)
tup = tuple(lst)
```

---

## 🆚 Tuple vs List (Interview Favorite)

| Feature | Tuple       | List     |
|---------|-------------|----------|
| Mutable | ❌ No       | ✅ Yes   |
| Methods | Very few    | Many     |
| Speed   | ⚡ Faster   | Slower   |
| Memory  | Less        | More     |
| Safety  | Thread-safe | Not safe |

---

## 🔹 Why Use Tuples? (Interview Question)

- ✔ Faster than lists
- ✔ Protect data (immutable)
- ✔ Can be used as **dictionary keys**
- ✔ Suitable for fixed data (coordinates, DB rows)

## 🔹 Tuple as Dictionary Key

```python
location = {
    (18.52, 73.85): "Pune",
    (19.07, 72.87): "Mumbai"
}
```

---

## 🔹 Common Tuple Interview Questions

### ✔ Can tuple store mutable objects?

Yes!

```python
t = (1, [2, 3])
t[1].append(4)  # allowed
```

### ✔ Tuple vs NamedTuple?

`namedtuple` gives readable fields.

### ✔ When to prefer tuple over list?

When data should **not change**.

---




