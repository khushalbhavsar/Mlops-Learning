# 6. Create a function to find the cube of a number.

def cube_number(a):
    return a ** 3   

a = float(input("Enter a number: "))
result = cube_number(a)
print(f"The cube of {a} is: {result}")