# First Non-Repeated Character
# Given a string, find the first non-repeated character

text = "programming"

for char in text:
    if text.count(char) == 1:
        print("First non-repeated character:", char)
        break
