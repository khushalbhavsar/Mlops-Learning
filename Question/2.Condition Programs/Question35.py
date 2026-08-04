# Employee promotion eligibility

years_of_experience = int(input("Enter your years of experience: "))
rating = float(input("Enter your performance rating (out of 5): "))

if years_of_experience >= 5:
    if rating >= 4.0:
        print("You are eligible for promotion!")
    else:
        print("You are not eligible for promotion due to low performance rating.")

else:
    print("You are not eligible for promotion due to insufficient years of experience.")

    
