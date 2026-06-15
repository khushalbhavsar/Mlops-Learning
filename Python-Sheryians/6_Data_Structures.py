# What is Data Structures?
# Data structures are ways of organizing and storing data in a computer so that it can be accessed and modified efficiently.
# Common data structures in Python include lists, tuples, sets, and dictionaries.

print("Lists in Python")
# What is List?
# A list is an ordered collection of items that can be of different types.
# Lists are defined using square brackets [].

# Understanding so terminology related to lists:
# 1. Mutable: Lists are mutable, meaning their elements can be changed after the list is created.
# Example:
my_list = [1, 2, 3]
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3]

# 2. Duplicates: Lists can contain duplicate elements.
# Example:
my_list = [1, 2, 2, 3]
print(my_list)  # Output: [1, 2, 2, 3]

# 3. Ordered: Lists maintain the order of elements as they were added.
# Example:
my_list = [5, 3, 8]
print(my_list)  # Output: [5, 3, 8] 

# 4. Hetrogeneous: Lists can contain elements of different data types.
# Example:
my_list = [1, "hello", 3.14, True]
print(my_list)  # Output: [1, 'hello', 3.14, True]

# List Traversing and methods:
# Traversing a list means going through each element in the list one by one.
# Example:
numbers = [1, 2, 3, 4, 5]
# Traversing a list using a for loop
for num in numbers:
    print(num)
# Example accessing elements directly by index
for i in range(len(numbers)):
    print(numbers[i])

# Common List Methods:
print("Common List Methods:")
# print(dir(list))  # This will print all the methods available for list objects
# Here are some commonly used list methods with examples:
# 1. append(): Adds an element to the end of the list.
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]
# 2. remove(): Removes the first occurrence of a specified element from the list.
my_list.remove(2)
print(my_list)  # Output: [1, 3, 4]
# 3. pop(): Removes and returns the element at the specified index (default is the last element).
popped_element = my_list.pop()
print(popped_element)  # Output: 4
print(my_list)  # Output: [1, 3]
# 4. sort(): Sorts the elements of the list in ascending order.
my_list = [3, 1, 4, 2]
my_list.sort()
print(my_list)  # Output: [1, 2, 3, 4]
# 5. reverse(): Reverses the order of elements in the list.
my_list.reverse()
print(my_list)  # Output: [4, 3, 2, 1]
# 6. len(): Returns the number of elements in the list.
print(len(my_list))  # Output: 4
# 7. index(): Returns the index of the first occurrence of a specified element.
index_of_3 = my_list.index(3)
print(index_of_3)  # Output: 1
# 8. extend(): Extends the list by appending elements from another iterable (like another list).
my_list.extend([5, 6])
# 9. count(): Returns the number of occurrences of a specified element in the list.
count_of_2 = my_list.count(2)
print(count_of_2)  # Output: 1
print(my_list)  # Output: [4, 3, 2, 1, 5, 6]
# 10. clear(): Removes all elements from the list.
my_list.clear()
print(my_list)  # Output: []


print("Print positive and negative numbers from a list")
# Question: Print positive and negative numbers from a list
numbers = [10, -5, 3, -1, 0, 7, -8]
print("Positive numbers:")
for num in numbers:
    if num > 0:
        print(num)
print("Negative numbers:")
for num in numbers:
    if num < 0:
        print(num)

print("Mean of list elements")
# Question: Mean of list elements
numbers = [10, 20, 30, 40, 50]
sum = 0
for num in numbers:
    sum += num  
mean = sum / len(numbers)
print(f"Mean: {mean}")  # Output: Mean: 30.0

print("Find the greatest element and print its index too")
# Question : Find the greatest element and print its index too
numbers = [10, 25, 5, 40, 15]
greatest = numbers[0]
index_of_greatest = 0
for i in range(1, len(numbers)):
    if numbers[i] > greatest:
        greatest = numbers[i]
        index_of_greatest = i
print(f"Greatest element: {greatest} at index {index_of_greatest}")  # Output: Greatest element: 40 at index 3

print("Find the second greatest element")
# Question: Find the second greatest element
numbers = [10, 25, 5, 40, 15]
first_greatest = numbers[0] 
second_greatest = numbers[0]
for num in numbers:
    if num > first_greatest:
        second_greatest = first_greatest
        first_greatest = num
    elif first_greatest > num > second_greatest:
        second_greatest = num
print(f"Second greatest element: {second_greatest}")  # Output: Second greatest element: 25

print("Check if List is sorted or not")
# Question: Check if List is sorted or not.
numbers = [1, 2, 3, 4, 5]
is_sorted = True
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        is_sorted = False
        break
if is_sorted:
    print("The list is sorted.")
else:
    print("The list is not sorted.")

print("Tuples in Python")
# What is Tuples?
# A tuple is an ordered collection of items that can be of different types.
# Tuples are defined using parentheses ().
# Understanding so terminology related to tuples:
# 1. Immutable: Tuples are immutable, meaning their elements cannot be changed after the tuple is created.
# Example:
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # This will raise a TypeError
print(my_tuple)  # Output: (1, 2, 3)
# 2. Duplicates: Tuples can contain duplicate elements.
# Example:
my_tuple = (1, 2, 2, 3)
print(my_tuple)  # Output: (1, 2, 2, 3
# 3. Ordered: Tuples maintain the order of elements as they were added.
# Example:
my_tuple = (5, 3, 8)
print(my_tuple)  # Output: (5, 3, 8)
# 4. Hetrogeneous: Tuples can contain elements of different data types.
# Example:
my_tuple = (1, "hello", 3.14, True)
print(my_tuple)  # Output: (1, 'hello', 3.14, True)

# Tuple Traversing and methods:
print("Tuple Traversing and methods:")
# Traversing a tuple means going through each element in the tuple one by one.
# Example:
numbers = (1, 2, 3, 4, 5)
# Traversing a tuple using a for loop
for num in numbers:
    print(num)
# Example accessing elements directly by index
for i in range(len(numbers)):
    print(numbers[i])

# What is touple unpacking?
print("Tuple Unpacking:")
# Tuple unpacking is a feature in Python that allows you to assign the elements of a tuple to multiple variables in a single statement.
# Example:
my_tuple = (10, 20, 30)
a, b, c = my_tuple
print(a)  # Output: 10      
print(b)  # Output: 20
print(c)  # Output: 30

print("Common Tuple Methods")
# Common Tuple Methods:
# 1. count(): Returns the number of occurrences of a specified element in the tuple.
my_tuple = (1, 2, 2, 3)
count_of_2 = my_tuple.count(2)
print(count_of_2)  # Output: 2
# 2. index(): Returns the index of the first occurrence of a specified element.
index_of_3 = my_tuple.index(3)
print(index_of_3)  # Output: 3
# Note: Since tuples are immutable, they do not have methods like append(), remove(), pop(), sort(), reverse(), or clear().

