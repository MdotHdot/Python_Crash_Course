# using dictionaries this prograim will print an alien

# alien_0 = {'color': 'green', 'points': 5} # creating a dictionary for alien_0
# alien_1 = {'color': 'yellow', 'points': 10}

# # new_points = alien_0['points']
# # print(f"You just earned {new_points} points!")
# # adding new key-value pairs to the dictionary
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)
# # modifying the value of a key in the dictionary

# alien_0 = {} # creating an empty dictionary
# alien_0['color'] = 'green' # adding a key-value pair to the dictionary
# alien_0['points'] = 5 # adding another key-value pair to the dictionary
# print(alien_0) # printing the dictionary


alien_0 = {'color': 'green', 'points': 5} # creating a dictionary for alien_0
print(f"the alien is {alien_0['color']}.") # printing the value of the key 'color' in the dictionary
alien_0['color'] = 'yellow' # modifying the value of the key 'color' in the dictionary
print(f"Now the alien is {alien_0['color']}.") 

# alien_0 = {'x_position': 2, 'y_position': 25 , 'speed': 'fast'} # creating a dictionary for alien_0 postions and speed 
# print(f"Original x-position: {alien_0['x_position']}") # printing the value of the key 'x_position' in the dictionary
# # moving the alien to the right
# # determine how far to move the alien based on its current speed
# if alien_0['speed'] == 'slow': # checking if the speed of the alien is slow
#     x_increment = 1 # if the speed is slow, set the increment to 1
# elif alien_0['speed'] == 'medium':
#     x_increment = 2 # if the speed is medium, set the increment to 2
# else:
#     # This must be a fast alien!
#     x_increment = 3

# alien_0 ['x_position'] = alien_0['x_position'] + x_increment # updating the value of the key 'x_position' in the dictionary
# print(f"New x-position: {alien_0['x_position']}") # printing the new value of the key 'x_position' in the dictionary
print(alien_0) # printing the dictionary
del alien_0['points']   # deleting the key 'points' from the dictionary
print(alien_0) # printing the dictionary after deleting the key 'points'