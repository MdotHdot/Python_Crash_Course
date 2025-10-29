#loterry draw, containing a series of numbers 10 numbers and 5 letters
import random
import string
class LotteryDraw:
    def __init__(self):
        self.numbers = random.sample(range(1, 71), 10)  # 10 unique numbers from 1 to 70
        self.letters = random.sample(string.ascii_uppercase, 5)  # 5 unique letters from A to Z

    def display_draw(self):
        print("Lottery Draw:")
        results = ', '.join(str(num) for num in self.numbers + self.letters)
        print(results)
        
print("Generating a lottery draw...")
draw = LotteryDraw()
draw.display_draw()