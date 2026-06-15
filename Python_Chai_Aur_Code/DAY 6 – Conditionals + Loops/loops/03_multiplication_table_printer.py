# Multiplication Table Printer
# Print the multiplication table for a given number up to 10, but skip the fifth iteration

num = 5

for i in range(1, 11):
    if i == 5:
        continue
    print(num, "x", i, "=", num * i)
