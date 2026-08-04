# Check whether number is 2-digit / 3-digit / 4-digit

integer = int(input("Enter a number: "))
if 10 <= integer <= 99:
    print(integer, "is a 2-digit number")
elif 100 <= integer <= 999:
    print(integer, "is a 3-digit number")
elif 1000 <= integer <= 9999:
    print(integer, "is a 4-digit number")
else:
    print(integer, "is not a 2-digit, 3-digit, or 4-digit number")