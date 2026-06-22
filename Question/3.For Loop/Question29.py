# - Q29: Count the number of digits in a number

n = int(input("Enter a number: "))
count = 0
for i in str(n):
    count += 1
print(f"The number of digits in the given number is {count}")