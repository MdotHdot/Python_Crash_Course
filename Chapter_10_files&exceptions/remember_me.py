#storing user data for future sessions
from pathlib import Path
import json



def get_stored_user_data(path):
    """Get stored username if available."""
    if path.exists():
        contents = path.read_text()
        username = json.loads(contents)
        return username
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
    print(f"Is this your information? Name: {username}, Age: {age}, Email: {email}")
    response = input("Enter 'y' for yes or 'n' for no: ").lower()
    if response == 'y':
        return True
    else:
        return False
    
    

def greet_user():
    """Greet the user by name."""
    path = Path("username.json")
    username = get_stored_user_data(path)
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_user_data(path)
        print(f"We'll remember you when you come back, {username}!")
    

greet_user()