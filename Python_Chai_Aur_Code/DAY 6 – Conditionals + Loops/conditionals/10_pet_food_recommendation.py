# Pet Food Recommendation
# Recommend a type of pet food based on the pet's species and age

pet = input("Enter pet (dog/cat): ").lower()
age = int(input("Enter pet age: "))

if pet == "dog":
    if age < 2:
        print("Puppy food")
    else:
        print("Adult dog food")

elif pet == "cat":
    if age > 5:
        print("Senior cat food")
    else:
        print("Adult cat food")
else:
    print("Unknown pet")
