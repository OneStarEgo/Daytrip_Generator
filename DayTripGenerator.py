# Lists for destinations, resturants, modes of transportation, and entertainment
destination_choices = ["Hawaii", "Fiji", "Tulum", "Barbados", "Germany"]
resturant_choices = ["Italian", "Mexican", "Bbq", "Seafood", "Greek"]
mode_of_transportation = ["Car", "Bus", "Train", "Scooters", "Carriage"]
form_of_entertainment = ["Concert", "Hiking", "Water Park", "Sightseeing","Diving"]

# Greeting
def welcome_user():
     print("Welcome to the Day Trip Generator! Lets begin planning your trip?")

# Generate random selections
import random
def give_destination():
     random_destination = random.choice(destination_choices)
     good_user_input = "y"
     while good_user_input == "y":
          user_input = input(f"We have chosen {random_destination} for your destination! Sound good? y/n: ")
          if good_user_input != user_input:
               random_destination = random.choice(destination_choices)
               continue
          else:
               print("Awesome! Glad we got that figured out. Lets move on")
               
               return random_destination

def give_resturant():
     random_resturant = random.choice(resturant_choices)
     good_user_input = "y"
     while good_user_input == "y":
          user_input = input(f"We have chosen {random_resturant} for your resturant! Sound good? y/n: ")
          if good_user_input != user_input:
               random_resturant = random.choice(resturant_choices)
               continue
          else:
               print("Awesome! Glad we got that figured out. Lets move on")
               return random_resturant

def give_transportation():
     random_mode_of_transportation = random.choice(mode_of_transportation)
     good_user_input = "y"
     while good_user_input == "y":
          user_input = input(f"We have chosen {random_mode_of_transportation} for your transportation! Sound good? y/n: ")
          if good_user_input != user_input:
               random_mode_of_transportation = random.choice(mode_of_transportation)
               continue
          else:
               print("Awesome! Glad we got that figured out. Lets move on")
               return random_mode_of_transportation

def give_entertainment():
     random_form_of_entertainment = random.choice(form_of_entertainment)
     good_user_input = "y"
     while good_user_input == "y":
          user_input = input(f"We have chosen {random_form_of_entertainment} for your entertainment! Sound good? y/n: ")
          if good_user_input != user_input:
               random_form_of_entertainment = random.choice(form_of_entertainment)
               continue
          else:
               print("Awesome! Glad we got that figured out. Your trip is all planned! ")
               return random_form_of_entertainment


give_destination()
give_resturant()
give_entertainment()
give_transportation()