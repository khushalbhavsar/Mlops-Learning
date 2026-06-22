# - Q26: Find the sum of cubes of numbers from 1 to n

n = int(input("Enter the number : "))
sum = 0
for i in range(1, n + 1):
    sum += i ** 3
print(f"The sum of cubes of numbers from 1 to {n} is {sum}")