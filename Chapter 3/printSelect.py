# This program selects a random name from a list and prints a message with the selected name.

import random
randon_name = ['Mr Blue', 'Mr Green', 'Mr Red', 'Mr Black', 'Mr White', 'Mr Yellow', 'Mr Pink', 'Mr Orange', 'Mr Purple', 'Mr Brown']
# Select a random name from the list

from_name = random.choice(randon_name)
receiver_name = random.choice(randon_name)


print(f"To: {receiver_name.lower()} hello sir or Madam would you like to learn some Python today? \n From: {from_name.upper()} \n")