# 15. Find the largest number in a list using a `for` loop.

num = [11, 12, 13, 15, 14]
largest = 0
for i in num:
    if i > largest:
        largest = i
print(f"The largest number in the list is {largest}")