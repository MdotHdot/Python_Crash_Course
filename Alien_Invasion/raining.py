# raining using Pygame and OOP principles with raindrop class
import pygame
import sys
from raindrops import Raindrop
from pygame.sprite import Group

def __init__(self):
    """Initialize the raindrop game and create game resources."""
    pygame.init()
    self.settings = Settings()
    self.clock = pygame.time.Clock()
    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    self.settings.screen_width = self.screen.get_rect().width
    self.settings.screen_height = self.screen.get_rect().height
    pygame.display.set_caption("Raindrop Simulation")
    
    self.raindrops = Group()
    
    self._create_fleet()
    
    # Set the background color
    self.bg_color = (200, 230, 250)
    
