#This program creates a dictionary to store information of programming terms and their meanings.
"""
This program creates a glossary of programming terms and their meanings using a dictionary.
It provides the following functionalities:
1. Prints all terms and their meanings in the glossary.
2. Displays a sorted list of all available commands (terms) without their meanings.
3. Allows the user to input a specific command to see its meaning or input 'all' to display all terms and their meanings.
Key Features:
- The glossary is implemented as a dictionary where keys are programming terms and values are their meanings.
- User input is handled to provide flexibility in retrieving specific term meanings or all terms at once.
- Input is case-insensitive and trimmed of leading/trailing whitespace for better usability.
- Error handling is included to notify the user if the entered command is not in the glossary.
Comments:
- The first loop iterates through the dictionary to print all terms and their meanings.
- The second loop prints a sorted list of all available commands (terms) in title case.
- User input is taken to either display the meaning of a specific term or all terms and their meanings.
- If the user enters an invalid command, an appropriate error message is displayed.
"""
# It then prints the meaning of each term in the dictionary.

glossary = {
    'if': 'A conditional statement that executes a block of code if its condition is true.',
    'elif': 'A conditional statement that executes a block of code if its condition is true and the previous conditions were false.',
    'else': 'A conditional statement that executes a block of code if all previous conditions were false.',
    'for': 'A loop that iterates over a sequence (like a list or string) and executes a block of code for each item.',
    'while': 'A loop that continues to execute a block of code as long as its condition is true.',
    'break': 'A statement that terminates the nearest enclosing loop.',
    'continue': 'A statement that skips the current iteration of the nearest enclosing loop and continues with the next iteration.',
    'def': 'A keyword used to define a function.',
    'return': 'A statement used to exit a function and return a value to the caller.',
}

for command, meaning in glossary.items():
    print(f"{command}: {meaning}")
    
print("\nThe following commands are avaliable for information:")
for command in sorted(glossary.keys()):
    print(command.title())
# this prints the list of commands without meanings in the sorted order 

# the next step will then ask user to input the command, and the meaning will be printed
user_input = input("Enter a command to see its meaning (or 'all' to see all meanings): ").strip().lower()

if user_input == 'all':
    for command, meaning in glossary.items():
        print(f"{command}: {meaning}")
elif user_input in glossary:
    print(f"{user_input}: {glossary[user_input]}")
else:
    print("Sorry, that command is not in the glossary.")
    

            

        
   

# for key, meaning in glossary.items():
#     input("enter a term to see its meaning: ") # Wait for user input before proceeding
#     print(f"{key}: {meaning}")
# elif input == 'all':
#     print(f"{key}: {meaning}")