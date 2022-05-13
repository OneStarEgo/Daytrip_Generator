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
     print(f"We have chosen {random_mode_of_transportation} for your transportation!")
     user_input = "y"
     while user_input != "n":
          user_input = input("Does this sound good? y/n: ")
          if user_input == "n":
               random_mode_of_transportation = random.choice(mode_of_transportation)
               print("Oh, sorry you dont like that transportation option. No worries, we can try something else!")
               print(input(f"How about {random_mode_of_transportation} ? y/n: "))
          
               return random_mode_of_transportation

def give_entertainment():
     random_form_of_entertainment = random.choice(form_of_entertainment)
     print(f"We have chosen {random_form_of_entertainment} for your entertainment! Does this sound good? Enter y/n:")
     return random_form_of_entertainment

# user input

welcome_user()
give_transportation()