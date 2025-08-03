#Using th emodulo operator to check if a number is even or odd
number = input("Enter a number, and I will tell you if it is even or odd: ")
number = int(number)
if number % 2 == 0:
    print(f"\nThe number is even.")
else:
    print(f"\nThe number is odd.")
#The modulo operator (%) returns the remainder of a division operation.