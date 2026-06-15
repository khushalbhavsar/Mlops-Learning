# Weather Activity Suggestion
# Suggest an activity based on the weather

weather = input("Enter weather: ").lower()

if weather == "sunny":
    print("Go for a walk")
elif weather == "rainy":
    print("Read a book")
elif weather == "snowy":
    print("Build a snowman")
else:
    print("Stay indoors")
