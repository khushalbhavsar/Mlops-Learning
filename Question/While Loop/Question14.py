# 14. Find and print the sum of digits of the given number.

number = int(input("Enter a number: "))
sum_of_digits = 0
while number != 0:
    digit = number % 10  # Get the last digit of the number
    sum_of_digits += digit  # Add the digit to the sum
    number //= 10  # Remove the last digit from the original number
print(f"The sum of digits of the given number is: {sum_of_digits}")