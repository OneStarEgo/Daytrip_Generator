destination_choices = ["Hawaii", "Fiji", "Tulum", "Barbados"]
resturant_choices = ["Italian", "Mexican", "Bbq", "Seafood"]
mode_of_transportation = ["Car", "Bus", "Train", "Scooters"]
form_of_entertainment = ["Concert", "Hiking", "Water Park", "Sightseeing"]


import random
random_destination = (random.choice(destination_choices))
print(random_destination)

random_resturant = (random.choice(resturant_choices))
print(random_resturant)

random_mode_of_transportation = (random.choice(mode_of_transportation))
print(random_mode_of_transportation)

random_form_of_entertainment = (random.choice(form_of_entertainment))
print(random_form_of_entertainment)