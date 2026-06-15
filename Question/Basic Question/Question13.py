# 13. Write a program to convert an integer into a string.

user_val = input("Enter an integer to convert into a string: ")
try:
    int_val = int(user_val) # First, we attempt to convert the input into an integer to ensure it's a valid integer.
    str_val = str(int_val) # Then, we convert the integer back into a string.
    print(f"The string value of the integer is: '{str_val}'")
except ValueError:
    print("The provided input is not a valid integer and cannot be converted into a string.")
    