print("Sets in Python")
# What is Sets?
# A set is an unordered collection of unique items.
# Sets are defined using curly braces {} or the set() function.
# Understanding so terminology related to sets:
# 1. Mutable: Sets are mutable, meaning their elements can be changed after the set is created.
# Example:
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}
# 2. No Duplicates: Sets cannot contain duplicate elements.
# Example:
my_set = {1, 2, 2, 3}
print(my_set)  # Output: {1, 2, 3}
# 3. Unordered: Sets do not maintain the order of elements.
# Example:
my_set = {5, 3, 8}
print(my_set)  # Output: {8, 3, 5} (order may vary)
# 4. Hetrogeneous: Sets can contain elements of different data types.
# Example:
my_set = {1, "hello", 3.14, True}
print(my_set)  # Output: {1, 3.14, 'hello', True} (order may vary)

print("Set Traversing and methods:")
# Set Traversing and methods:
# Traversing a set means going through each element in the set one by one.
# Example:
numbers = {1, 2, 3, 4, 5}
# Traversing a set using a for loop
for num in numbers:
    print(num)
print("Common Set Methods:")
# Common Set Methods:
# 1. add(): Adds an element to the set.
my_set = {1, 2, 3}
my_set.add(4)       
print(my_set)  # Output: {1, 2, 3, 4}
# 2. remove(): Removes a specified element from the set. Raises KeyError if the element is not found.
my_set.remove(2)
print(my_set)  # Output: {1, 3, 4}
# 3. discard(): Removes a specified element from the set. Does not raise an error
my_set.discard(5)  # No error even though 5 is not in the set
print(my_set)  # Output: {1, 3, 4}
# 4. pop(): Removes and returns an arbitrary element from the set.
popped_element = my_set.pop()
print(popped_element)  # Output: (an arbitrary element, e.g., 1)
print(my_set)  # Output: (remaining elements, e.g., {3, 4})
# 5. clear(): Removes all elements from the set.
my_set.clear()
print(my_set)  # Output: set()

# 6. union(): Returns a new set that is the union of two sets.
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print(union_set)  # Output: {1, 2, 3, 4, 5}
# 7. intersection(): Returns a new set that is the intersection of two sets.
intersection_set = set1.intersection(set2)
print(intersection_set)  # Output: {3}
# 8. difference(): Returns a new set that is the difference of two sets.
difference_set = set1.difference(set2)
print(difference_set)  # Output: {1, 2}
# 9. symmetric_difference(): Returns a new set that is the symmetric difference of two sets.
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}


print("Dictionaries in Python")
# What is Dictionaries?
# A dictionary is an unordered collection of key-value pairs.
# Dictionaries are defined using curly braces {} with key-value pairs separated by colons.
# Understanding so terminology related to dictionaries:
# 1. Mutable: Dictionaries are mutable, meaning their elements can be changed after the dictionary is created.
# Example:
my_dict = {"a": 1, "b": 2}
my_dict["a"] = 10
print(my_dict)  # Output: {'a': 10, 'b': 2
# 2. No Duplicate Keys: Dictionary keys must be unique. Values can be duplicated.
# Example:
my_dict = {"a": 1, "b": 2, "a": 3}
print(my_dict)  # Output: {'a': 3, 'b': 2}
# 3. Unordered: Dictionaries do not maintain the order of key-value pairs (prior to Python 3.7).
# Example:  
my_dict = {"b": 2, "a": 1}
print(my_dict)  # Output: {'b': 2, 'a': 1} (order may vary)
# 4. Hetrogeneous: Dictionary keys and values can be of different data types
# Example:
my_dict = {1: "one", "two": 2, 3.0: [1, 2, 3]}
print(my_dict)  # Output: {1: 'one', 'two': 2, 3.0: [1, 2, 3]}

print("Dictionary Traversing and methods:")
# Dictionary Traversing and methods:
# Traversing a dictionary means going through each key-value pair in the dictionary one by one.
# Example:
my_dict = {"a": 1, "b": 2, "c": 3}
# Traversing a dictionary using a for loop
for key in my_dict:
    print(f"Key: {key}, Value: {my_dict[key]}")

