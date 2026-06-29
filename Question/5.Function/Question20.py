# 10. Create a function to swap two numbers.

def swap_numbers(a, b):
    return b, a

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num1, num2 = swap_numbers(num1, num2)
print(f"After swapping: First number is {num1}, Second number is {num2}")

