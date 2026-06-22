# 20. Count the number of digits, alphabets, and special characters in a string.

input_string = input("Enter a string: ")
digit_count = 0
alphabet_count = 0
special_char_count = 0
for char in input_string:
    if char.isdigit():
        digit_count += 1
    elif char.isalpha():
        alphabet_count += 1
    else:
        special_char_count += 1
print(f"Number of digits: {digit_count}")
print(f"Number of alphabets: {alphabet_count}")
print(f"Number of special characters: {special_char_count}")
