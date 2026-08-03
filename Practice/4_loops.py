# What is loops in Python?
# Loops are used to execute a block of code repeatedly as long as a specified condition is true. 
# Python provides two types of loops: for loops and while loops.

# What is a for loop in Python?
# A for loop is used to iterate over a sequence (like a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence.

# What is a while loop in Python?
# A while loop is used to execute a block of code as long as a specified condition is true. 
# The loop will continue until the condition becomes false.

# Python Loops - One Complete Example

# -------------------------------
# for loop -> Iterates over a sequence
# -------------------------------
numbers = [10, 20, 30, 40, 50]

print("for loop:")
for num in numbers:
    print(num)

# -------------------------------
# range() -> Generates a sequence of numbers
# -------------------------------
print("\nrange(5):")
for i in range(5):
    print(i)

# -------------------------------
# range(start, stop)
# -------------------------------
print("\nrange(1, 6):")
for i in range(1, 6):
    print(i)

# -------------------------------
# range(start, stop, step)
# -------------------------------
print("\nrange(0, 11, 2):")
for i in range(0, 11, 2):
    print(i)

# -------------------------------
# enumerate() -> Returns index and value
# -------------------------------
print("\nenumerate():")
fruits = ["Apple", "Banana", "Mango"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

# -------------------------------
# zip() -> Iterates over multiple lists together
# -------------------------------
print("\nzip():")
names = ["Ram", "Shyam", "Amit"]
marks = [80, 90, 85]

for name, mark in zip(names, marks):
    print(name, mark)

# -------------------------------
# break -> Exits the loop immediately
# -------------------------------
print("\nbreak:")
for i in range(1, 6):
    if i == 3:
        break
    print(i)

# -------------------------------
# continue -> Skips the current iteration
# -------------------------------
print("\ncontinue:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# -------------------------------
# pass -> Placeholder (does nothing)
# -------------------------------
print("\npass:")
for i in range(3):
    if i == 1:
        pass
    print(i)

# -------------------------------
# else with for -> Executes if loop finishes normally
# -------------------------------
print("\nfor-else:")
for i in range(3):
    print(i)
else:
    print("Loop Completed")

# -------------------------------
# Nested for loop -> Loop inside another loop
# -------------------------------
print("\nNested for loop:")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"({i},{j})", end=" ")
    print()


# Print numbers from 1 to 100.
for i in range(1, 101):
    print("Print 1 to 100 : ", i)

# Print even numbers.
for i in range(2, 101, 2):
    print("Even number : ", i)

# Print odd numbers.
for i in range(1, 101, 2):
    print("Odd number : ", i)

# Print the multiplication table.
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

# Find the sum of numbers from 1 to N.
N = int(input("Enter a number: "))
sum = 0
for i in range(1, N+1):
    sum += i
print("Sum of numbers from 1 to", N, "is", sum)

# Find the factorial of a number.   
N = int(input("Enter a number: "))
factorial = 1
for i in range(1, N+1):
    factorial *= i
print("Factorial of", N, "is", factorial)
