# - Q28: Find the sum of digits of a number

n = int(input("Enter a number: "))
sumofdigits = 0
for digit in str(n):
    sumofdigits += int(digit)
print(f"The sum of digits of the given number is {sumofdigits}")