# Lists for destinations, resturants, modes of transportation, and entertainment
destination_choices = ["Hawaii", "Fiji", "Tulum", "Barbados"]
resturant_choices = ["Italian", "Mexican", "Bbq", "Seafood"]
mode_of_transportation = ["Car", "Bus", "Train", "Scooters"]
form_of_entertainment = ["Concert", "Hiking", "Water Park", "Sightseeing"]

# Greeting
def welcome_user():
     print("Welcome to the Day Trip Generator! Lets begin planning your trip?")

# Generate random selections
import random
def give_destination():
     random_destination = random.choice(destination_choices)
     print(f"We have chosen {random_destination} for your destination! Does this sound good? Enter y/n:")
     return random_destination
     
def give_resturant():
     random_resturant = random.choice(resturant_choices)
     print(random_resturant)
     return random_resturant

def give_transportation():
     random_mode_of_transportation = random.choice(mode_of_transportation)
     print(random_mode_of_transportation)
     return random_mode_of_transportation

def give_entertainment():
     random_form_of_entertainment = random.choice(form_of_entertainment)
     print(random_form_of_entertainment)
     return random_form_of_entertainment

welcome_user()
give_destination()