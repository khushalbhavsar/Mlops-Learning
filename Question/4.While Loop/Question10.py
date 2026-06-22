# 10. Find and print the product of all digits of a given number.

number = int(input("Enter a number: "))
product = 1
while number > 0:
    digit = number % 10
    product *= digit
    number //= 10
print(f"The product of all digits is: {product}")

# What is product of all digits of a given number?
# The product of all digits of a given number is the result of multiplying all the digits together.
# For example, if the number is 123, the product of its digits is 1 * 2 * 3 = 6.