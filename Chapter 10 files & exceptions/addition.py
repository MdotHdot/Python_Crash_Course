#adds 2 numbers together from user input if they are both integers if not returns a vaule error

def add_two_numbers():
    while True:
        first_input = input("Enter the first number (or 'q' to quit): ")
        if first_input.lower() == 'q':
            break
        try:
            num1 = int(first_input)
            num2 = int(input("Enter the second number: "))
            result = num1 + num2
            print(f"The sum of {num1} and {num2} is {result}.")
        except ValueError:
            print("Invalid input. Please enter valid integers.")
        
        
add_two_numbers()