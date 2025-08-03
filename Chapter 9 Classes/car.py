# creating a Car class to represent a car object
class Car:
    """A class to represent a car."""

    def __init__(self, make, model, year):
        """Initializes the car with a make, model, and year."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_car_description(self):
        """Prints a description of the car."""
        long_name = (f"{self.year}, {self.make}, {self.model}")
        return long_name.title()
    
    def read_odometer(self):
        """Prints the car's odometer reading."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def start_engine(self):
        """Simulates starting the car's engine."""
        print(f"The engine of the {self.year} {self.make} {self.model} is now running.")

    def stop_engine(self):
        """Simulates starting the car's engine."""
        print(f"The engine of the {self.year} {self.make} {self.model} has been switched off.")
            
    def update_odometer(self, mileage):
        """Updates the odometer reading to a new value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!") 
            
    def increment_odometer(self, miles):
        """Adds a specified amount to the odometer reading.""" 
        if miles >= 0:          
            self.odometer_reading += miles
        else:
            print("You can't increment the odometer with a negative value!")
            
            
        
#   Example usage of the Car class

my_used_car = Car("Honda", "Civic", 2018)
print(my_used_car.get_car_description())
my_used_car.update_odometer(30000)
my_used_car.read_odometer()
my_used_car.start_engine()
my_used_car.increment_odometer(500)
my_used_car.stop_engine()
my_used_car.read_odometer()
