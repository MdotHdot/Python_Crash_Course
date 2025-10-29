#this program illustrates the use of an if statement to check if a value is in a list, for this example im using voters age.

# age = int(input("Enter your age: ")) # This will create a new variable with the value 'age'
# if age >= 18: # This will check if the value is greater than or equal to '18'
#     print("You are old enough to vote!")
#     print("Have you registered to vote yet?")
# else:
#     print("Sorry, you are too young to vote.")
#     print("Please register to vote when you turn 18.")

# This program will show an example of conditional testing using IF statements
print( "welcome to the theme park")
age = int(input("Enter your age: ")) # This will create a new variable with the value 'age'
if age < 4 :
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
elif age >= 65:

    price = 20
print(f"Your ticket price is ${price}.") # This will print the value of the variable
# This program will show an example of conditional testing using IF statements