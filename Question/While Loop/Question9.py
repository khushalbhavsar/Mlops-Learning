# 9. Calculate and print the factorial of a given number.

n = int(input("Enter a natural number: "))
factorial = 1   
count = 1
while count <= n:
    factorial *= count
    count += 1
print(f"The factorial of {n} is: {factorial}")

# Example: If the user inputs 5, the output will be "The factorial of 5 is: 120" since 5! = 5 × 4 × 3 × 2 × 1 = 120.