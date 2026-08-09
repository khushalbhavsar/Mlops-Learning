# 2. Create a function with default age = 18.

def print_name_age(name, age=18):
    print(f"Name: {name}, Age: {age}")

name = input("Enter your name: ")
age_input = input("Enter your age (press Enter to use default age 18): ")
if age_input:
    age = int(age_input)
    print_name_age(name, age)
else:
    print_name_age(name)  # This will use the default age of 18

    