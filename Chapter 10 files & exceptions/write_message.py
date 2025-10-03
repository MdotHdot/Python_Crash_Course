#this program will write a message to a text file
from pathlib import Path

contents = "I love programming!"
contents += "\nI love creating new games."
contents += "\nI love learning new languages."

path = Path('Python_Crash_Course/Chapter 10 files & exceptions/programming.txt')

path.write_text(contents)


# message = input("Tell me something and I will write it to a file: ")
# path.write_text(message)
