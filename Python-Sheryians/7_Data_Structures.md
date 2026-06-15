# Advanced Data Structures: Sets and Dictionaries

## Sets in Python

### What are Sets?

A set is an unordered collection of unique items defined using curly braces `{}` or the `set()` function.

### Set Characteristics

**1. Mutable**: Elements can be added or removed after creation.

```python
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}
```

**2. No Duplicates**: Sets automatically remove duplicate elements.

```python
my_set = {1, 2, 2, 3}
print(my_set)  # {1, 2, 3}
```

**3. Unordered**: Sets do not maintain element order.

```python
my_set = {5, 3, 8}
print(my_set)  # Order may vary
```

**4. Heterogeneous**: Sets can contain different data types.

```python
my_set = {1, "hello", 3.14, True}
print(my_set)  # Order may vary
```

### Set Traversal

```python
numbers = {1, 2, 3, 4, 5}
for num in numbers:
    print(num)
```

### Common Set Methods

```python
# add(): Add single element
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

# remove(): Remove element (raises KeyError if not found)
my_set.remove(2)
print(my_set)  # {1, 3, 4}

# discard(): Remove element without error
my_set.discard(5)
print(my_set)  # {1, 3, 4}

# pop(): Remove arbitrary element
element = my_set.pop()
print(element, my_set)

# clear(): Remove all elements
my_set.clear()
print(my_set)  # set()

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# union(): Combine sets
union = set1.union(set2)
print(union)  # {1, 2, 3, 4, 5}

# intersection(): Common elements
intersection = set1.intersection(set2)
print(intersection)  # {3}

# difference(): Elements in set1 but not set2
difference = set1.difference(set2)
print(difference)  # {1, 2}

# symmetric_difference(): Elements in either but not both
sym_diff = set1.symmetric_difference(set2)
print(sym_diff)  # {1, 2, 4, 5}
```

## Dictionaries in Python

### What are Dictionaries?

A dictionary is an unordered collection of key-value pairs defined using curly braces with colons `{"key": value}`.

### Dictionary Characteristics

**1. Mutable**: Can be modified after creation.

```python
my_dict = {"a": 1, "b": 2}
my_dict["a"] = 10
print(my_dict)  # {'a': 10, 'b': 2}
```

**2. No Duplicate Keys**: Keys must be unique. Values can be duplicated.

```python
my_dict = {"a": 1, "b": 2, "a": 3}
print(my_dict)  # {'a': 3, 'b': 2}
```

**3. Unordered**: Prior to Python 3.7, order was not guaranteed.

```python
my_dict = {"b": 2, "a": 1}
print(my_dict)
```

**4. Heterogeneous**: Keys and values can be different types.

```python
my_dict = {1: "one", "two": 2, 3.0: [1, 2, 3]}
print(my_dict)
```

### Dictionary Traversal

```python
my_dict = {"a": 1, "b": 2, "c": 3}
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")
```

### Common Dictionary Methods

```python
my_dict = {"a": 1, "b": 2, "c": 3}

# keys(): Get all keys
print(my_dict.keys())  # dict_keys(['a', 'b', 'c'])

# values(): Get all values
print(my_dict.values())  # dict_values([1, 2, 3])

# items(): Get key-value pairs
print(my_dict.items())  # dict_items([('a', 1), ('b', 2), ('c', 3)])

# get(): Get value by key
value = my_dict.get("b")
print(value)  # 2

# pop(): Remove and return value
removed = my_dict.pop("c")
print(removed)  # 3
print(my_dict)  # {'a': 1, 'b': 2}

# update(): Merge dictionaries
my_dict.update({"d": 4, "e": 5})
print(my_dict)  # {'a': 1, 'b': 2, 'd': 4, 'e': 5}

# clear(): Remove all pairs
my_dict.clear()
print(my_dict)  # {}
```

## Shallow Copy vs Deep Copy

Understanding the difference between shallow and deep copies is crucial when working with nested data structures.

**Shallow Copy**: Creates a new container but references the original nested objects.

**Deep Copy**: Creates a completely independent copy, including nested objects.

```python
import copy

original_list = [1, 2, [3, 4]]

# Shallow copy
shallow = copy.copy(original_list)

# Deep copy
deep = copy.deepcopy(original_list)

# Modify nested list
original_list[2][0] = 99

print("Original:", original_list)        # [1, 2, [99, 4]]
print("Shallow:", shallow)               # [1, 2, [99, 4]]
print("Deep:", deep)                     # [1, 2, [3, 4]]
```

## Dictionary Practice Examples

### Merge Two Dictionaries

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}

# Using update()
dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 3, 'c': 4}

# Using loop
for key, value in dict2.items():
    dict1[key] = value
print(dict1)  # {'a': 1, 'b': 3, 'c': 4}
```

### Sum All Dictionary Values

```python
my_dict = {"a": 10, "b": 20, "c": 30}

# Method 1: Loop
total = 0
for value in my_dict.values():
    total += value
print("Total:", total)  # 60

# Method 2: sum() function
total = sum(my_dict.values())
print("Total:", total)  # 60
```

### Count Frequency of Elements

```python
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = {}

for element in elements:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1

print(frequency)  # {'apple': 3, 'banana': 2, 'orange': 1}
```

### Combine Two Dictionaries with Value Addition

```python
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}

combined = {}
for key in dict1.keys() | dict2.keys():
    combined[key] = dict1.get(key, 0) + dict2.get(key, 0)

print(combined)  # {'a': 400, 'b': 400, 'c': 300, 'd': 400}
```

## Summary of Data Structures

| Structure  | Ordered | Mutable | Duplicates | Key-Value | Syntax |
| ---------- | ------- | ------- | ---------- | --------- | ------ |
| List       | Yes     | Yes     | Yes        | No        | `[]`   |
| Tuple      | Yes     | No      | Yes        | No        | `()`   |
| Set        | No      | Yes     | No         | No        | `{}`   |
| Dictionary | No      | Yes     | No (keys)  | Yes       | `{}`   |

## Quick Comparison Table

Use this table to choose the right data structure for your needs:

- **Lists**: When you need ordered, mutable collections with duplicates
- **Tuples**: When you need immutable sequences (e.g., dictionary keys)
- **Sets**: When you need unique elements and don't care about order
- **Dictionaries**: When you need to associate values with unique keys
