# #this program creates a dictonary of aliens using nestedq dictionaries.
# # creating a dictionaries for each alien
# alien_0 = {'color': 'green', 'points': 5} 
# alien_1 = {'color': 'yellow', 'points': 10} 
# alien_2 = {'color': 'red', 'points': 15} 
# # creating a list of aliens
# aliens = [alien_0, alien_1, alien_2] 
# for alien in aliens: # iterating through the list of aliens
#     print(alien)

# Make an empty list to store aliens
aliens = []
# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'} # creating a dictionary for each alien
    aliens.append(new_alien) # adding the alien to the list of aliens
    
    for alien in aliens[0:3]:
        if alien['color'] == 'green':
            alien['color'] = 'yellow'
            alien['points'] = 10
            alien['speed'] = 'medium'
        elif alien['color'] == 'yellow':
            alien['color'] = 'red'
            alien['points'] = 15
            alien['speed'] = 'fast'
            
# Ch
# Show the first 5 aliens
for alien in aliens[:6]: # iterating through the first 5 aliens in the list
    print(alien) # printing the alien
print("...") # printing the ellipsis

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}") # printing the total number of aliens in the list