# 28. Remove duplicate values from a list using a set.

my_list = [1, 2, 3, 4, 4, 5, 5, 6]
unique_values = set(my_list) # A set automatically removes duplicate values
unique_list = list(unique_values) # Convert the set back to a list if needed
print(unique_list) # This will print the list with duplicates removed, e.g. [1, 2, 3, 4, 5, 6]

