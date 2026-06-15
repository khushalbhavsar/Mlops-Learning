# List Uniqueness Checker
# Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

items = ["apple", "banana", "orange", "apple", "mango"]
seen = []

for item in items:
    if item in seen:
        print("Duplicate found:", item)
        break
    seen.append(item)
