# 10. Create a shopping bill calculator with a default discount.

def calculate_bill(total_amount, discount=0.1):
    discounted_amount = total_amount * (1 - discount)
    return discounted_amount

total_amount = float(input("Enter the total amount: "))
discounted_bill = calculate_bill(total_amount)  
print(f"The total bill after applying a default discount of 10% on {total_amount} is: {discounted_bill}")

