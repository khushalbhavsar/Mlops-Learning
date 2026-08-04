# Apply discount if purchase > amount

purchase_amount = float(input("Enter the purchase amount: "))
if purchase_amount > 1000:
    discount = purchase_amount * 0.1
    final_amount = purchase_amount - discount
    print(f"You received a discount of {discount}. The final amount to pay is: {final_amount}")
else:
    print("No discount applied. The final amount to pay is:", purchase_amount)