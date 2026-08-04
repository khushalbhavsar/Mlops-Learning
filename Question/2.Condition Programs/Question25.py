# Calculate electricity bill based on units

# Input -> Read the number of electricity units consumed
units = int(input("Enter Units Consumed: "))

# If units are 100 or less
# Charge ₹5 per unit
if units <= 100:
    bill = units * 5

# If units are between 101 and 300
# First 100 units = ₹5 per unit
# Remaining units = ₹7 per unit
elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 7)

# If units are above 300
# First 100 units = ₹5 per unit
# Next 200 units = ₹7 per unit
# Remaining units = ₹10 per unit
else:
    bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)

# Display the total electricity bill
print("Electricity Bill:", bill)