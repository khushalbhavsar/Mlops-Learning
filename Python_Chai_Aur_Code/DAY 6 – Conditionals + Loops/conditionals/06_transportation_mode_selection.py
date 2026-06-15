# Transportation Mode Selection
# Choose a mode of transportation based on the distance (<3 km: Walk, 3-15 km: Bike, >15 km: Car)

distance = float(input("Enter distance in km: "))

if distance < 3:
    print("Walk")
elif distance <= 15:
    print("Bike")
else:
    print("Car")
