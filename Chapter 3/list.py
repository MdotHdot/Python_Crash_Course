import random
# This program demonstrates the use of lists in Python.
#names = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

#random_name = random.choice(names)
#print(ranom_name)  # Output: Random name from the list

#greetings = ['Hello', 'Hi', 'Hey', 'Greetings']
#random_greeting = random.choice(greetings) 
#print(random_greeting)  # Output: Random greeting from the list

#video_games = ['Minecraft', 'Fortnite', 'Call of Duty', 'The Legend of Zelda']
#random_video_game = random.choice(video_games)
#print(random_video_game)  # Output: Random video game from the list

#print(f"{random_greeting} {ranom_name}, would you like to play {random_video_game} today?")
# Output: Greeting + name + video game suggestion
#names.append('Frank')
#print(names)  # Output: List with the new name added

#video_games.append('Overwatch')
#print(video_games)  # Output: List with the new video game added

#names[0] = 'Alice Cooper'
#print(names)  # Output: List with the first name changed
#names.remove('Bob')
#print(names)  # Output: List with 'Bob' removed
#names.sort()
#print(names)  # Output: Sorted list of names

cars = []
cars.append('Toyota')
cars.append('Honda')
cars.append('Ford')
cars.append('Chevrolet') 
# add more cars to the list
cars.insert(1, 'Nissan') # Insert 'Nissan' at index 1
#cars.sort(reverse=True) # Sort the list of cars
print("List of original cars:")
print(cars[-1]) # Output: Sorted list of cars
#print("\nList of sorted cars:")
#print(sorted(cars)) # Output: Sorted list of cars


#del cars[2] # Remove the car at index 2
#popped_cars = cars.pop(2) # Remove the last car from the list



#print(cars) # Output: List of cars
#print(popped_cars) # Output: The car that was removed
#print(f"The last car I drove was a {popped_cars}.") # Output: The last car that was removed