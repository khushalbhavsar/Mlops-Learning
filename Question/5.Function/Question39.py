# 9. Create a function where some parameters are default and some are mandatory.

def introduce(name, age=30):
    print(f"My name is {name} and I am {age} years old.")

introduce("Bob")  # This will use the default age of 30
introduce("Alice", 25)  # This will use the provided age of 25
