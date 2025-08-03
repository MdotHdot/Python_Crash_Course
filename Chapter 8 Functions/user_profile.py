# This program defines a function to build a user profile dictionary
# and allows the user to input their first name, last name, and additional information.
def build_profile(first_name, last_name, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first_name
    user_info['last_name'] = last_name
    return user_info

# # Main program to create a user profile
print("Welcome to the User Profile Creator!")
user_profile = build_profile
while True:
    print("\nPlease enter your first name:")
    first_name = input()
    if first_name.lower() == "exit":
        print("Exiting the profile creation. Goodbye!")
        break
    print("\nPlease enter your last name:")
    last_name = input()
    if last_name.lower() == "exit":
        print("Exiting the profile creation. Goodbye!")
        break

    if first_name and last_name:
        print(f"\nHello {first_name} {last_name}! Let's build your profile.")    
    else:
        print("Both first name and last name are required. Please try again.")
    
    user_info = {}
    while True:
        print("\n Enter additional information (key=value) or type 'done' to finish:")
        info = input()
        if info.lower() == 'done':
                print("Finished entering information.")
                break
        try:
            key, value = info.split('=')
            user_info[key.strip()] = value.strip()
        except ValueError:
            print("Invalid format. Please use key=value format.")
    
    profile = build_profile(first_name, last_name, **user_info)
    print("\nUser Profile:")
    print(profile)
    


# user_profile = build_profile('albert', 'einstein',
#                              location='princeton',
#                              field='physics',
#                              age=76,
#                              occupation='theoretical physicist')
# print(user_profile)
# # Example output:

