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
               return give_destination()
          else:
               print("Sorry, I don't recognize that input, please try again.")
               continue


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

def day_trip():
     destination_result = give_destination()
     resturant_result = give_resturant()
     entertainment_result = give_entertainment()
     transportation_result = give_transportation()
     print(f""""The trip we have generated for you is as follows:
     destination: {destination_result}
     Transportation: {transportation_result}
     Resturant: {resturant_result}
     Entertainment: {entertainment_result}
     """)


welcome_user()
give_destination()
give_resturant()
give_transportation()
give_entertainment()
print(f"Congrats! We have completed generating your day trip. Now lets just confirm that this is the trip you wanted.")
day_trip()