# 7. Calculate the sum of all even numbers from 1 up to n.

n = int(input("Enter a natural number: "))
sum_even = 0
count = 1
while count <= n:
    if count % 2 == 0:
        sum_even += count
    count += 1  
print(f"The sum of all even numbers from 1 to {n} is: {sum_even}")
