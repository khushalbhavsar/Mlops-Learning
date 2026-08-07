# Create a bank balance program using a global variable.

def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited: ${amount}. New balance: ${balance}")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds.")
    else:
        balance -= amount
        print(f"Withdrew: ${amount}. New balance: ${balance}")

# Initialize the global variable
