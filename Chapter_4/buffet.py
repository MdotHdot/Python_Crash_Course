# using Tuples this program will create a buffet with different types of food
# and print the buffet
buffet = ('chowmein', 'pizza', 'sushi', 'tacos', 'salad') # A tuple is a collection of values that cannot be changed
print("Buffet items:")
#buffet [1] = 'pasta' # This will cause an error
#print("Buffet items:")
print ("Lunch Buffet:")
for buffet in buffet:
    print(buffet) # prints the buffet items
buffet = ('pasta', 'pizza', 'sushi', 'tacos', 'salad') # This will create a new tuple with the new value
print("\nDinner Buffet:")
for buffet in buffet:
    print(buffet) # prints the buffet items