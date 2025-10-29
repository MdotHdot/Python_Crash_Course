# Counts the number of words in a file
from pathlib import Path


def count_words(filename):
    """Counts the number of words in a file.

    Args:
        filename (str): The name of the file to count words in.
    """
    
    # Correctly constructs the path by joining the current working directory
    # with the filename.
    path = Path(filename)
    
    try:
        # Reads the file and stores it in contents variable
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # The exception block runs only for the file that doesn't exist.
        pass
    else:
        # Counts the number of words in the file
        words = contents.split()
        num_words = len(words)
        print(f"The file '{filename}' has about {num_words} words.")

# List of filenames to process
filenames = ['alice.txt', 'little_women.txt', 'moby_dick.txt', 'siddarah.txt']

# Loop through each filename in the list and call the function
for filename in filenames:
    count_words(filename)
