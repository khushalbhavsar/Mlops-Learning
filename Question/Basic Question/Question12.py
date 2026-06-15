# 12. Write a program to convert a string into an integer.

user_val = input("Enter a string to convert into an integer: ")
try:
    int_val = int(user_val) # We attempt to convert the input string into an integer. If the string is not a valid integer, it will raise a ValueError.
    print(f"The integer value of the string is: {int_val}")
except ValueError:
    print("The provided string cannot be converted into an integer.")
    