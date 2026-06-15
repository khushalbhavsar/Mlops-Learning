# What is Data Structures?

# Data structures are ways of organizing and storing data in a computer so that it can be accessed and modified efficiently.

# Common data structures in Python include lists, tuples, sets, and dictionaries.

# Data Structures in Python

Data structures are ways of organizing and storing data so it can be accessed and modified efficiently. Common data structures in Python include lists, tuples, sets, and dictionaries.

## Lists in Python

### What is a List?

A list is an ordered collection of items that can be of different types, defined using square brackets `[]`.

### List Characteristics

**1. Mutable**: Lists can be modified after creation.

```python
my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3]
```

**2. Duplicates**: Lists can contain duplicate elements.

```python
my_list = [1, 2, 2, 3]
print(my_list)  # Output: [1, 2, 2, 3]
```

**3. Ordered**: Lists maintain insertion order.

```python
my_list = [5, 3, 8]
print(my_list)  # Output: [5, 3, 8]
```

**4. Heterogeneous**: Lists can contain different data types.

```python
my_list = [1, "hello", 3.14, True]
print(my_list)  # Output: [1, 'hello', 3.14, True]
```

### List Traversal and Methods

```python
numbers = [1, 2, 3, 4, 5]

# Using for loop
for num in numbers:
    print(num)

# Using index
for i in range(len(numbers)):
    print(numbers[i])
```

### Common List Methods

```python
# append(): Add element to end
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

# remove(): Remove first occurrence
my_list.remove(2)
print(my_list)  # [1, 3, 4]

# pop(): Remove and return element at index
popped = my_list.pop()
print(popped, my_list)  # 4, [1, 3]

# sort(): Sort in ascending order
my_list = [3, 1, 4, 2]
my_list.sort()
print(my_list)  # [1, 2, 3, 4]

# reverse(): Reverse order
my_list.reverse()
print(my_list)  # [4, 3, 2, 1]

# len(): Length
print(len(my_list))  # 4

# index(): Find first occurrence
print(my_list.index(3))  # 1

# extend(): Add multiple elements
my_list.extend([5, 6])
print(my_list)  # [4, 3, 2, 1, 5, 6]

# count(): Count occurrences
print(my_list.count(2))  # 1

# clear(): Remove all elements
my_list.clear()
print(my_list)  # []
```

### List Practice Examples

```python
# Print positive and negative numbers
numbers = [10, -5, 3, -1, 0, 7, -8]
print("Positive:", [n for n in numbers if n > 0])
print("Negative:", [n for n in numbers if n < 0])

# Find mean
numbers = [10, 20, 30, 40, 50]
mean = sum(numbers) / len(numbers)
print(f"Mean: {mean}")  # 30.0

# Find greatest element and index
numbers = [10, 25, 5, 40, 15]
greatest = max(numbers)
index = numbers.index(greatest)
print(f"Greatest: {greatest} at index {index}")

# Find second greatest
numbers = [10, 25, 5, 40, 15]
first = numbers[0]
second = numbers[0]
for num in numbers:
    if num > first:
        second = first
        first = num
    elif first > num > second:
        second = num
print(f"Second greatest: {second}")

# Check if sorted
numbers = [1, 2, 3, 4, 5]
is_sorted = all(numbers[i] <= numbers[i+1] for i in range(len(numbers)-1))
print(f"Is sorted: {is_sorted}")
```

## Tuples in Python

### What is a Tuple?

A tuple is an ordered, immutable collection of items, defined using parentheses `()`.

### Tuple Characteristics

**1. Immutable**: Cannot be changed after creation.

```python
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This raises TypeError
print(my_tuple)
```

**2. Duplicates**: Can contain duplicates.

```python
my_tuple = (1, 2, 2, 3)
print(my_tuple)
```

**3. Ordered**: Maintains insertion order.

```python
my_tuple = (5, 3, 8)
print(my_tuple)
```

**4. Heterogeneous**: Can contain different types.

```python
my_tuple = (1, "hello", 3.14, True)
print(my_tuple)
```

### Tuple Unpacking

```python
my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a, b, c)  # 10 20 30
```

### Common Tuple Methods

