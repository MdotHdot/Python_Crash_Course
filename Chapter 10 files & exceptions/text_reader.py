#a program to read a text file and print its contents to the screen
from pathlib import Path
path = Path('Python_Crash_Course/Chapter 10 files & exceptions/learning_python.txt')
contents = path.read_text().rstrip()
stored_string = [contents]
print(stored_string)
for line in stored_string:
    line = line.replace('Python', 'C')
    print(line)