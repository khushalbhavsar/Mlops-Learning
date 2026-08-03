# What is Dictionaries in Python?
# A dictionary is a collection of key-value pairs. 
# Each key is unique and maps to a value. 
# Dictionaries are mutable, meaning you can change their content without changing their identity.

# Python Dictionary Methods - One Complete Example
# Original dictionary
student = {
    "name": "Khushal",
    "age": 22,
    "city": "Pune"
}

print("Original Dictionary:", student)

# get() -> Returns the value of a key 
print("get('name'):", student.get("name"))

# keys() -> Returns all keys
print("keys():", student.keys())

# values() -> Returns all values
print("values():", student.values())

# items() -> Returns key-value pairs
print("items():", student.items())

# update() -> Updates existing key or adds new key
student.update({"age": 23, "course": "Python"})
print("update():", student)

# pop() -> Removes and returns the specified key
removed = student.pop("city")
print("pop():", removed)
print("After pop:", student)

# popitem() -> Removes and returns the last inserted key-value pair
last_item = student.popitem()
print("popitem():", last_item)
print("After popitem():", student)

# setdefault() -> Returns value if key exists, else adds key with default value
student.setdefault("country", "India")
print("setdefault():", student)

# copy() -> Creates a shallow copy
new_student = student.copy()
print("copy():", new_student)

# clear() -> Removes all key-value pairs
new_student.clear()
print("clear():", new_student)