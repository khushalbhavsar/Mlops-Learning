# 5. Create a function to find the square of a number.

def square_number(a):
    return a ** 2

a = float(input("Enter a number: "))
result = square_number(a)
print(f"The square of {a} is: {result}")
