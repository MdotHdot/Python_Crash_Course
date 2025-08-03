def print_models(unprinted_designs, completed_models):
    '''simulate printing each design until there are no more unprinted designs,
    move each design to completed_models after printing'''

    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)
def show_completed_models(completed_models):
    '''show all the models that have been printed'''
    
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
      
# FILE: printing_functions.py
# Make sure this file is named exactly 'printing_functions.py'

# def print_models(unprinted_designs, completed_models):
#     '''simulate printing each design until there are no more unprinted designs,
#     move each design to completed_models after printing'''
#     # The 'while' loop and its contents MUST be indented here (e.g., 4 spaces or 1 tab)
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     '''show all the models that have been printed'''
#     # The 'print' statement and 'for' loop MUST be indented here (e.g., 4 spaces or 1 tab)
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)