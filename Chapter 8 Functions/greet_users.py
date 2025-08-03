# greeting users passing a list
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)
# List of usernames
usernames = ['hannah', 'ty', 'margot']
# Calling the function with the list of usernames
greet_users(usernames)  # Output: Hello, Hannah! Hello, Ty! Hello, Margot!