# Check if number divisible by 2 and 5

input_number = int(input("Enter a number: "))
if input_number % 2 == 0 and input_number % 5 == 0:
    print("The number is divisible by both 2 and 5.")
elif input_number % 2 == 0:
    print("The number is divisible by 2 but not by 5.")
elif input_number % 5 == 0:
    print("The number is divisible by 5 but not by 2.")
else:
    print("The number is not divisible by either 2 or 5.")