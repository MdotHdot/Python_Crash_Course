#This program is for users to rent a car , it will check if the car is available or not

cars = ['audi', 'bmw', 'subaru', 'toyota'] # A list is a collection of values that can be changed

car_rental = input("Enter the car you want to rent: ") # This will ask the user to enter a car
if car_rental in cars: # This will check if the value is in the list
    print(f"\nWe have a {car_rental} available") # This will print the value of the variable
else:
    print(f"\nSorry, we dont have a {car_rental} available")

    
# for car in cars:
#     if car == 'ford':
#         print ("We have a ford available") # This will print the value of the variable
#     else:
#         print(f"we dont have a Ford but we have {car} available")
        
# new_car = 'porsche' # This will create a new variable with the value 'audi'
# if new_car == cars:
#     print("We have a Porshe available") # This will print the value of the variable
# else:
#     print(f"we dont have a porsche but we have {cars} available")
    

  
        
        
