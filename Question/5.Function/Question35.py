# 5. Create a function to print a default country.

def print_country(country="USA"):
    print(f"The default country is: {country}")

country = input("Enter a country (or press Enter to use the default): ")
if country:
    print_country(country)
else:
    print_country()  # This will use the default country "USA"

    