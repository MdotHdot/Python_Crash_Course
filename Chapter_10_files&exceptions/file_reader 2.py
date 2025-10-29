from pathlib import Path
#this file is a simple file reader

path = Path('Python_Crash_Course/Chapter 10 files & exceptions/pi_million_digits.txt')
contents = path.read_text().rstrip()
# contents = contents()
lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()
print(pi_string)
print(f"{len(pi_string[:52])} digits of pi")