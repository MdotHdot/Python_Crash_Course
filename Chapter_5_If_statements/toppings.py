#requested_topping = 'mpy'
#if requested_topping != 'anchovies':
 #   print("Hold the anchovies!")
# This program will show an example of conditional testing using IF statements
avalable_toppings = ['pepperoni', 'pineapple', 'mushrooms', 'extra cheese'] # A list is a collection of values that can be changed
requested_toppings = ['pepperoni' , 'extra cheese', 'french fries', 'mushrooms', 'olives'] # A list is a collection of values that can be changed

if requested_toppings:
    
    for requested_topping in requested_toppings:
        if requested_topping in avalable_toppings:
            print(f"Adding {requested_topping}.")
        else:
            print(f"Sorry, we don't have {requested_topping}.")
        
    
        
        
print("\nFinished making your pizza!") # This will print the value of the variable
# if 'mushrooms' in requested_topping:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_topping:
#     print("Adding pepperoni.")
# print("\nFinished making your pizza!") # This will print the value of the variable

#customer_order = str(input(f"Select your toppings: {requested_topping}")) # This will create a new variable with the value 'customer_order'

