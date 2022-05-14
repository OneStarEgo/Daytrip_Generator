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
     bad_user_input = "n"
     invalid_input = True
     while invalid_input:
          user_input = input(f"We have chosen {random_destination} for your destination! Sound good? y/n: ")
          if user_input == good_user_input:
               print("Awesome! Glad we got that figured out. Lets move on")
               return random_destination
          elif user_input == bad_user_input:
               print("Oh, sorry to hear that. No worries, we can try something else... ")
               return give_destination
          else:
               print("Sorry, I don't recognize that input, please try again.")
               continue
dest_result = give_destination()
print(f"You have chosen {dest_result}!")

def give_resturant():
     random_resturant = random.choice(resturant_choices)
     good_user_input = "y"
     bad_user_input = "n"
     invalid_input = True
     while invalid_input:
          user_input = input(f"We have chosen {random_resturant} for your resturant! Sound good? y/n: ")
          if user_input == good_user_input:
               print("Awesome! Glad we got that figured out. Lets move on")
               return random_resturant
          elif user_input == bad_user_input:
               print("Oh, sorry to hear that. No worries, we can try something else... ")
               return give_resturant()
          else:
               print("Sorry, I don't recognize that input, please try again.")
               continue
rest_result = give_resturant()
print(f"You have chosen {rest_result}!")

def give_transportation():
     random_mode_of_transportation = random.choice(mode_of_transportation)
     good_user_input = "y"
     bad_user_input = "n"
     invalid_input = True
     while invalid_input:
          user_input = input(f"We have chosen {random_mode_of_transportation} for your transportation! Sound good? y/n: ")
          if user_input == good_user_input:
               print("Awesome! Glad we got that figured out. Lets move on")
               return random_mode_of_transportation
          elif user_input == bad_user_input:
               print("Oh, sorry to hear that. No worries, we can try something else... ")
               return give_transportation()
          else:
               print("Sorry, I don't recognize that input, please try again.")
               continue
trans_result = give_transportation()
print(f"You have chosen {trans_result}!")

def give_entertainment():
     random_form_of_entertainment = random.choice(form_of_entertainment)
     good_user_input = "y"
     bad_user_input = "n"
     invalid_input = True
     while invalid_input:
          user_input = input(f"We have chosen {random_form_of_entertainment} for your entertainment! Sound good? y/n: ")
          if user_input == good_user_input:
               print("Awesome! Glad we got that figured out. Your trip is all planned! ")
               return random_form_of_entertainment
          elif user_input == bad_user_input:
               print("Oh, sorry to hear that. No worries, we can try something else... ")
               return give_entertainment()
          else:
               print("Sorry, I don't recognize that input, please try again.")
               continue
ent_result = give_entertainment()
print (f"You chose {ent_result}!")
