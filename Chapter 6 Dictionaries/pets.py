# this program is to provide dictionaries of pets and their owners 
pets = {
    'travis': {
        'animal': 'dog',
        'pet_name': 'scooby',
        'age': 3,
        'color': 'brown',
    },
    'matt': {
        'animal': 'cat',
        'pet_name': 'whiskers',
        'age': 2,
        'color': 'black',
    },
    'james': {
        'animal': 'fish',
        'pet_name': 'goldie',
        'age': 1,
        'color': 'gold',
    },
}
for owner, pet_info in pets.items(): # iterating through the dictionary
    print(f"\nOwner: {owner.title()}") # printing the key of the dictionary
    animal = pet_info['animal'] # getting the value of the key 'animal' in the dictionary
    pet_name = pet_info['pet_name'] # getting the value of the key 'pet_name' in the dictionary
    age = pet_info['age'] # getting the value of the key 'age' in the dictionary
    color = pet_info['color'] # getting the value of the key 'color' in the dictionary
    print(f"\tAnimal: {animal.title()}") # printing the value of the key 'animal' in the dictionary
    print(f"\tPet name: {pet_name.title()}") # printing the value of the key 'pet_name' in the dictionary
    print(f"\tAge: {age}") # printing the value of the key 'age' in the dictionary
    print(f"\tColor: {color.title()}") # printing the value of the key 'color' in the dictionary