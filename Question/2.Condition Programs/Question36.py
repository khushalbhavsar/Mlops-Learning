# Check number between two ranges

input_number = int(input("Enter a number: "))
if 10 <= input_number <= 20:
    print("The number is between 10 and 20.")
elif 30 <= input_number <= 40:
    print("The number is between 30 and 40.")
elif 50 <= input_number <= 60:
    print("The number is between 50 and 60.")
else:
    print("The number is not in any of the specified ranges.")