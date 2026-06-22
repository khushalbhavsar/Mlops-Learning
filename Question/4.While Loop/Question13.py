# 13. Check whether the given number is a palindrome.

number = int(input("Enter a number: "))
original_number = number  # Store the original number for comparison
reversed_number = 0
while number != 0:
    digit = number % 10  # Get the last digit of the number
    reversed_number = reversed_number * 10 + digit  # Append the digit to the reversed number
    number //= 10  # Remove the last digit from the original number
if original_number == reversed_number:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")
