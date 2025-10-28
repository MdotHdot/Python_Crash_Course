# python crash course excersises 13-1 making a grid of stars 
import pygame
import sys
from random import randint # Changed import for cleaner calls

class StarGrid:
    def __init__(self):
        pygame.init()
        self.screen_width = 800
        self.screen_height = 600
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Star Grid")
        
        # Load and resize the image once to be more efficient
        self.star_image = pygame.image.load('images/star.png')
        self.star_image = pygame.transform.scale(self.star_image, (50, 50))

    def _create_star(self, x_position, y_position):
        """Create a single star at a specific position."""
        # This function is now much simpler!
        rect = self.star_image.get_rect()
        rect.x = x_position
        rect.y = y_position
        return self.star_image, rect

    def _create_stars(self): # Renamed for clarity
        """Create a set of randomly placed stars."""
        stars = []
        number_of_stars = 25 # You can change this number
        
        # Get the star's dimensions
        star_rect = self.star_image.get_rect()
        star_width, star_height = star_rect.size

        # A 'for' loop is perfect for when you know how many times to repeat
        for _ in range(number_of_stars):
            random_x = randint(0, self.screen_width - star_width)
            random_y = randint(0, self.screen_height - star_height)
            stars.append(self._create_star(random_x, random_y))
            
        return stars

    def run_game(self):
        """Main game loop."""
        stars = self._create_stars()
    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        sys.exit()

        # --- Twinkle Logic ---

            # 1. ADD a star occasionally
            # We can also add a condition to not let the screen get too crowded
            if randint(1, 100) <= 10 and len(stars) < 50:
                star_rect = self.star_image.get_rect()
                star_width, star_height = star_rect.size
                
                stars.append(self._create_star(
                    randint(0, self.screen_width - star_width),
                    randint(0, self.screen_height - star_height)
                ))

            # 2. REMOVE a star occasionally
            # The 'and stars' part is a quick way to check if the list is not empty
            if randint(1, 100) <= 10 and stars:
                stars.pop(randint(0, len(stars) - 1))

            # --- Drawing Section ---
            self.screen.fill((0, 0, 0))
            for star_image, star_rect in stars:
                self.screen.blit(star_image, star_rect)
            pygame.display.flip()
        
def main():
    star_grid = StarGrid()
    star_grid.run_game()

if __name__ == '__main__':
    main()