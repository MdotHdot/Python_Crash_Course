# this program gathers information about a person and stores it in a dictionary
people = {
    'travis': {
        'food' : 'cereal',
        'color' : 'blue',
        'animal' : 'giraffe',
        'fun place' : 'butlins',
        'game': 'minecraft',
    },
    'matt': {
        'food' : 'buffalo wings',
        'color' : 'green',
        'animal' : 'dog',
        'fun place' : 'wave pool',
        'game': 'final fantasy',

    },
    'james': {
        'food' : 'pizza',
        'color' : 'red',
        'animal' : 'cat',
        'fun place' : 'amusement park',
        'game': 'fortnite',

    },
}

for name, info in people.items(): # iterating through the dictionary
    print (f"\nName: {name.title()}") # printing the key of the dictionary
    food = info['food'] # getting the value of the key 'food' in the dictionary
    color = info['color'] # getting the value of the key 'color' in the dictionary
    animal = info['animal'] # getting the value of the key 'animal' in the dictionary
    fun_place = info['fun place'] # getting the value of the key 'fun place' in the dictionary
    game = info['game'] # getting the value of the key 'game' in the dictionary
    print(f"\tFood: {food.title()}") # printing the value of the key 'food' in the dictionary
    print(f"\tColor: {color.title()}") # printing the value of the key 'color' in the dictionary
    print(f"\tAnimal: {animal.title()}") # printing the value of the key 'animal' in the dictionary
    print(f"\tFun place: {fun_place.title()}") # printing the value of the key 'fun place' in the dictionary
    print(f"\tGame: {game.title()}") # printing the value of the key 'game' in the dictionary






# person_0 = {
#     'first_name': 'travis',
#     'last_name': 'hinton',
#     'age': 3,
#     'city': 'London',
# }

# print(f"First name: {person_0['first_name'].title()}") # printing the value of the key 'first_name' in the dictionary
# print(f"Last name: {person_0['last_name'].upper()}") # printing the value of the key 'last_name' in the dictionary
# print(f"Age: {person_0['age']}") # printing the value of the key 'age' in the dictionary
# print(f"City: {person_0['city'].lower()}") # printing the value of the key 'city' in the dictionary

