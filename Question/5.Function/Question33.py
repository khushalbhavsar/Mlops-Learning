# 3. Create a function to calculate tax with a default tax rate.

def calculate_tax(amount, tax_rate=0.05):
    return amount * tax_rate

amount = float(input("Enter the amount: "))
tax = calculate_tax(amount)
print(f"The tax for the amount {amount} at a tax rate of 5% is: {tax}")
