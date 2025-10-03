#draws the pilot 
import pygame
class Pilot:
    def __init__(self, ai_game):
        """Add pilot to screen"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.image = pygame.image.load('images/archerspace.bmp')
        self.rect = self.image.get_rect()
        self.rect.topright = self.screen_rect.topright
        
    def blitme(self):
        """Draw the pilot at its current location."""
        self.screen.blit(self.image, self.rect)