# 12. Count how many numbers are present from 1 to n.

n = int(input("Enter number : "))
count = 0
for i in range(1, n + 1):
    count += 1
print(f"The count of numbers from 1 to {n} is {count}")
