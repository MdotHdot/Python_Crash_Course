#This Program introduces the concept of of tuples in python using the dimensions of a rectangle
dimensions = (200, 50) # A tuple is a collection of values that cannot be changed

#print(dimensions[0]) # Prints the first value of the tuple
#print(dimensions[1]) # Prints the second value of the tuple
# The values of the tuple cannot be changed

#dimensions[0] = 250 # This will cause an error
print("Original dimensions:")
for dimension in dimensions: # This will print all the values of the tuple
    print(dimension)
dimensions = (250, 100) # This will create a new tuple with the new value
print("\nModified dimensions:")
for dimension in dimensions: # This will print all the values of the new tuple
    print(dimension)