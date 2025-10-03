#storing user data for future sessions
from pathlib import Path
import json

def get_stored_user_data(path):
    """Get stored user data if available."""
    if path.exists():
        contents = path.read_text()
        user_data = json.loads(contents)
        return user_data
    else:
        return None

def get_new_user_data(path):
    """Prompts for new user information."""
    user_data = {}
    
    username = input("Enter your name: ")
    user_data['username'] = username
    age = input("Enter your age: ")
    user_data['age'] = age
    email = input("Enter your email: ")
    user_data['email'] = email
       
    contents = json.dumps(user_data)
    path.write_text(contents)
    return user_data

def verify_user_data(user_data):
    """Verify if the stored data is correct."""
    # This function now takes the dictionary as an argument.
    print(f"Is this your information? Name: {user_data['username']}, Age: {user_data['age']}, Email: {user_data['email']}")
    response = input("Enter 'y' for yes or 'n' for no: ").lower()
    if response == 'y':
        return True
    else:
        return False
    
def greet_user():
    """Greet the user by name."""
    path = Path("user_data.json") # Changed filename to be more descriptive
    user_data = get_stored_user_data(path)
    
    if user_data:
        # We call the function and check its returned True/False value.
        # We also pass the entire user_data dictionary to it.
        user_verified = verify_user_data(user_data)
        
        if user_verified:
            print(f"Welcome back, {user_data['username']}!")
        else:
            # If the user says no, get new data
            user_data = get_new_user_data(path)
            print(f"We'll remember you when you come back, {user_data['username']}!")

    else:
        user_data = get_new_user_data(path)
        print(f"We'll remember you when you come back, {user_data['username']}!")

# We just call the main function
greet_user()