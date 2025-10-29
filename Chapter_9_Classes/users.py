# Creates a class to represent a user
class User:
    """A class to represent a user."""

    def __init__(self, first_name, last_name, age):
        """Initializes the user with a first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0
 
    def set_login_attempts(self, attempts):
        """Sets the number of login attempts."""
        self.login_attempts = attempts
        print(f"Login attempts set to: {self.login_attempts}")
    def increment_login_attempts(self, count):
        """Increments the number of login attempts."""
        
        if self.login_attempts >= 0:
            # Increment the login attempts by 1
            self.login_attempts += count
            print(f"Login attempts: {self.login_attempts}")
        else:
            print("Login attempts cannot be negative!")
            
    def reset_login_attempts(self):
        """Resets the number of login attempts to zero."""
        self.login_attempts = 0
        print("Login attempts have been reset to zero.")
        

    def describe_user(self):
        """Prints a description of the user."""
        print(f"User: {self.first_name} {self.last_name}, Age: {self.age}")

    def greet_user(self):
        """Greets the user."""
        print(f"Hello, {self.first_name} {self.last_name}!")
    

        
        
user_1 = User("John", "Doe", 30)
user_1.describe_user()
user_1.greet_user()
user_1.set_login_attempts(3)  # Initialize login attempts
user_1.increment_login_attempts(1)  # Simulate a login attempt

user_2 = User("Jane", "Smith", 25)
user_2.describe_user()
user_2.greet_user() 
user_2.set_login_attempts(2)  # Initialize login attempts
user_2.increment_login_attempts(2) 
user_2.reset_login_attempts()# Simulate another login attempt

user_3 = User("Alice", "Johnson", 28)
user_3.describe_user()
user_3.greet_user()
user_3.increment_login_attempts(3)  # Simulate a login attemp

