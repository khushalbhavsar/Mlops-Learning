# 4. Create a function to calculate interest with a default rate.

def calculate_interest(principal, rate=0.05, time=1):
    return principal * rate * time

principal = float(input("Enter the principal amount: "))
time = float(input("Enter the time (in years): "))
interest = calculate_interest(principal, time=time)
print(f"The interest for a principal of {principal} at a rate of 5% over {time} years is: {interest}")

