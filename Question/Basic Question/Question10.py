# 10. Write a program to swap two variables without using a third variable.

# Get input from the user
a = input("Enter the first variable (a): ")
b = input("Enter the second variable (b): ")
# Display original values
print(f"Before swapping: a = {a}, b = {b}")
# Swap without using a third variable
a, b = b, a
# Display swapped values
print(f"After swapping: a = {a}, b = {b}")

