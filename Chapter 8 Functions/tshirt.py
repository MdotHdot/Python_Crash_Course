#creates a fuction for tshirt for size and colour
def make_tshirt( colour, size='large'):
    """Display the size and colour of the tshirt."""
    print(f"The size of the tshirt is {size} and the colour is {colour}.")
# calling the function with positional arguments
make_tshirt('large', 'blue')  # calling the function with positional arguments
make_tshirt(size='medium', colour='red')  # calling the function with keyword arguments
make_tshirt(colour='green', size='small')  # calling the function with keyword arguments