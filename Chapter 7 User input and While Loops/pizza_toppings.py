# Using while loops user, will enter pizza toppings for there pizza order
prompt = "\nWelcome To Pythons Pizzaria! \nPlease enter the name of a topping you would like on your pizza:"
prompt += "\n(Enter 'quit' when you are finished.)"


while True:
    topping = input(prompt)
    if topping == 'quit':
        break
    else:
        print(f"Adding {topping} to your pizza!") # printing the toppings of the pizza
# # asking a user what toppings they would like on their pizza using the break statement to stop when user request

# #store information about a pizza being ordered
# pizza = {
#     'crust': 'thick',
#     'toppings': ['mushrooms', 'extra cheese'],
# }
# # summarize the order
# print(f"You ordered a {pizza['crust']}-crust pizza " # printing the crust type of the pizza
#       f"with the following toppings:")

# for topping in pizza['toppings']:
#     print(f"\t{topping}") # printing the toppings of the pizza