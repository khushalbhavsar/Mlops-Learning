# - Q25: Find the sum of squares of numbers from 1 to n

n = int(input("Enter number : "))
sum = 0
for i in range(1, n + 1):
    sum += i ** 2
print(f"The sum of squares of numbers from 1 to {n} is {sum}")