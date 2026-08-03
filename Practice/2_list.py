# What is a list in Python?
# A list is a collection of items that can be of different data types. Lists are mutable, meaning you can change their content without changing their identity.

# Python List Methods - One Complete Example
# Original list
numbers = [10, 20, 30]
print("Original List:", numbers)

# append() -> Adds one element at the end
numbers.append(40)
print("append():", numbers)

# extend() -> Adds multiple elements
numbers.extend([50, 60])
print("extend():", numbers)

# insert() -> Inserts an element at a specific index
numbers.insert(2, 25)
print("insert():", numbers)

# remove() -> Removes the first matching value
numbers.remove(25)
print("remove():", numbers)

# pop() -> Removes and returns an element (last by default)
removed = numbers.pop()
print("pop():", removed)
print("After pop:", numbers)

# sort() -> Sorts the list in ascending order
numbers.sort()
print("sort():", numbers)

# reverse() -> Reverses the list
numbers.reverse()
print("reverse():", numbers)

# index() -> Returns the index of the first matching value
print("index(30):", numbers.index(30))

# count() -> Counts occurrences of a value
numbers.append(20)
print("count(20):", numbers.count(20))

# copy() -> Creates a shallow copy of the list
new_list = numbers.copy()
print("copy():", new_list)

# clear() -> Removes all elements from the list
new_list.clear()
print("clear():", new_list)

# Find the largest element in a list.
list1 = [10, 20, 30, 40, 50]
largest = max(list1)
print("Largest element in the list:", largest)

# Find the smallest element in a list.
list1 = [10, 20, 30, 40, 50]
smallest = min(list1)
print("Smallest element in the list:", smallest)

# Remove duplicate elements.
list2 = [1, 2, 3, 2, 4, 1, 5]
unique_list = list(set(list2))
print("List with unique elements:", unique_list)

# Reverse a list.
list3 = [1, 2, 3, 4, 5]
list3.reverse()
print("Reversed list:", list3)

# Sort a list in ascending order.
list4 = [5, 2, 8, 1, 9]
list4.sort()
print("List sorted in ascending order:", list4)

# Sort a list in descending order.
list5 = [5, 2, 8, 1, 9]
list5.sort(reverse=True)
print("List sorted in descending order:", list5)

# Find the second largest element.
list6 = [5, 2, 8, 1, 9]
list6.sort(reverse=True)
second_largest = list6[1]
print("Second largest element:", second_largest)

# Merge two lists.
list7 = [1, 2, 3]
list8 = [4, 5, 6]
merged_list = list7 + list8
print("Merged list:", merged_list)

# Count occurrences of an element.
list9 = [1, 2, 3, 2, 4, 2, 5]
count = list9.count(2)
print("Occurrences of 2:", count)

# Remove a specific element from a list.
list10 = [1, 2, 3, 4, 5]
list10.remove(3)
print("List after removing 3:", list10)
