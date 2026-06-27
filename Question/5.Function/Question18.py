# 8. Create a function to calculate simple interest.

def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest (in %): "))
time = float(input("Enter the time (in years): "))
simple_interest = calculate_simple_interest(principal, rate, time)
print(f"The simple interest for a principal of {principal}, rate of {rate}%, and time of {time} years is: {simple_interest}")
