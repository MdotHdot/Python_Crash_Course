#Thid is a Parrot Program testing the bacic functionality of user input, it will repeat whatever the user types.
#the prompts are designed to be clear and easy to understand.
prompt = "\n Type a message and I will repeat it back to you:"
prompt += "\n Enter 'quit' to end the program. "

# message = ""
# #the while loop allows user to imppt until user types 'quit'
# while message != 'quit':
#     message = input(prompt)
  
#     if message != 'quit':
#         print(message)
# #This program will repeat whatever the user types, until the user types 'quit'.
active = True
while active:
    message  = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)