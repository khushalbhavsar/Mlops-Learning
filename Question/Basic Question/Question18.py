# 18. Write a program to create a list and add an element using `append()`.

my_list = []  # We start with an empty list.
print(f"Initial list: {my_list}")
element_to_add = input("Enter an element to add to the list: ")
my_list.append(element_to_add)  # We use the append() method to add the element
print(f"Updated list after appending: {my_list}")

