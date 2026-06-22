# - Q21: Print all numbers from 1 to n that are divisible by 2

n = int(input("Enter number : "))
for i in range(1, n + 1 ):
    if i % 2 == 0:
        print(i)