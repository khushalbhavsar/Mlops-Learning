# Coffee Customization
# Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso

size = input("Enter size (Small/Medium/Large): ").lower()
extra_shot = input("Extra shot? (yes/no): ").lower()

print("Coffee size:", size.capitalize())

if extra_shot == "yes":
    print("With extra espresso shot")
else:
    print("No extra shot")
