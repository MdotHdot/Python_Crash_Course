#for value in range(1, 10000000000000): # creates a list of numbers from 1 to 1000000000000
#    print(value) 
#
# numbers = list(range(2, 11)) # creates a list of numbers from 1 to 10
#print(numbers) # prints the list of numbers

#even_numbers = list(range(2, 11, 2)) # creates a list of  even numbers from 2 to 10
#print(even_numbers) # prints the list of even numbers
#odd_numbers = list(range(1, 20, 2)) # creates a list of  odd numbers from 1 to 10
#print(odd_numbers) # prints the list of even numbers
#squares = []
#for value in range(1, 11): # creates a list of numbers from 1 to 10

#    squares.append(value ** 2) # squares each number and adds it to the list
#print(squares) # prints the list of squared numbers
#squares = [value ** 3 for value in range(1, 11)] # creates a list of squared numbers using list comprehension
#print(squares) # prints the list of squared numbers

digits = list(range(1, 100001))  # creates a range of numbers from 1 to 100000
print("Min:", min(digits))  # prints the minimum value in the list
print("Max:", max(digits))  # prints the maximum value in the list
print("Sum:", sum(digits))  # prints the sum of all numbers in the list
