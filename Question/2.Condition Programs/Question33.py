# Ticket booking age + seat availability check

age = int(input("Enter your age: "))
available_seats = 5

if age >= 18:
    if available_seats > 0:
        print("Ticket booked successfully!")
        available_seats -= 1
        print("Remaining seats:", available_seats)
    else:
        print("No seats available.")
else:
    print("You must be at least 18 years old to book a ticket.")
