# Factorial Calculator
# Compute the factorial of a number using a while loop

num = 5
factorial = 1

while num > 0:
    factorial *= num
    num -= 1

print("Factorial:", factorial)
