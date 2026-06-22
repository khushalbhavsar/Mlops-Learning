# 17. Calculate the average of elements in a list using a `for` loop.

n = int(input("Enter the number of elements in the list: "))
numbers = []
for i in range(n):
    num = float(input(f"Enter element {i + 1}: "))
    numbers.append(num)
    total = 0
    for num in numbers:
        total += num
        average = total / n
print(f"The average of the elements in the list is: {average}")