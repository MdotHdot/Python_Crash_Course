#This program displays information about pets usin positional arguments.
def decsribe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
# calling the function with positional arguments
# decsribe_pet('jeff')
# decsribe_pet('snoopy', 'dog')
# decsribe_pet( pet_name='whishkers') # calling the function with keyword arguments
decsribe_pet()


    