from car import Car

class Battery:
    """A class to represent a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initializes the battery with a default size."""
        self.battery_size = battery_size 
        
    def describe_battery(self):
        """Prints a description of the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")
    
    def get_range(self):
        """Returns the range of the car based on the battery size."""
        if self.battery_size == 75:
            range = 240  # miles
        elif self.battery_size == 100:
            range = 315  # miles
        
        print(f"This car can go approximately {range} miles on a full charge.")
              
# creating an ElectricCar class that inherits from Car
class ElectricCar(Car):
    """A class to represent an electric car, inheriting from Car."""
    
    def __init__(self, make, model, year):
        """Initializes the electric car with make, model, year, and battery size."""
        super().__init__(make, model, year)
        self.battery = Battery()  # Initialize the battery object

        
    def fill_gas_tank(self):
        """Overrides the fill_gas_tank method to indicate electric cars don't have gas tanks."""
        print(f"The {self.year} {self.make} {self.model} is electric and does not have a gas tank to fill.")
        

my_leaf = ElectricCar('nissan', 'leaf', 2022)
print(my_leaf.get_car_description())
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()


