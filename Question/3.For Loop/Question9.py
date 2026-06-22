# 9. Find the sum of odd numbers from 1 to n.

n = int(input("Enter number: "))
total = 0
for i in range(1, n + 1):
    if i % 2 != 0:
        total += i
print(f"The sum of odd numbers from 1 to {n} is {total}")