# This program is a simple dinner party invitation system. using lists 

Dinner_guests = ['cloud strife', 'tifa lockhart', 'barret wallace', 'aerith gainsborough']
#list of guests

#print(f"Hello {Dinner_guests[0].title()}, would you like to join me for dinner?")
#print(f"Hello {Dinner_guests[1].title()}, would you like to join me for dinner?")
#print(f"Hello {Dinner_guests[2].title()}, would you like to join me for dinner?")
#print(f"Hello {Dinner_guests[3].title()}, would you like to join me for dinner?")
# prints individual messages to each guest
declined_guest = Dinner_guests.pop() # removes the last guest from the list
print(f"Sorry ypu cant come {declined_guest.title()}, I will invite some one else.") 
new_guest = 'sephiroth' # new guest to be added

Dinner_guests.append(new_guest) # adds the new guest to the list


#print(f"Hello {Dinner_guests[0].title()}, would you like to join me for dinner?")
#print(f"Hello {Dinner_guests[1].title()}, would you like to join me for dinner?")
#print(f"Hello {Dinner_guests[2].title()}, would you like to join me for dinner?")
#print(f"Hello {Dinner_guests[3].title()}, would you like to join me for dinner?")

downsized_guest_list = Dinner_guests.pop() # deletes the last two guests from the list
print(f"Sorry you cant come {downsized_guest_list.title()}, my table isnt big enough.")
downsized_guest_list = Dinner_guests.pop() # deletes the last two guests from the list
print(f"Sorry you cant come {downsized_guest_list.title()}, my table isnt big enough.")

print(f"Hello {Dinner_guests[0].title()}, would you like to join me for dinner?")
print(f"Hello {Dinner_guests[1].title()}, would you like to join me for dinner?")


print("I am sorry I cant invite you to dinner anymore") # prints the message
print("I will be sending out new invites soon") # prints the message
print(len(Dinner_guests)) # prints the number of guests

