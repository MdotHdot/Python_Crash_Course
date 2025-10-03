#importd car.py as a module
from car import Car
from electric_car import ElectricCar as EC

my_new_car = Car("Audi", "A4", 2024)
print(my_new_car.get_car_description())
my_new_car.odometer_reading = 10
my_new_car.read_odometer()
my_electric_car = EC("Tesla", "Model S", 2024)
print(my_electric_car.get_car_description())
my_electric_car.battery.describe_battery()
my_electric_car.battery.get_range()