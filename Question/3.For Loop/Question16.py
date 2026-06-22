# 16. Find the smallest number in a list using a `for` loop.

num = [11, 12, 13, 15, 14]
smallest = num[0]  # Initialize smallest to the first element of the list
for i in num:
    if i < smallest:
        smallest = i
print(f"The smallest number in the list is {smallest}")