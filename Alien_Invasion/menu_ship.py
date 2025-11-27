import pygame

class MenuShip:
    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        
        # Load the ship image, rotate it, and get its rect.
        original_image = pygame.image.load('images/ship.bmp')
        # Rotate the image 90 degrees clockwise
        self.image = pygame.transform.rotate(original_image, -90) 
        self.rect = self.image.get_rect()

        # Start each new ship at the mid-left of the screen.
        self.rect.midleft = self.screen_rect.midleft
        
        # Store a float for the ship's vertical position
        self.y = float(self.rect.y)
        
        # Movement flags for vertical movement
        self.moving_up = True
        self.moving_down = True
        
    def update(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's y value, not the rect.
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
            
        # Update rect object from self.y.
        self.rect.y = self.y
        
    def center_ship(self):
        """Center the ship on the left side of the screen."""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)
        
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)