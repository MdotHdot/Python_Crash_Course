# This script demonstrates how to create a list of players, slicing and sort them, and print them in a formatted way.

players = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Aubrey', 'Kevin'] # List of players
#print(players[0:4]) # Output: ['Alice', 'Bob', 'Charlie', 'David']
#print(players[1:3]) # Output: ['Bob', 'Charlie']
#players.append('barry') # Adding a new player
#players.sort() # Sorting the list of players
#print(players) # Output: ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
#print(players[-3:]) # Output: ['Alice', 'Bob', 'Charlie', 'David']
print("Here are the players on the home team:")
for player in players[:3]:
    print(player.title()) # Output: prints first 3 names  ['Alice', 'Bob', 'Charlie', 'David']
print("Here are the players on the away team:")
for player in players[3:]:
    print(player.title()) # Output: prints last 3 names  ['Alice', 'Bob', 'Charlie', 'David']