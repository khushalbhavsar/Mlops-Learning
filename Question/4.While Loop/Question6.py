# 6. Calculate and print the sum of the first n natural numbers.

n = int(input("Enter a natural number: "))
sum_natural = 0
count = 1
while count <= n:
    sum_natural += count
    count += 1
print(f"The sum of the first {n} natural numbers is: {sum_natural}")
