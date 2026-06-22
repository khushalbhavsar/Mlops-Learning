# 10. Check whether a number is zero, positive, or negative.

num = float(input("Enter a number: "))
if num == 0:
    print(f"{num} is zero.")
elif num > 0:
    print(f"{num} is a positive number.")
else:
    print(f"{num} is a negative number.")