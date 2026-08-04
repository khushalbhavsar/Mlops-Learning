# Check whether number ends with 5

number = int(input("Enter a number: "))
if number % 10 == 5: # number % 10 returns the last digit 
    print(number, "ends with 5")
else:
    print(number, "does not end with 5")

