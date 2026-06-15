# Write a program to find the largest of three numbers.

num1 = float(input("Enter value num1: "))
num2 = float(input("Enter value num2: "))
num3 = float(input("Enter value num3: "))

if(num1 > num2) and (num1 > num3):
    largest = num1
elif(num2 > num1) and (num2 > num3):
    largest = num2
else:
    largest = num3

print("The largest number is ", largest)