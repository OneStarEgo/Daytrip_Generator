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
     print(f"We have chosen {random_resturant} for your resturant! Does this sound good? Enter y/n:")
     return random_resturant

def give_transportation():
     random_mode_of_transportation = random.choice(mode_of_transportation)
     good_user_input = "y"
     while good_user_input == "y":
          user_input = input(f"We have chosen {random_mode_of_transportation} for your transportation! Sound good? y/n: ")
          if good_user_input != user_input:
               random_mode_of_transportation = random.choice(mode_of_transportation)
               print(input(f"Oh, sorry you dont like that transportation option. No worries, we can try something else! How about {random_mode_of_transportation}? y/n: "))
               continue
     else:
          print("Awsome! Glad we got that figured out. Lets move on")

def give_entertainment():
     random_form_of_entertainment = random.choice(form_of_entertainment)
     print(f"We have chosen {random_form_of_entertainment} for your entertainment! Does this sound good? Enter y/n:")
     return random_form_of_entertainment

# user input

welcome_user()
give_transportation()