#Coints the number of words in a file
from pathlib import Path

def count_words(filename):
    """Counts the number of words in a file."""
    
    path = Path.cwd() / filename  # Fixed path construction
    try:
        contents = path.read_text(encoding='utf-8') #Reads the file and stores it in contents variable
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        #Counts the number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

filenames = ['alice.txt', 'little_women.txt', 'moby_dick.txt', 'siddarah.txt']
for filename in filenames:
    count_words(filename)