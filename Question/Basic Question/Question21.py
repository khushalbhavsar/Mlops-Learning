# 21. Reverse a string using slicing.

my_string = "Hello, World!"
reversed_string = my_string[::-1] # This slicing syntax reverses the string
print(f"The reversed string is: {reversed_string}")


# Example input: "Hello, World!"
# Example output: "!dlroW ,olleH"

# Explanation:
# The slicing syntax `[::-1]` means:
# - Start from the end of the string (indicated by the empty start index).
# - Move backwards through the string (indicated by the step of -1).
# This effectively reverses the string, as it takes characters from the end to the beginning.


