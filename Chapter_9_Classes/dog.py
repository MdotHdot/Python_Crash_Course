#Creating Dog Class to represent a dog and its attributes
class Dog:
    """A class to represent a dog."""
    
    def __init__(self, name, age, breed):
       """Initializes the dog with a name, age, and breed."""
       self.name = name
       self.age = age
       self.breed = breed

    def sit(self):
        """Simulates the dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
        
    def roll_over(self):
        """Simulates the dog rolling over in response to a command."""
        print(f"{self.name} rolled over!")
        
My_dog = Dog("Buddy", 3, "Golden Retriever")
print(f"My dog's name is {My_dog.name}, he is {My_dog.age} years old and is a {My_dog.breed}.")
My_dog.sit()
My_dog.roll_over()

friend_dog = Dog("Max", 5, "Labrador")
print(f"My friend's dog's name is {friend_dog.name}, he is {friend_dog.age} years old and is a {friend_dog.breed}.")
friend_dog.sit()
friend_dog.roll_over()
# End of dog.py
# This code defines a Dog class with methods to simulate actions like sitting and rolling over.