# Fruit Ripeness Checker (Banana Example)
# Determine if a fruit is ripe, overripe, or unripe based on its color

color = input("Enter banana color: ").lower()

if color == "green":
    print("Unripe")
elif color == "yellow":
    print("Ripe")
elif color == "brown":
    print("Overripe")
else:
    print("Unknown color")
