
print("Welcome to the day trip planner, where your dream vacation is made for you!")
user_input = input("Do you want to start planning your trip? ")

if user_input == "yes":
    print("Okay, let's begin!")
else:
    print("Okay, maybe next time.")

import random
destinations = [ "Louisiana", "Texas", "California", "Chicago"]
restaruants = [ "Hometown Buffet", "Al's BBQ", "Kitchen Story", "Chi-Town Pizza"]
mode_of_transportation = [ "Plane", "Train", "Boat", "Cab"]
entertainment = ["Theatre", "Football game", "Haunted house", "Night club"]

randomly_generated_destination = random.choice(destinations)
print(f"We have selected for you {randomly_generated_destination}")

randomly_generated_restaruants = random.choice(restaruants)
print(f"We have selected for you {randomly_generated_restaruants}")

randomly_generated_transportation = random.choice(mode_of_transportation)
print(f"We have selected for you a {randomly_generated_transportation}")

randomly_generated_entertainment = random.choice(entertainment)
print(f"We have selected for you a {randomly_generated_entertainment}")
