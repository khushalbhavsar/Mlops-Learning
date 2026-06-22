# - Q30: Check whether a number is an Armstrong number using a for loop

# An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits raised to the power of the number of digits. For example, 153 is an Armstrong number because 1^3 + 5^3 + 3^3 = 153.

n = int(input("Enter a number: "))
num_str = str(n) 
num_digits = len(num_str)
armstrong_sum = 0
for digit in num_str:
    armstrong_sum += int(digit) ** num_digits
if armstrong_sum == n:
    print(f"{n} is an Armstrong number.")
else:
    print(f"{n} is not an Armstrong number.")
