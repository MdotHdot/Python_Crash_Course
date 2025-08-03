# Creates a poll for taking sandwich orders, asking for names and the type of sandwich they would like
sandwhich_orders = {'salami': 0}

# Set a flag to indicate that polling is active
# Check if the number of salami sandwiches ordered is less than 4 (maximum available stock)
if sandwhich_orders.get('salami', 0) < 4:
    polling_active = True
else:
    print("Sorry, we are out of salami.")


while polling_active:
    # prompt for the persons name and response 
    name = input("\nWhat is your name? ")
    response = input("What sandwhich would you like ? ") 
    
    # store the response in the dictionary
    sandwhich_orders[name] = response
    
    # find out if anyone else wants to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
# polling is complete, show the results
print("\n--- Poll Results ---")
for name, response in sandwhich_orders.items():
    print(f"{name.title()} would like a  {response.title()}.")
# This program collects sandwich orders and displays the results.
