#counts the common word in a text file
from pathlib import Path

path = Path('alice.txt')

contents = path.read_text(encoding='utf-8')
common_words = contents.lower().count('alice')  # Convert to lowercase before counting
print(f"The word 'alice' appears {common_words} times in the text.")