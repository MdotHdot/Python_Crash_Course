#Class for the bullets fired from the ship
import pygame
from pygame.sprite import Sprite
from menu_ship import MenuShip

class Bullet(Sprite):
    def __init__(self, ai_game, firing_ship):
        """Create a bullet object at the ship's current position."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        
        
        '''Determine which axis and ship this is firing from'''
        
        # Check if the firing_ship is an instance of the MenuShip class.
        self.is_menu_bullet = isinstance(firing_ship, MenuShip)
        
        if self.is_menu_bullet:
            self.rect.midleft = firing_ship.rect.midright
            # Shooting Menu Ship bullets
            self.x = float(self.rect.x)
            # Rotate the bullet rect by swapping width and height for horizontal bullets
            self.rect.width, self.rect.height = self.settings.bullet_height, self.settings.bullet_width
            
         

        else:
            self.rect.midtop = firing_ship.rect.midtop
            #shoothing from Shop Class
            self.y = float(self.rect.y)
        
    def update(self):
        """Move the bullet based on its source (menu or game ship)."""
        if self.is_menu_bullet:
            # Menu ship fires right (positive x direction)
            self.x += self.settings.bullet_speed
            self.rect.x = self.x
        else:
            # Game ship fires up (negative y direction)
            self.y -= self.settings.bullet_speed
            self.rect.y = self.y
        """Move the bullet up the screen."""
    
    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)   