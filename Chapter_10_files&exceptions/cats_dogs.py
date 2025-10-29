#getting cats and dogs from files
from pathlib import Path

def get_pets(filename):

    path = Path(filename)
    """Get a list of pets from a file"""
    try:
        contents = path.read_text(encoding='utf-8')
        filename = contents.splitlines()
    except FileNotFoundError:    
        pass
    else:
        print(f"\nHere are the pets in {filename}:")
        for pet in filename:
            print(pet.title())
    
pets = ['cats.txt', 'dogs.txt', 'rabbits.txt']    
for pet in pets:
            
    get_pets(pet)