print("What is Shallow and Deep Copy ?")
# What is Shallow and Deep Copy ?
# Shallow Copy: A shallow copy of a collection creates a new collection object but does not create copies of nested objects. Instead, it references the original nested objects.
# Deep Copy: A deep copy of a collection creates a new collection object and recursively copies all nested objects, resulting in a completely independent copy.
# Example:
import copy
original_list = [1, 2, [3, 4]]
shallow_copied_list = copy.copy(original_list)
deep_copied_list = copy.deepcopy(original_list)
# Modifying the nested list in the original list
original_list[2][0] = 99
print("Original List:", original_list)          # Output: [1, 2, [99, 4]]
print("Shallow Copied List:", shallow_copied_list)  # Output: [1, 2, [99, 4]]
print("Deep Copied List:", deep_copied_list)      # Output: [1, 2, [3, 4]]


print("Common Dictionary Methods:")
# Common Dictionary Methods:
# 1. keys(): Returns a view object containing the keys of the dictionary.
my_dict = {"a": 1, "b": 2, "c": 3}
keys = my_dict.keys()
print(keys)  # Output: dict_keys(['a', 'b', 'c'])
# 2. values(): Returns a view object containing the values of the dictionary.
values = my_dict.values()
print(values)  # Output: dict_values([1, 2, 3])
# 3. items(): Returns a view object containing the key-value pairs of the dictionary.
items = my_dict.items()
print(items)  # Output: dict_items([('a', 1), ('b', 2), ('c', 3)])
# 4. get(): Returns the value for a specified key. If the key is not found, returns None (or a default value if provided).
value = my_dict.get("b")
print(value)  # Output: 2
# 5. pop(): Removes the specified key and returns the corresponding value.
removed_value = my_dict.pop("c")
print(removed_value)  # Output: 3
print(my_dict)  # Output: {'a': 1, 'b': 2}
# 6. update(): Updates the dictionary with key-value pairs from another dictionary or iterable of key-value pairs.
my_dict.update({"d": 4, "e": 5})
print(my_dict)  # Output: {'a': 1, 'b': 2, 'd': 4, 'e': 5}
# 7. clear(): Removes all key-value pairs from the dictionary.
my_dict.clear()
print(my_dict)  # Output: {}

print("Write a Python script to merge two Python dictionaries")
# Question: Write a Python script to merge two Python dictionaries
dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
# Merging dictionaries using a for loop
for key, value in dict2.items():
    dict1[key] = value
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}
# Merging dictionaries using the update() method
dict1.update(dict2)
print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}

print("Write a Python program to sum all the values in a dictionary")
# Write a Python program to sum all the values in a dictionary
my_dict = {"a": 10, "b": 20, "c": 30}
# 1. Using a for loop
total_sum = 0
for value in my_dict.values():
    total_sum += value
print("Total Sum:", total_sum)  # Output: Total Sum: 60
# 2. Using the sum() function
total_sum = sum(my_dict.values())
print("Total Sum:", total_sum)  # Output: Total Sum: 60


print("Count the frequency of each elementv in a list")
# Count the frequency of each element in a list
elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
frequency = {}
for element in elements:
    if element in frequency:
        frequency[element] += 1
    else:
        frequency[element] = 1
print(frequency)  # Output: {'apple': 3, 'banana': 2, 'orange': 1}


print("Write a Python program to combine two dictionary by adding values for common keys")
# Write a Python program to combine two dictionary by adding values for common keys
dict1 = {'a': 100, 'b': 200, 'c':300}
dict2 = {'a': 300, 'b': 200, 'd':400}
combined_dict = {}
for key in dict1.keys() | dict2.keys():
    combined_dict[key] = dict1.get(key, 0) + dict2.get(key, 0)
print(combined_dict)  # Output: {'a': 400, 'b': 400, 'c': 300, 'd': 400}

# Summary of Data Structures in Python
# 1. Lists: Ordered, mutable collections that allow duplicates and can contain heterogeneous elements.
# 2. Tuples: Ordered, immutable collections that allow duplicates and can contain heterogeneous elements.
# 3. Sets: Unordered, mutable collections that do not allow duplicates and can contain heterogeneous elements.
# 4. Dictionaries: Unordered, mutable collections of key-value pairs that do not allow duplicate keys and can contain heterogeneous elements.

# Quick Comparison Table
# | Data Structure | Ordered | Mutable | Allows Duplicates | Heterogeneous Elements |
# |----------------|---------|---------|-------------------|-----------------------|
# | List           | Yes     | Yes     | Yes               | Yes                   |
# | Tuple          | Yes     | No      | Yes               | Yes                   |
# | Set            | No      | Yes     | No                | Yes                   |
# | Dictionary     | No      | Yes     | No (keys)        | Yes                   |

