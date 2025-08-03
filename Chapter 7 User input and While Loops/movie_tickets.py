#This Program will ask customers their age and will provide them with a ticket price based on their age.
promppt = "\nWelcome to Coding Cinema!Please enter your age:"
promppt += "\n(Enter 'quit' when you are finished.)"

while True:
    age = input(promppt)
    if age == ' quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif age < 12:
            print("Your ticket is $10.")
        else:
            print("Your ticket is $15.")
#This program will ask customers their age and will provide them with a ticket price based on their age.