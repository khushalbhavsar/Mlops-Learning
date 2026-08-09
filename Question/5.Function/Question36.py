# 6. Create a function to print a default city.

def print_city(city="New York"):
    print(f"The default city is: {city}")

city = input("Enter a city (or press Enter to use the default): ")
if city:
    print_city(city)
else:
    print_city()  # This will use the default city "New York"
    