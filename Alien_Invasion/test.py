import math

def calculate_square_root(number):
  if number < 0:
    raise ValueError("Cannot calculate square root of a negative number")
  return math.sqrt(number)

# How can we call calculate_square_root(-4) without the program crashing?
try:
    result = calculate_square_root(-4)
    print(f"The square root is: {result}")
  
except ValueError as e:
    print(f"Error: {e}")