# ATM withdrawal if balance sufficient

balance = 10000
amount = float(input("Enter Withdrawal Amount: "))

# Check if amount is greater than zero
if amount > 0:

    # Check if sufficient balance is available
    if amount <= balance:
        balance = balance - amount
        print("Withdrawal Successful")
        print("Remaining Balance:", balance)
    else:
        print("Insufficient Balance")

else:
    print("Invalid Withdrawal Amount")