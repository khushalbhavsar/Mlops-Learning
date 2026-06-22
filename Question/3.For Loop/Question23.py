# - Q23: Count the number of even numbers between 1 and n

n = int(input("Enter number : "))
count = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        count += 1
print("Count of even numbers between 1 and", n, "is:", count)