#reads file stored in favourite_number.py and prints the contents
from pathlib import Path
import json

path = Path('favourite_numbers.json')
contents = path.read_text()
favourite_number = json.loads(contents)
print(f"Your favourite number is {favourite_number}")