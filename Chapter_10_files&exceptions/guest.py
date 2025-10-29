#using write text to write to a file
from pathlib import Path
path = Path('Python_Crash_Course/Chapter 10 files & exceptions/guest.txt')
# guest = "guest name is:"
# path.write_text(guest)
# name = input("What is your name? ")
# updated_guest = guest + " " + name
# path.write_text(updated_guest)

while True:
    name = input("What is your name? (enter 'q' to quit) ")
    if name == 'q':
        break
    else:
        guest = "\n Guest name is: " + name 
        with open(path, 'a') as file:
            file.write(guest)

