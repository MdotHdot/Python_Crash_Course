# using 2 lists one for messages and an empty list to show the messages
def show_messages(unsent_messages, sent_messages):
    """Display each message in the unsent list and move it to the sent list."""
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)
def show_sent_messages(sent_messages):
    """Display all the messages that have been sent."""
    print("\n Sent messages:")
    for sent_message in sent_messages:
        print(sent_message)
        
        
    
    
# Program that simulates sending messages from one list to another
# starting with a list of unsent messages, the program will send each message and move it to a list of sent messages.   

unsent_messages = [ "Hello, world!",
             "Python is great!",
             "Functions are powerful!",
             "Keep learning and coding!"]
sent_messages = []

show_messages(unsent_messages[:], sent_messages)
show_sent_messages(sent_messages)
archived_messages = sent_messages[:]  # Copy sent messages to archived messages
print("\nArchived messages:")
for archived_message in archived_messages:
    print(archived_message)
# def show_messages(messages):
#     """Display each message in the list."""
#     for message in messages:
#         print(message)
# def show_messages(messages):
#     """Display each message in the list."""
#     for message in messages:
#         print(message)
        