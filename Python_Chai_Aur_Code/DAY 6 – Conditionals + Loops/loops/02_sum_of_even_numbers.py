# Sum of Even Numbers
# Calculate the sum of even numbers up to a given number n

n = 10
total = 0

for i in range(1, n + 1):
    if i % 2 == 0:
        total += i

print("Sum of even numbers:", total)
