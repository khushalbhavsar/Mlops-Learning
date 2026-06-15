# 9. Check whether a character is uppercase or lowercase.

char = input("Enter a character: ")
if char.isupper():
    print(f"{char} is an uppercase character.")
elif char.islower():
    print(f"{char} is a lowercase character.")

# isupper() method returns True if all characters in the string are uppercase, otherwise it returns False.
# islower() method returns True if all characters in the string are lowercase, otherwise it returns False.