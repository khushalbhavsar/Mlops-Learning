# 8. Check whether a character is vowel or consonant.

char = input("Enter a character: ").lower()
if char in 'aeiou': 
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")

# in operator checks if the character is present in the string 'aeiou'. If it is present, it means the character is a vowel; otherwise, it is a consonant.
