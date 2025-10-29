# model_printer.py
import sys
import os

print(f"Current working directory: {os.getcwd()}")
print("Python sys.path:")
for p in sys.path:
    print(f"  {p}")
print("-" * 30)

from printing_functions import print_models, show_completed_models
# This code imports the printing_functions module and uses its functions to print models and show completed models.
# It starts with a list of unprinted designs, prints each design, and moves it to

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
printed_models = []
print_models(unprinted_designs, printed_models)
show_completed_models(printed_models)
#print(unprinted_designs)  # This will show the original list is unchanged
# This code defines two functions: print_models and show_completed_models.









#Program that modifys list of models in a function 
#starting with a list of unprinted designs, the program will print each design and move it to a list of completed models.


# def print_models(unprinted_designs, completed_models):
#     '''simulate printing each design until there are no more unprinted designs,
#     move each design to completed_models after printing'''

#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)
# def show_completed_models(completed_models):
#     '''show all the models that have been printed'''