#This program will show an example of conditional testing using IF statements
#cars = ['audi', 'bmw', 'subaru', 'toyota'] # A list is a collection of values that can be changed

#for loop to print values of the list while looking for bmw in th elist
#for car in cars: # This will print all the values of the list
#    if car == 'bmw': # This will check if the value is equal to 'bmw'
 #       print(car.upper()) # This will print the value in uppercase
  #  else:
   #     print(car.title()) # This will print the value in title case
 
#car = 'subaru' # This will create a new variable with the value 'subaru'
#print("Is car == 'subaru'? I predict True.") # This will print the value of the variable
#print(car == 'subaru') # This will check if the value is equal to 'subaru'
#print("\nIs car == 'audi'? I predict False.") # This will print the value of the variable
#print(car == 'audi') # This will check if the value is equal to 'audi'

cars = ['audi', 'bmw', 'subaru', 'toyota'] # A list is a collection of values that can be changed
#for car in cars:
 #   if car == 'bmw' or car == 'audi': # This will check if the value is equal to 'bmw' or 'audi'
  #      print("We have a car that is either bmw or audi") # This will print the value of the variable
   # if car != 'bmw' or car != 'audi': # This will check if the value is equal to 'bmw' or 'audi'
    #    print(f"we have {car} available") # This will print the value of the variable
for car in cars:
    if car == 'ford':
        print ("We have a ford available") # This will print the value of the variable
    else:
        print(f"we dont have a Ford but we have {car} available")
        
new_car = 'porsche' # This will create a new variable with the value 'audi'
if new_car == cars:
    print("We have a Porshe available") # This will print the value of the variable
else:
    print(f"we dont have a porsche but we have {cars} available")
    

  
        
        
