# This program demonstrates how to copy a list in Python and modify both lists independently.
my_foods = ['pizza', 'falafel', 'carrot cake'] # list of foods
friend_foods = my_foods[:] # makes a copy of the list
my_foods.append('cannoli') # adds a new food to the list
friend_foods.append('ice cream') # adds a new food to the copied list
friend_foods.remove('falafel') # removes a food from the copied list

print ("My favorite foods are:")
print(my_foods) # prints the list of foods
print("\nMy friend's favorite foods are:")
print(friend_foods) # prints the copied list of foods