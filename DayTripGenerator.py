# Lists for destinations, restaurants, modes of transportation, and entertainment
destination_choices = ["Hawaii", "Fiji", "Tulum", "Barbados", "Germany"]
restaurant_choices = ["Italian", "Mexican", "Bbq", "Seafood", "Greek"]
mode_of_transportation = ["Car", "Bus", "Train", "Scooters", "Carriage"]
form_of_entertainment = ["Skydiving", "Hiking", "Biking", "Sightseeing","Diving"]

# Greeting
def welcome_user():
     print("Welcome to the Day Trip Generator! Lets begin planning your trip?")
     give_destination()

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



def give_restaurant():
     random_restaurant = random.choice(restaurant_choices)
     good_user_input = "y"
     bad_user_input = "n"
     invalid_input = True
     while invalid_input:
          user_input = input(f"We have chosen {random_restaurant} for your restaurant! Sound good? y/n: ")
          if user_input == good_user_input:
               print("Awesome! Glad we got that figured out. Lets move on")
               return random_restaurant
          elif user_input == bad_user_input:
               print("Oh, sorry to hear that. No worries, we can try something else... ")
               return give_restaurant()
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
     print(f"""The trip we have generated for you is as follows:
destination: {destination_result}
Transportation: {transportation_result}
Restaurant: {restaurant_result}
Entertainment: {entertainment_result}""")


def ask_for_corrections():
     reroll_destination = "1"
     reroll_transportation = "2"
     reroll_restaurant = "3"
     reroll_entertainment = "4"
     good_user_input = "y"
     bad_user_input = "n"
     invalid_input = True
     while invalid_input:
          user_input = input("""Please type
          '1' for a new destination
          '2' for a new mode of transportation
          '3' for a new restaurant
          '4' for a new form of entertainment
          what would you like to change: """)
          if user_input == reroll_destination:
               destination_result = random.choice(destination_choices)
               print(f"Okay, your new destination is {destination_result}!")
               return destination_result
          elif user_input == reroll_transportation:
               transportation_result = random.choice(mode_of_transportation)
               print("Okay, lets get you a new restaurant!")
               return transportation_result
          elif user_input == reroll_restaurant:
               restaurant_result = random.choice(restaurant_choices)
               print("Okay, lets get you a new mode of transportation!")
               return restaurant_result
          elif user_input == reroll_entertainment:
               entertainment_result = random.choice(form_of_entertainment)
               print("Okay, lets get you a new form of entertainment!")
               return entertainment_result
          else:
               print("Sorry, I don't recognize that input, please try again.")
               continue


def get_confirmation():
     good_user_input = "y"
     bad_user_input = "n"
     invalid_input = True
     while invalid_input:
          user_input = input("Would you like to finilize this trip? y/n: ")
          if user_input == good_user_input:
               print(f"""Congrats! You're headed to {destination_result} by {transportation_result}, where you will spend the day {entertainment_result}.
                You will end the night dining at a renown {restaurant_result} restaurant. Have fun!""")
          elif user_input == bad_user_input:
               print("Oh, im sorry you didn't like your trip")
               ask_for_corrections()
               break
          else:
               print("Sorry, I don't recognize that input, please try again.")
               continue


welcome_user()
destination_result = give_destination()
restaurant_result = give_restaurant()
transportation_result = give_transportation()
entertainment_result = give_entertainment()
print(f"That does it! We have completed generating your day trip. Now lets confirm that this is the trip you wanted.")
day_trip()
get_confirmation()
# ask_for_corrections()
print(f"That does it! We have completed generating your day trip. Now lets confirm that this is the trip you wanted.")
day_trip()
get_confirmation()
# ask_for_corrections()
