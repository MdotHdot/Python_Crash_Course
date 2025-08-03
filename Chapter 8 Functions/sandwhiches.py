def make_sandwich(size, *fillings):
    """Print the list of fillings that have been requested."""
    print(f"\nMaking a {size}-inch sandwich with the following fillings:")
    for filling in fillings:
        print(f"- {filling}")
        
make_sandwich(6, 'turkey', 'lettuce', 'tomato')
make_sandwich(12, 'ham', 'cheese', 'onions', 'pickles', 'mustard')
make_sandwich(8, 'roast beef', 'swiss cheese', 'horseradish', 'arugula')

