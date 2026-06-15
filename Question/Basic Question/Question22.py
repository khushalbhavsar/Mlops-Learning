# 22. Extract the first 5 characters from a string.

my_string = "Hello, World!"
first_five_characters = my_string[:5] # This slicing syntax extracts the first 5 characters
print(f"The first 5 characters of the string are: {first_five_characters}")

# Example input: "Hello, World!"
# Example output: "Hello"
# Explanation:
# The slicing syntax `[:5]` means:
# - Start from the beginning of the string (indicated by the empty start index).
# - Take characters up to, but not including, index 5 (which is the 6th character).
# This effectively extracts the first 5 characters of the string.
