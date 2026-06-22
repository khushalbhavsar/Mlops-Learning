# 19. Count the number of vowels in a string.

input_string = input("Enter a string: ")
vowel_count = 0
for char in input_string:
    if char.lower() in 'aeiou':
        vowel_count += 1
print(f"The number of vowels in the string is: {vowel_count}")