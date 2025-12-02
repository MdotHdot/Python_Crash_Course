import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    """A class to to report scoring information"""
    def __init__(self, ai_game):
        '''initialize scorekeeping attributes.'''
        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats= ai_game.stats
        
        #Font settings for scoring information
        self.text_color = (255,255,255)
        self.font = pygame.font.SysFont(None,48)
        
        #Prepare the initial score image.
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
        
    def prep_score(self):
        """Turn the score into rendered image"""
        score_str = str(self.stats.score)
        rounded_score =round(self.stats.score, -1)
        score_str = F'Score:{rounded_score}'
        self.score_image = self.font.render(score_str, True, self.text_color, 
                                            self.settings.bg_color)
        
        #display the score at the top right of the screen 
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top + self.screen_rect.top + 40 
    
    def prep_high_score(self):
        """Turn the high score into rendered image"""
        
        high_score = round(self.stats.high_score, -1)
        high_score_str = f'High Score:{high_score}'
        self.high_score_image = self.font.render(high_score_str, True, self.text_color, 
                                                 self.settings.bg_color)
        
        #display the score at the top right of the screen 
        self.high_score_rect = self.score_image.get_rect()
        self.high_score_rect.left = self.screen_rect.left + 20
        self.high_score_rect.top  = self.screen_rect.top + 20
    
    def check_high_score(self):
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()
    
    def prep_level(self):
        """ Turn level into rendered image""" 
        level_str = str(self.stats.level)
        level_str = f'Level: {level_str}'
        self.level_image = self.font.render(level_str, True, self.text_color, 
                                                 self.settings.bg_color)
        
     #display the level at the top right of the screen 
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.screen_rect.right -300
        self.level_rect.top - 20 
    
    def prep_ships(self):
        """Prepare the group of ship sprites representing remaining lives."""         
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 350 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)
            
    def show_score(self):
        """Draw score, levels and ships remain on screen on screen """
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)