# 11. Count and print the total number of digits in a given number.

number = int(input("Enter a number: "))
count = 0
while number != 0:
    number //= 10 # Remove the last digit from the number
    count += 1 # Increment the count for each digit removed 
print(f"The total number of digits in the given number is: {count}")