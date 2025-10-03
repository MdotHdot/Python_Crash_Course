# creates a Class called Restaurant and multiple methods to represent a restaurant's attributes and behaviors.
class Restaurant:
    """A class to represent a restaurant."""

    def __init__(self, name, cuisine_type, customer_count=0):
        """Initializes the restaurant with a name and cuisine type.(self should always be the first parameter in a class method)
        The customer_count is optional and defaults to 0."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.customer_count = customer_count
        self.number_served = 0
        
    def describe_restaurant(self):
        """Prints a description of the restaurant."""
        print(f"{self.name} serves {self.cuisine_type} cuisine.")
    
    def open_restaurant(self):
        """Simulates opening the restaurant."""
        print(f"{self.name} is now open for business!")
    
    def set_customer_count(self, count):
        """Sets the number of customers currently in the restaurant."""
        self.customer_count = count
        print(f"{self.name} currently has {self.customer_count} customers.")
# Example usage of the Restaurant class
    def set_customer_served(self, count):
        """Sets the number of customers served by the restaurant."""
        self.number_served = count
        print(f"{self.name} has served {self.number_served} customers.")
    def increment_customer_served(self, count):
        """Increments the number of customers served by a specified count."""
        if count >= 0:
            self.number_served += count
            print(f"{self.name} has now served {self.number_served} customers.")
        else:
            print("You can't decrement the number of customers served with a negative value!")
        
class IceCreamStand(Restaurant):
    """A class to represent an ice cream stand, inheriting from Restaurant."""

    def __init__(self, name, cuisine_type, flavors=None):
        """Initializes the ice cream stand with a name, cuisine type, and optional flavors."""
        super().__init__(name, cuisine_type)
        print(f"Creating an ice cream stand named {self.name} that serves {self.cuisine_type} cuisine.")
        self.flavors = flavors if flavors is not None else []

    def display_flavors(self):
        """Displays the available ice cream flavors."""
        if self.flavors:
            print(f"{self.name} offers the following ice cream flavors: {', '.join(self.flavors)}")
        else:
            print(f"{self.name} currently has no ice cream flavors available.")
icecream1 = IceCreamStand("Sweet Treats", "Dessert", ["Vanilla", "Chocolate", "Strawberry"])

# restaurant_1 = Restaurant("The Gourmet Kitchen", "French")
# restaurant_1.describe_restaurant()
# restaurant_1.open_restaurant()
# restaurant_1.set_customer_count(30)
# restaurant_1.set_customer_served(50)
# restaurant_1.increment_customer_served(-50)


# restaurant_2 = Restaurant("Spicy Delight", "Indian", 50)
# restaurant_2.describe_restaurant()
# restaurant_2.open_restaurant()
# restaurant_2.set_customer_count(50)
# restaurant_2.set_customer_served(100)
# restaurant_2.increment_customer_served(20)