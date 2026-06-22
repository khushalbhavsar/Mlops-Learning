# 12. Reverse the given number and print the reversed value.

number = int(input("Enter a number: "))
reversed_number = 0
while number != 0:
    digit = number % 10  # Get the last digit of the number
    reversed_number = reversed_number * 10 + digit  # Append the digit to the reversed number
    number //= 10  # Remove the last digit from the original number
print(f"The reversed number is: {reversed_number}")