```python
my_tuple = (1, 2, 2, 3)

# count(): Count occurrences
print(my_tuple.count(2))  # 2

# index(): Find index
print(my_tuple.index(3))  # 3
```

**Note**: Tuples don't have methods like append(), remove(), pop(), sort(), etc.

## Sets in Python

### What is a Set?

A set is an unordered collection of unique items, defined using curly braces `{}`.

### Set Characteristics

```python
# Mutable
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)

# No duplicates
my_set = {1, 2, 2, 3}
print(my_set)  # {1, 2, 3}

# Unordered
my_set = {5, 3, 8}
print(my_set)  # Order may vary

# Heterogeneous
my_set = {1, "hello", 3.14, True}
print(my_set)
```

### Common Set Methods

```python
my_set = {1, 2, 3}

# add(): Add element
my_set.add(4)

# remove(): Remove element (raises KeyError if not found)
my_set.remove(2)

# discard(): Remove without error
my_set.discard(5)

# pop(): Remove arbitrary element
my_set.pop()

# clear(): Remove all
my_set.clear()

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))                    # {1, 2, 3, 4, 5}
print(set1.intersection(set2))             # {3}
print(set1.difference(set2))               # {1, 2}
print(set1.symmetric_difference(set2))     # {1, 2, 4, 5}
```

## Dictionaries in Python

### What is a Dictionary?

A dictionary is an unordered collection of key-value pairs, defined using curly braces with colons `{}`.

### Dictionary Characteristics

```python
# Mutable
my_dict = {"a": 1, "b": 2}
my_dict["a"] = 10
print(my_dict)  # {'a': 10, 'b': 2}

# No duplicate keys
my_dict = {"a": 1, "b": 2, "a": 3}
print(my_dict)  # {'a': 3, 'b': 2}

# Unordered
my_dict = {"b": 2, "a": 1}
print(my_dict)

# Heterogeneous values
my_dict = {1: "one", "two": 2, 3.0: [1, 2, 3]}
print(my_dict)
```

### Traversing Dictionaries

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
print(my_dict.get("b"))  # 2

# pop(): Remove and return value
print(my_dict.pop("c"))  # 3

# update(): Merge dictionaries
my_dict.update({"d": 4, "e": 5})
print(my_dict)

# clear(): Remove all
my_dict.clear()
```

## Shallow Copy vs Deep Copy

```python
import copy

original_list = [1, 2, [3, 4]]
shallow = copy.copy(original_list)
deep = copy.deepcopy(original_list)

original_list[2][0] = 99
print("Original:", original_list)        # [1, 2, [99, 4]]
print("Shallow:", shallow)               # [1, 2, [99, 4]]
print("Deep:", deep)                     # [1, 2, [3, 4]]
```

## Dictionary Examples

### Merge Dictionaries

```python
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
dict1.update(dict2)
print(dict1)  # {'a': 1, 'b': 3, 'c': 4}
```

### Sum All Dictionary Values

```python
my_dict = {"a": 10, "b": 20, "c": 30}
total = sum(my_dict.values())
print(f"Total: {total}")  # 60
```

### Count Frequency of Elements

```python
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = {}
for element in elements:
    frequency[element] = frequency.get(element, 0) + 1
print(frequency)  # {'apple': 3, 'banana': 2, 'orange': 1}
```

### Combine Dictionaries with Value Addition

```python
dict1 = {'a': 100, 'b': 200, 'c': 300}
dict2 = {'a': 300, 'b': 200, 'd': 400}
combined = {}
for key in dict1.keys() | dict2.keys():
    combined[key] = dict1.get(key, 0) + dict2.get(key, 0)
print(combined)  # {'a': 400, 'b': 400, 'c': 300, 'd': 400}
```

## Quick Comparison Table

| Structure  | Ordered | Mutable | Duplicates | Syntax |
| ---------- | ------- | ------- | ---------- | ------ |
| List       | Yes     | Yes     | Yes        | `[]`   |
| Tuple      | Yes     | No      | Yes        | `()`   |
| Set        | No      | Yes     | No         | `{}`   |
| Dictionary | No      | Yes     | No (keys)  | `{}`   |
