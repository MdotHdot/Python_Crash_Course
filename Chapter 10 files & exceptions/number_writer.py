#using Json to store numbers
from pathlib import Path
import json

numbers = []
while True:
    try:
        num = input("Enter a number (or 'q' to quit): ")
        if num.lower() == 'q':
            break
        numbers.append(int(num))
    except ValueError:
        print("Please enter a valid number.")

path = Path('numbers.json')
contents = json.dumps(numbers)
path.write_text(contents)