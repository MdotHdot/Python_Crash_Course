# This is an expansion on toppings.py where we will store lists of toppings and crust types in a dictionary

#store information about a pizza being ordered
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# summarize the order
print(f"You ordered a {pizza['crust']}-crust pizza " # printing the crust type of the pizza
      f"with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}") # printing the toppings of the pizza