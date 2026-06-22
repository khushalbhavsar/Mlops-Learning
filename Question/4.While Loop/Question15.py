# 15. Check whether the given number is an Armstrong number.

number = int(input("Enter a number: "))
# Calculate the number of digits in the number
num_digits = 0
temp = number
while temp != 0:
    temp //= 10
    num_digits += 1

# Check if the number is an Armstrong number
temp = number
armstrong_sum = 0
while temp != 0:
    digit = temp % 10
    armstrong_sum += digit ** num_digits
    temp //= 10

if number == armstrong_sum:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")