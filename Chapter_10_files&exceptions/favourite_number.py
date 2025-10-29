#asks user for favourite number and stores it in a file
from pathlib import Path
import json


def get_stored_number(path):
    """Get stored favourite number if available."""
    if path.exists():
        contents = path.read_text()
        favourite_number = json.loads(contents)
        return favourite_number
    else:
        return None

def get_new_number(path):
    """Prmpt for a new favourite number."""
    favourite_number = input("What is your favourite number? ")
    contents = json.dumps(favourite_number)
    path.write_text(contents)
    return favourite_number 

def remember_number():
    """Remember the user's favourite number."""
    path = Path('favourite_numbers.json')
    favourite_number = get_stored_number(path)
    if favourite_number:
        print(f"Your favourite number is {favourite_number}")
    else:
        favourite_number = get_new_number(path)
        print(f"We'll remember that your favourite number is {favourite_number} when you come back!")
        
remember_number()