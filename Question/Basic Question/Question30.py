# 30. Find the power of a number using `pow()`.

base = float(input("Enter the base number: ")) # Get the base number from the user
exponent = float(input("Enter the exponent: ")) # Get the exponent from the user
result = pow(base, exponent) # The `pow()` function calculates the power of the base raised to the exponent
print(f"{base} raised to the power of {exponent} is {result}") # This will print the result of the power calculation, e.g. "2.0 raised to the power of 3.0 is 8.0"

