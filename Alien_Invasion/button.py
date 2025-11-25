import pygame.font
import random

class Button:
    """A class to create a button."""
    
    def __init__(self, ai_game, msg):
        """Initialize button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        
        # Set the dimensions and properties of the button.
        self.width, self.height = 200, 50
        self.button_color = (0, 135, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
        #random movements of start button 
        self.x_direction = random.choice([1, -1]) 
        self.y_direction = random.choice([1, -1])
        
        # The button message needs to be prepped only once.
        self._prep_msg(msg)
    
    def update(self):
        """Update the the button's random movement """
        self.x += self.x_direction * self.settings.button_speed
        self.y += self.y_direction * self.settings.button_speed
        
        self.rect.x = self.x
        self.rect.y = self.y
        
        # 3. Synchronize the text position to the button's new center 🎯
        self.msg_image_rect.center = self.rect.center
        # Apply speed and direction to the float position
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            self.x_direction *= -1
            
        if self.rect.bottom >= self.screen_rect.bottom or self.rect.top <= 0:
            self.y_direction *= -1
            
        
        
        
       
        
        
           
    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
        
    def draw_button(self):
        """Draw blank button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
           
        
        
        
