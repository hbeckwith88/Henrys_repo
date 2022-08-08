def welcome_message():
    print("Welcome to the day trip planner, where your dream vacation is made for you!")
    user_input = input("Do you want to start planning your trip? ")

    if user_input == "yes":
        print("Okay, let's begin!")
    else:
        print("Okay, maybe next time.")



from cProfile import run
import random
destinations = [ "Louisiana", "Texas", "California", "Chicago"]
restaruants = [ "Hometown Buffet", "Al's BBQ", "Kitchen Story", "Chi-Town Pizza"]
mode_of_transportation = [ "Plane", "Train", "Boat", "Cab"]
entertainment = ["Theatre Performance", "Football game", "Haunted house", "Night club"]

def randomly_generated_destination():
    randomly_generated_destination = random.choice(destinations)
    return randomly_generated_destination

def randomly_generated_restaruants():
    randomly_generated_restaruants = random.choice(restaruants)
    return randomly_generated_restaruants

def randomly_generated_transportation():
    randomly_generated_transportation = random.choice(mode_of_transportation)
    return randomly_generated_transportation

def randomly_generated_fun():
    randomly_generated_entertainment = random.choice(entertainment)
    return randomly_generated_entertainment

welcome_message()
final_destination = ""
rgd = randomly_generated_destination()
user_input = input(f"We selected for you {rgd}. Do you like this destination? y/n ")
if user_input == "yes":
    final_destination = rgd
while user_input != "yes":
    rgd = randomly_generated_destination()
    user_input = input(f"Okay what about this location: {rgd} ")
    if user_input == "yes":
        final_destination = rgd
print(f"Your selected destination is {final_destination}! ")

final_restaruants = ""
rgr = randomly_generated_restaruants()
user_input = input(f"We selected for you {rgr}. Do you like this restaruant? y/n ")
if user_input == "yes":
    final_restaruants = rgr
while user_input != "yes":
    rgr = randomly_generated_restaruants()
    user_input = input(f"Okay what about this restaruant: {rgr} ")
    if user_input == "yes":
        final_restaruants = rgr
print(f"Your selected restaruant is {final_restaruants}! ")

final_transportation = ""
rgt = randomly_generated_transportation()
user_input = input(f"We selected for you a {rgt}. Do you like this form of transportation? y/n ")
if user_input == "yes":
    final_transportation = rgt
while user_input != "yes":
    rgt = randomly_generated_transportation()
    user_input = input(f"Okay what about this form of transportation: {rgt} ")
    if user_input == "yes":
        final_transportation = rgt
print(f"Your selected form of transprtation is a {final_transportation}! ")

final_fun = ""
rgf = randomly_generated_fun()
user_input = input(f"We selected this for your a {rgf}. Do you like this entertainment? y/n ")
if user_input == "yes":
    final_fun = rgf
while user_input != "yes":
    rgf = randomly_generated_fun()
    user_input = input(f"Okay what this about for entertainment: {rgf} ")
    if user_input == "yes":
        final_fun = rgf
print(f"Your selected entertainment is a {final_fun}! ")

print(f"Here if your completed trip!!! You'll be going to {final_destination},  you'll be eating at {final_restaruants}, you'll be traveling by way of {final_transportation}, and for entertainment, you'll go to a {final_fun}. Have fun on your trip!!!")








