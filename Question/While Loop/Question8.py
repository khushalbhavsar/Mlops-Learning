# 8. Calculate the sum of all odd numbers from 1 up to n.

n = int(input("Enter a natural number: "))
sum_odd = 0
count = 1
while count <= n:
    if count % 2 != 0:
        sum_odd += count
    count += 1
print(f"The sum of all odd numbers from 1 to {n} is: {sum_odd}")
