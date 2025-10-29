# greeting a formatted name with user input 
def get_formatted_name(first_name, last_name , middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

#this is an infinte loop that will ask for user input
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")
    
    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if f_name == 'q':
        break

    m_name = input("Middle name (optional): ")
    if m_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name, m_name)
    print(f"\nHello, {formatted_name}!")
     
    
  
# def greet_user(username):
#     """Display a simple greeting."""
#     print(f"Hello {username}!") # printing a simple greeting
# # calling the function
# greet_user('Travis') # calling the function